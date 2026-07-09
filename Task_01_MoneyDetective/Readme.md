# Money Detective

Money Detective is a small Python project that analyzes transaction history to spot financial leaks such as recurring charges, forgotten subscriptions, and duplicate payments. It helps reveal where money is being spent repeatedly, so the user can review unnecessary spending and make better decisions.

## Tech Stack

- Python 3
- Pandas
- CSV/TSV data processing

## How It Works

The script loads transaction data from `data.csv`, cleans the description and amount fields, parses timestamps, and then searches for repeated expenses, cross-month charges, and suspicious back-to-back transactions. The output is printed in a simple text report.

## Files

- `MoneyDetective.py` - main analysis script
- `data.csv` - transaction dataset(Removed Due to Privacy Reasons)
- `Report.md` - project report
- `Result.png` - result screenshot
