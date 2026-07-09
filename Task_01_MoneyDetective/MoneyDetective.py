from pathlib import Path
from datetime import timedelta

import pandas as pd

# 1. LOAD THE DATA
data_path = Path(__file__).with_name("data.csv")
df = pd.read_csv(data_path, sep="\t", engine="python")

# Normalize column names and ensure correct data types
df.columns = [column.strip().title() for column in df.columns]
df["Date"] = pd.to_datetime(
    df["Timestamp"].astype(str).str.replace(r"\s+", " ", regex=True).str.strip(),
    format="mixed",
    dayfirst=True,
)
df["Description"] = df["Description"].astype(str)
df["Amount"] = pd.to_numeric(
    df["Amount"].astype(str).str.replace(",", "", regex=False).str.replace("+", "", regex=False),
    errors="coerce",
)
df["Clean_Desc"] = df["Description"].str.lower().str.strip() # Normalize text
df["Month"] = df["Date"].dt.to_period("M")

print("--- FINANCIAL LEAK ANALYSIS REPORT ---\n")

# ==========================================
# LEAK 1: RECURRING CHARGES
# ==========================================
print("1. RECURRING CHARGES (Potential Subscriptions)")
print("-" * 40)
# Filter only expenses (negative amounts)
expenses = df[df['Amount'] < 0]
recurring = expenses.groupby('Clean_Desc').agg(
    Times_Charged=('Amount', 'count'),
    Total_Leaked=('Amount', 'sum')
).sort_values(by='Times_Charged', ascending=False)

# Only show things that happened more than once
recurring = recurring[recurring['Times_Charged'] > 1]
for desc, row in recurring.iterrows():
    print(f"⚠️  {desc.upper()}: Charged {row['Times_Charged']} times. Total lost: Rs. {abs(row['Total_Leaked']):,.2f}")

# ==========================================
# LEAK 2: FORGOTTEN SUBSCRIPTIONS (Monthly)
# ==========================================
print("\n2. FLAGGED FORGOTTEN SUBSCRIPTIONS (Cross-Month)")
print("-" * 40)
monthly_expenses = expenses.groupby(['Clean_Desc', 'Month']).size().reset_index(name='Counts')
subs = monthly_expenses.groupby('Clean_Desc').filter(lambda x: len(x) > 1)['Clean_Desc'].unique()

for sub in subs:
    print(f"🔴 ALERT: '{sub.upper()}' appears in multiple months. Is this an active subscription you forgot to cancel?")

# ==========================================
# LEAK 3: DUPLICATES & SUSPICIOUS REFUNDS
# ==========================================
print("\n3. DUPLICATES & SUSPICIOUS ACTIVITY (2-Minute Window)")
print("-" * 40)
df_sorted = df.sort_values(by='Date').reset_index(drop=True)
duplicates_found = False

for i in range(len(df_sorted) - 1):
    current_row = df_sorted.iloc[i]
    next_row = df_sorted.iloc[i + 1]
    
    # Calculate time difference
    time_diff = next_row['Date'] - current_row['Date']
    
    # If two transactions happen within 2 minutes
    if time_diff <= timedelta(minutes=2):
        # Check if it's a perfect duplicate (same sign) OR a suspicious immediate reversal (Opposite signs, similar amount)
        if (current_row['Amount'] < 0 and next_row['Amount'] < 0) or (current_row['Amount'] > 0 and next_row['Amount'] > 0):
            print(f"🔴 DUPLICATE PAYMENT: '{current_row['Description']}' and '{next_row['Description']}' happened {time_diff}. Check this!")
            duplicates_found = True
        elif (current_row['Amount'] < 0 and next_row['Amount'] > 0):
            # Flag if the refund is roughly the same amount as the debit
            if abs(abs(current_row['Amount']) - next_row['Amount']) < 50: 
                print(f"🟡 SUSPICIOUS REVERSAL: You paid Rs. {abs(current_row['Amount']):.2f} to '{current_row['Description']}',")
                print(f"   but received Rs. {next_row['Amount']:.2f} from '{next_row['Description']}' just {time_diff} later.")
                print(f"   -> This looks like a cancelled order, OR potentially a money loop/scam tactic.")

if not duplicates_found:
    print("No exact duplicates found in the 2-minute window.")