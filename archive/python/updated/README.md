# Python Foundations

A beginner college lesson using a fictional **student grade analyzer**. The 48-slide presentation covers Python through text and CSV file reading and writing. Allow **42 minutes**, or use the instructor guide for 30-minute, 45-minute, and 6-minute routes.

All six lessons are sections of one [Python Foundations notebook](notebooks/python_foundations.ipynb), with clickable contents for quick navigation.

Django (web applications), NumPy (numerical arrays for analysis), and TensorFlow (machine learning) are examples of later applications. They are not dependencies of this course.

For learners, see the [student guide (Word)](docs/documentation.docx) or its [online text version](markdown/documentation.md). For teaching notes and delivery routes, see the [instructor guide](markdown/instructor_guide.md).

## How to access

### Run in Google Colab

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/demo-teaching/blob/main/notebooks/python_foundations.ipynb)

Open the notebook using the button above, then use its **Contents** links to choose a lesson. No local installation is needed. Sign in to Google if prompted, then choose **File → Save a copy in Drive** to keep your notebook work. Run cells in order using **Shift+Enter**. Use **Runtime → Run all** only when you want to execute the entire notebook, including the provided solutions.

Lesson 06 automatically **creates its fictional sample data when no local copy exists**. It does not fetch data from GitHub, request uploads, or mount Google Drive. Existing CSV data are preserved. Reports are replaced on repeat runs.

To keep a generated report, open the **Files** sidebar, refresh the listing, find `outputs/grade_summary.txt`, open its menu, and choose **Download**. Runtime files are temporary. Saving the notebook to Drive does not automatically preserve generated files.

### Run locally

Install **Python 3.10 or newer**, then clone [this repository](https://github.com/mano-octavianojr/demo-teaching) or download and extract its ZIP. Open a terminal in the project folder.

```bash
git clone https://github.com/mano-octavianojr/demo-teaching.git
cd demo-teaching
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m jupyter lab
```

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m jupyter lab
```

If PowerShell blocks activation, use the environment's executable directly, without changing system policy:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m jupyter lab
```

In JupyterLab, open `notebooks/python_foundations.ipynb` and use its **Contents** links to choose a lesson. Start with lesson 01 for the complete course and press **Shift+Enter** to run each cell. Each lesson section also works independently; run its cells in order. To reset notebook state, restart the kernel and run all cells from the beginning. Standard-library lesson code needs no package installation in Colab. `requirements.txt` installs local notebook tools.

### Run the example program

The grade analyzer is the completed example program, not an answer checker. It reads fictional grades and writes a report; it does not assess notebook answers.

From the project folder, using the activated environment:

```bash
python examples/grade_analyzer.py
```

The script needs no third-party packages. You can also use `python3 examples/grade_analyzer.py` on macOS/Linux without activating an environment. It resolves repository paths from the script's location, so it also works when launched from another folder.

## Lessons

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/demo-teaching/blob/main/notebooks/python_foundations.ipynb)

The [Python Foundations notebook](notebooks/python_foundations.ipynb) contains all six sections below. Use its **Contents** links to jump to a section and **Back to contents** to return. Each section includes explanations, examples, practice cells, and solutions. Run the selected section's cells in order, including its setup cells. If a contents link does not jump in your notebook viewer, use its table of contents sidebar to select the lesson.

Try each practice cell before reading or running its solution. Both share the same Python session, so a solution that appends to a list can repeat your own changes. Rerun the lesson's setup cell before comparing that solution.

| Section | Python focus |
| --- | --- |
| 01 — First Steps | Printing, strings, comments |
| 02 — Variables and Calculations | Variables, types, operators, conversion |
| 03 — Student Records | Strings, lists, dictionaries |
| 04 — Decisions and Repetition | Conditions, loops, accumulation |
| 05 — Reusable Functions | Functions, return values, errors |
| 06 — Files and Grade Analyzer | Text/CSV files and complete analyzer |

## Final project output

The grade report below is the **final project output of the course**, created in **lesson 06** by combining the skills practiced in lessons 01–05: values, collections, decisions, loops, and functions. Earlier lessons have their own examples and exercises; they build toward this report.

