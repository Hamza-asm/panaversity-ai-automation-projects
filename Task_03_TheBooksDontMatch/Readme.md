# The Books Don't Match

The Books Don't Match is a Python project that reconciles messy payment logs against an expected collection target. It turns confusing transaction data into a clear summary of who paid, who still owes money, and how much is missing from the total.

## Tech Stack

- Python 3
- Standard library modules: `csv`, `io`

## How It Works

The script reads a messy CSV payment log, applies alias rules and memo filters, matches payments to the target list, and calculates the total collected amount. It then prints the remaining gap and a clear list of outstanding balances.

## Files

- `BooksDont.py` - main reconciliation script
- `data.csv` - payment log dataset
- `Report.md` - project report
- `Result.png` - output screenshot
