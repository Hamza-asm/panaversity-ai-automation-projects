# Task 01 Report: Money Detective

## Project Title and Problem It Solves

**Money Detective** is a Python project that analyzes bank transaction history to find financial leaks. It helps identify recurring charges, potential forgotten subscriptions, and duplicate or suspicious payments. The main problem it solves is making hidden spending patterns visible so the user can review where money is going.

## AI Tool(s) Used

- GitHub Copilot in VS Code & Glm 5 Turbo
- Python with the Pandas library for the analysis logic

## Initial Prompt and Improved Prompts

### Initial Prompt

>"Act as a programmer. I want to find financial leaks in my transaction history. Here is my transaction data attached as ss. Write a script that analyzes this data to identify recurring charges, flag potential forgotten subscriptions, and catch duplicate payments. Also, please explain the logic of your code in plain English so I understand exactly how it is searching for these leaks."

### Improved Prompt

"Fix the Python script so it correctly reads the attached transaction file, handles the real file format, and avoids parsing errors. Keep the same analysis goals: recurring charges, forgotten subscriptions, and duplicate payments. Also make the date parsing reliable for mixed timestamp formats."

## How I Verified the Result

I manually checked the transactions shown in the output against my bank statements, and the results were correct. The recurring Foodpanda charges matched what I saw in my statements, so the analysis was validated against known real transactions.

## What Worked, What Did Not, and Problems Faced

What worked was the final transaction analysis logic and the overall detection of repeated spending patterns. What did not work at first was the CSV loading and date parsing because the file format was different from what the script expected. The script initially gave parsing and grouping errors, but those were fixed by adjusting the file reader and timestamp handling.

## Final Result and What I Learned

The final result showed that I spend too much on Foodpanda because I eat fast food too often, so I need to control that spending. I also learned how to clean transaction data, handle malformed input files, and use Pandas to find repeating financial patterns.

## Result Screenshot

See [Result.png](Result.png) for the final output screenshot.