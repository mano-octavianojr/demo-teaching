# Python Foundations Student Guide

Learn Python by building a report from fictional student grades. You will practice displaying values, working with collections, making decisions, repeating steps, writing functions, and reading and saving files. All six lessons are in one notebook so you can move between topics using its contents list.

## Open your notebook

### Google Colab

1. Open the [Python Foundations notebook in Colab](https://colab.research.google.com/github/mano-octavianojr/demo-teaching/blob/main/notebooks/python_foundations.ipynb).
2. Sign in to Google if prompted.
3. Choose **File → Save a copy in Drive** to keep your own editable notebook.
4. Use the notebook's **Contents** links to choose a lesson. Start with lesson 01 if you are new to Python.
5. Select a code cell and press **Shift+Enter** to run it and move to the next cell.

No local installation is needed. The lesson code uses Python's standard library. Django, NumPy, and TensorFlow are examples of later applications; you do not need them for these lessons.

### Local JupyterLab

Install Python 3.10 or newer. Clone the repository, or download and extract its ZIP:

```bash
git clone https://github.com/mano-octavianojr/demo-teaching.git
cd demo-teaching
```

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m jupyter lab
```

On Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m jupyter lab
```

If PowerShell blocks activation, use the environment's executable directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m jupyter lab
```

Open `notebooks/python_foundations.ipynb` in JupyterLab and use the clickable contents list to choose a lesson. Begin with lesson 01 for the full course. Each lesson section also works independently; run its cells in order. Restart the kernel and run all cells from the beginning to reset its state.

`requirements.txt` supplies local notebook tools. Django, NumPy, and TensorFlow are examples of future applications and are not required for this course.

## Lesson sequence

| Lesson | Topics |
| --- | --- |
| [01 — First Steps](../notebooks/python_foundations.ipynb#lesson-01) | Printing, strings, and comments. |
| [02 — Variables and Calculations](../notebooks/python_foundations.ipynb#lesson-02) | Variables, types, operators, and conversion. |
| [03 — Student Records](../notebooks/python_foundations.ipynb#lesson-03) | Strings, lists, and dictionaries. |
| [04 — Decisions and Repetition](../notebooks/python_foundations.ipynb#lesson-04) | Conditions, loops, and accumulation. |
| [05 — Reusable Functions](../notebooks/python_foundations.ipynb#lesson-05) | Functions, return values, and errors. |
| [06 — Files and Grade Analyzer](../notebooks/python_foundations.ipynb#lesson-06) | Text files, CSV input, and the complete analyzer. |

Run cells in order within the lesson you select. The lessons build toward representing student records, processing grades, organizing reusable functions, and saving results.

## Work through a lesson

Each lesson includes explanations, runnable examples, expected results, practice cells, solutions, and an exit check.

1. Read the explanation and predict what the next code cell will display.
2. Run the cell with **Shift+Enter** and compare the result with the expected output.
3. Complete **Your turn** in the blank practice cell before reading the solution.
4. Use the solution to check your approach, then answer the exit check in your own words.
5. Select **Back to contents** to choose another lesson.

You can start any lesson independently, but run that lesson's cells in order so its variables and functions are available. A notebook remembers values from earlier executions. To check your work from a clean state, restart the kernel or runtime and run the cells again in order. **Run all** also executes the provided solution cells.

## Build your grade report

Lesson 06 combines the earlier skills into a complete analyzer. It reads student records, calculates a class average, identifies passing students, and writes a text report. Run the lesson from its setup cell through its analysis and writing cells.

The notebook creates fictional sample data if no local copy exists. You do not need to upload data or mount Google Drive. Existing CSV data are preserved, and generated reports are replaced when you run the same writing steps again.

The sample records are:

```csv
name,grade
Maya,88
Luis,72
Ari,95
Bea,75
```

With these records, your report should show:

```text
Students: 4
Class average: 82.50
Passing threshold (illustrative): 75
Passing students: 3
Names: Maya, Ari, Bea
```

The passing threshold of 75 is a teaching example, not institutional policy. The final **Saved:** line tells you where your report was written.

### Practice with a different threshold

Before running the lesson 06 exercise, predict who will pass with a threshold of 90. Try the exercise in its practice cell and save a second report so you can compare the two results. Only Ari passes at 90; the class average remains 82.50 because the input grades have not changed.

### Practice with CSV data

Use a copy of the fictional sample data for experiments. Keep the header exactly `name,grade`. Each student needs a nonempty name and a finite numeric grade from 0 to 100. A file containing only the header gives `No student records.` Invalid input produces an explanatory error.

## Save your work and report

Saving your notebook preserves your code and written work. In Colab, it does not automatically preserve files generated in the runtime.

To keep your report in Colab:

1. Open the **Files** sidebar and refresh the listing.
2. Find `outputs/grade_summary.txt`.
3. Open the file's menu and choose **Download**.
4. Download any additional practice reports you want to retain before the runtime resets.

When working locally, use the location printed after **Saved:** to find the report. Copy or rename a report you want to preserve before rerunning a cell that writes to the same filename.

## Troubleshooting

| Problem | What to try |
| --- | --- |
| A variable or function is not defined. | Run the earlier setup cells in the selected lesson, in order. |
| Results differ after editing or rerunning cells. | Restart the kernel or runtime and run the lesson again from its beginning. |
| A grade cannot be converted to a number. | Check for words, blank values, or extra characters in the grade field. |
| CSV input is rejected. | Check the `name,grade` headers, nonempty names, and numeric grades between 0 and 100. |
| A Colab report disappeared after a runtime reset. | Rerun lesson 06 to generate it again. Download reports before leaving the session. |
| PowerShell blocks environment activation. | Use the virtual environment's Python executable directly, as shown in the local setup instructions. |

## Check your understanding

Before finishing, make sure you can explain how a student record is represented, how a loop processes the class, how a function returns a result, and how a CSV input becomes a saved report. Change one value at a time and predict the effect before running your code.

For additional reading, see the [official references in the README](../README.md#official-references).
