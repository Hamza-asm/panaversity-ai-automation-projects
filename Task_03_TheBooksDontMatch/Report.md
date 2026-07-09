# Task 03 Report: The Books Don't Match

## Project Title and Problem It Solves

**The Books Don't Match** is a Python reconciliation script that cleans up a messy digital payment log and compares it to the expected collection target for a Northern Tour. It solves the problem of tracking who has paid, who still owes money, and how much money is missing from the total.

## AI Tool(s) Used

- GitHub Copilot in VS Code & Glm5 Turbo
- Python standard library for the parsing and reconciliation logic

## Initial Prompt and Improved Prompts

### Initial Prompt

```
"Act as a programmer. I need a Python script to reconcile a set of books. I have an expected total that I need to collect for a Northern Tour, and I have a messy digital payment log.

The Target:
I need to collect exactly $50 from 5 specific people: Kamal, Ismail, Ahmed, Bilal, and Zain. The expected total is $250.

The Messy Digital Log (CSV format):
Date,Sender,Amount,Memo
07/01,Kamal Mirza,50.00,northern tour
07/02,IDK_007,50.00,trip
07/03,Ahmed_99,25.00,tour deposit
07/04,Bilal,15.00,lunch yesterday
07/05,Z.A.,50.00,north

My Rules for Interpreting the Data:

The sender "IDK_007" is Ismail.

The sender "Z.A." is Zain.

The sender "Ahmed_99" is Ahmed.

Any transaction with the word "lunch" in the memo should be completely ignored; it does not count toward the tour funds.

The Task:
Write a Python script that parses this data, applies my rules, and calculates the total amount actually collected for the tour. Then, have the script print out the total gap (how much money is missing from the $250 target) and provide a specific list of who still owes money and exactly how much they owe. Use standard libraries only so I can run this easily. Add comments explaining the logic."
```

### Improved Prompt

```
"Keep the solution limited to Python standard libraries, and make the reconciliation logic easy to follow with comments. Also make sure the script clearly reports ignored transactions, matched payments, the gap from the target, and the outstanding balances per person."
```

## How I Verified the Result

I double-checked the data manually and calculated the totals myself. The script output matched the manual calculation, so the reconciliation result was correct.

## What Worked, What Did Not, and Problems Faced

What worked was the rule-based matching of aliases, the memo filter, and the final owed-balance summary. The only problem I faced was a typo in the data name, which I corrected. After that, the code ran on the first try.

## Final Result and What I Learned

The final result turned messy payment records into a clear picture of who paid and who still owes money. I learned how to use simple parsing rules to reconcile inconsistent data and make the output easier to understand.

## Result Screenshot

See [Result.png](Result.png) for the final output screenshot.