Run lesson 06’s setup and analyzer cells in order to generate the report. You can also produce the same result with `python examples/grade_analyzer.py`.

Using the sample CSV with Maya (88), Luis (72), Ari (95), and Bea (75), the final report is:

```text
Students: 4
Class average: 82.50
Passing threshold (illustrative): 75
Passing students: 3
Names: Maya, Ari, Bea
```

The report is `outputs/grade_summary.txt`. A final `Saved:` line prints its runtime-specific location. A threshold of **75 is a teaching example**, not institutional policy. With a threshold of 90, only Ari passes and the mean remains 82.50.

CSV headers must be `name,grade`. Grades must be finite numbers from 0 to 100 and names must be nonempty. A header-only file gives `No student records.`. Invalid data produce an explanatory error. Edit a copy of the fictional CSV for practice. The notebook chooses the repository root when started in `notebooks/`, otherwise the current working folder. The script always uses the repository root, resolved from its location in `examples/`.

## Presentation

- `lectures/presentation.tex`: standalone 16:9 LaTeX Beamer deck, exactly 48 slides. Code uses `listings` and needs no shell escape or Python package. The DLSU CCS logo is the supplied `template/DLSU-CCS-Logo-Clear.png`, referenced by its relative path from `lectures/`.
- `markdown/instructor_guide.md`: slide-by-slide speaking notes, timing, questions, and the 6-minute live demo script. Setup happens before the timed lesson.

Use a project-capable LaTeX compiler (an existing local TeX installation or Overleaf) with both `lectures/` and `template/` preserving their relative layout. The student view hides speaker notes by default; the instructor guide explains how to enable them. From the project folder, compile locally with:

```bash
cd lectures
pdflatex presentation.tex
pdflatex presentation.tex
```

Alternatively, run `latexmk -pdf presentation.tex` from `lectures/`. These are terminal commands, not Python code. The PDF is written beside the source by these commands. For Overleaf, upload both folders and select `lectures/presentation.tex` as the main document. Full lesson code is in the notebook; slide snippets may rely on earlier definitions and are not independent scripts.

| Slides | Content | Approximate time |
| --- | --- | --- |
| 1–6 | The report task, Python background, and execution | 4 min |
| 7–14 | One student: output, values, calculations, and errors | 9 min |
| 15–18 | A class: lists and student dictionaries | 5 min |
| 19–30 | Processing records: decisions and loop traces | 9 min |
| 31–38 | Organizing reusable functions | 6 min |
| 39–43 | Keeping results: text files and CSV input | 5 min |
| 44–48 | Complete analyzer, saved report, practice, and applications | 4 min |

Slide notes target approximately 42 minutes for the presentation and brief demonstrations; completing every notebook exercise takes additional time. Running Python setup stays in this README rather than the slides. For 45 minutes add three minutes of guided practice. For 30 minutes summarize designated reference slides. The short route has a separate six-minute schedule in the instructor guide. Timing is a delivery target, not a recorded classroom rehearsal.

## Repository

```text
template/        # Shared presentation assets
docs/            # Project documentation
lectures/        # LaTeX lecture deck
notebooks/       # Combined notebook with six lesson sections
data/            # Fictional sample data
examples/        # Grade analyzer script
README.md
requirements.txt
markdown/        # Other Markdown files, including the instructor guide
```

Generated reports go to the ignored `outputs/` folder at the repository root.


The materials are hosted at [mano-octavianojr/demo-teaching](https://github.com/mano-octavianojr/demo-teaching) on the `main` branch. All examples use fictional student data.

## Official references

- [Python tutorial](https://docs.python.org/3/tutorial/) — supplementary reference, assumes some programming knowledge.
- [Python files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files), [csv](https://docs.python.org/3/library/csv.html), and [pathlib](https://docs.python.org/3/library/pathlib.html).
- [Django](https://www.djangoproject.com/), [NumPy](https://numpy.org/), and [TensorFlow](https://www.tensorflow.org/).
- [Google Colab FAQ](https://research.google.com/colaboratory/faq.html).
