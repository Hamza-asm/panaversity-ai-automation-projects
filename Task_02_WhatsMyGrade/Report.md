# Task 02 Report: Whats My Grade

## Project Title and Problem It Solves

**Whats My Grade** is a Python grading calculator that determines a student's exact current percentage from quiz, assignment, and midterm scores. It solves the problem of manually calculating weighted grades and removes confusion about what score is needed on the final exam to get an A.

## AI Tool(s) Used

- GitHub Copilot in VS Code & Glm 5 Turbo
- Python for the grading logic and calculations

## Initial Prompt and Improved Prompts

### Initial Prompt

>"Act as a programmer. I need a script to calculate my exact current grade for a class. Here are my raw scores: quiz 13 assignment 13 mid 18. Here is my teacher's grading policy: Quiz 15 marks Assignment 15 marks Mid Term 20 Marks Finals 50 Marks. Write a script that applies these exact rules to calculate my current percentage. After that, add a feature to the script that calculates exactly what score I need on the final exam to get an A in the class."

### Improved Prompt

"Add the grading criteria table to the script so it can also show the letter grade and GPA for the current percentage. Keep the calculations simple and exact, and print the final-exam requirement clearly."

## How I Verified the Result

I checked the output manually against the grading rules and the transcript table. The current grade calculation matched the expected weighted result, and the final-exam requirement was consistent with the class policy.

## What Worked, What Did Not, and Problems Faced

What worked was the simple weighted calculation and the grade mapping logic. What did not work at first was that the prompt needed to be translated into exact grading rules and a usable script structure. The main challenge was making the output clear enough to read without losing accuracy.

## Final Result and What I Learned

The final result showed my current standing and the exact mark needed on the final exam to secure an A. I learned how to turn grading policy into working code and how small changes in weighted marks affect the final grade.

## Result Screenshot

See [Result.png](Result.png) for the final output screenshot.