# Task 04 Report: Organize The Mess

## Project Title and Problem It Solves

**Organize The Mess** is a Python cleanup script that helps organize files inside a specific parent folder. It solves the problem of messy folders by finding duplicate files, organizing items by file type, and flagging very large files for manual review. The script is designed to be safe because it does not make changes immediately.

## AI Tool(s) Used

- GitHub Copilot in VS Code & Glm5 Turbo
- Python standard library for file scanning and cleanup logic

## Initial Prompt and Improved Prompts

### Initial Prompt

```
"Write a Python script to clean up a specific folder on my computer by [finding duplicates / organizing by file type / flagging files over 1GB]. Safety is my top priority. Do not write a script that executes these changes immediately. The script must first output a 'dry run' plan showing every file it intends to move, rename, or delete, and it must ask for my typed approval before making any actual changes. Make sure the script only work in parent folder not whole pc"
```

### Improved Prompt

```
"Keep the script limited to the parent folder only, show a dry-run plan before any action, and require typed approval before moving or deleting files. Also make sure duplicate detection and file organization are clearly separated in the output."
```
## How I Verified the Result

I verified the result by running the script in dry-run mode first and checking that it listed the planned file moves and duplicate files before any change was made. After that, I approved the execution and confirmed that the output matched the expected cleanup behavior.

## What Worked, What Did Not, and Problems Faced

What worked was the dry-run workflow and the folder-scoped cleanup logic. What did not work at first was that the script could not find the file after marking it, and in one attempt it created a copy of files on its own, which I had to reset. After the second attempt, it worked successfully.

## Final Result and What I Learned

The final result was a safer cleanup script that organizes a specific folder instead of touching the whole PC. I learned how useful a dry run and approval step are when a script can move or delete files, because it makes the cleanup process much more controlled.

## Result Screenshot

See [Result.png](Result.png) for the final output screenshot.