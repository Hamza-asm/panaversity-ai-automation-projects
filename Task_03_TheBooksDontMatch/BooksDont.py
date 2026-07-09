import csv
import io

# --- 1. CONFIGURATION & RULES ---

# The master list of expected payers and their target amounts
TARGET_PAYERS = ["Jamal", "Ismail", "Ahmed", "Bilal", "Zain"]
EXPECTED_PER_PERSON = 50.00
EXPECTED_TOTAL = 250.00

# Rule: Map known aliases to real names
ALIAS_MAP = {
    "IDK_007": "Ismail",
    "Z.A.": "Zain",
    "Ahmed_99": "Ahmed"
}

# Rule: Keywords that invalidate a transaction for this tour
EXCLUDE_MEMOS_CONTAINING = ["lunch"]

# The messy digital log provided
MESSY_LOG_DATA = """Date,Sender,Amount,Memo
07/01,Jamal,50.00,northern tour
07/02,IDK_007,50.00,trip
07/03,Ahmed_99,25.00,tour deposit
07/04,Bilal,15.00,lunch yesterday
07/05,Z.A.,50.00,north
"""

# --- 2. INITIALIZATION ---

# Dictionary to keep a running tally of what each person has paid
# Starts everyone at $0.00
payments_received = {name: 0.00 for name in TARGET_PAYERS}

# --- 3. PARSING AND APPLYING RULES ---

# Use io.StringIO to turn the text string into a file-like object for the csv reader
log_file = io.StringIO(MESSY_LOG_DATA)
reader = csv.DictReader(log_file)

print("--- PROCESSING TRANSACTIONS ---")
for row in reader:
    original_sender = row['Sender']
    amount = float(row['Amount'])
    memo = row['Memo'].lower() # Convert to lowercase for easy keyword matching
    
    # RULE CHECK 1: Ignore transactions with excluded keywords in the memo
    skip_transaction = False
    for keyword in EXCLUDE_MEMOS_CONTAINING:
        if keyword in memo:
            print(f"IGNORED: ${amount:.2f} from {original_sender} (Memo contained '{keyword}')")
            skip_transaction = True
            break
            
    if skip_transaction:
        continue
        
    # RULE CHECK 2: Apply alias mapping
    resolved_name = original_sender
    if original_sender in ALIAS_MAP:
        resolved_name = ALIAS_MAP[original_sender]
        
    # RULE CHECK 3: Match the resolved name to our target list
    # We use 'in' to catch partial matches (e.g., "Kamal Mirza" contains "Kamal")
    matched_payer = None
    for payer in TARGET_PAYERS:
        if payer.lower() in resolved_name.lower():
            matched_payer = payer
            break
            
    # If we found a match, add the money to their tally
    if matched_payer:
        payments_received[matched_payer] += amount
        print(f"RECONCILED: +${amount:.2f} credited to {matched_payer} (From log entry: {original_sender})")
    else:
        # This handles money from people not on our target list
        print(f"UNMATCHED: ${amount:.2f} from {original_sender} is not part of the Northern Tour.")

# --- 4. RECONCILIATION CALCULATIONS ---

print("\n" + "="*35)
print("--- RECONCILIATION REPORT ---")
print("="*35)

# Calculate total collected
total_collected = sum(payments_received.values())
gap = EXPECTED_TOTAL - total_collected

print(f"Expected Total:  ${EXPECTED_TOTAL:.2f}")
print(f"Actual Collected: ${total_collected:.2f}")
print(f"TOTAL GAP:       ${gap:.2f}")

# --- 5. GENERATING THE OWED LIST ---

print("\n--- OUTSTANDING BALANCES ---")
owed_list = []
for payer in TARGET_PAYERS:
    paid = payments_received[payer]
    remaining = EXPECTED_PER_PERSON - paid
    
    if remaining > 0.01: # Using a small threshold to avoid floating-point math quirks (e.g., 0.0000001)
        owed_list.append((payer, remaining))
        print(f"⚠️  {payer} owes: ${remaining:.2f} (Paid ${paid:.2f} so far)")
    elif paid > 0:
        print(f"✅ {payer}: Paid in full.")

# Final summary of who to chase
if owed_list:
    print("\n--- ACTION REQUIRED ---")
    print("You need to follow up with the following people for the missing funds:")
    for name, amount in owed_list:
        print(f"-> {name}: ${amount:.2f}")
else:
    print("\n🎉 All tour funds have been collected!")