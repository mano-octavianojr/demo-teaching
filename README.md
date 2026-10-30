# Python Foundations

A beginner college lesson using a fictional **student grade analyzer**. The 48-slide presentation covers Python through text and CSV file reading and writing. Allow **42 minutes**, or use the instructor guide for 30-minute, 45-minute, and 6-minute routes.

Django (web applications), NumPy (numerical arrays for analysis), and TensorFlow (machine learning) are examples of later applications. They are not dependencies of this course.

## How to access

### Run in Google Colab

Click an **Open in Colab** button in the lessons table to run that notebook in your browser. No local installation is needed. Sign in to Google if prompted, then choose **File → Save a copy in Drive** to keep your notebook work. Run cells in order using **Shift+Enter**, or choose **Runtime → Run all**.

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

In JupyterLab open the `notebooks` folder, start with lesson 01, and press **Shift+Enter** to run each cell. Every notebook also works independently. To reset notebook state, restart the kernel and run all cells from the beginning. Standard-library lesson code needs no package installation in Colab. `requirements.txt` installs local notebook tools.

### Run the complete script

From the project folder, using the activated environment:

```bash
python grade_analyzer.py
```

The script needs no third-party packages. You can also use `python3 grade_analyzer.py` on macOS/Linux without activating an environment. It anchors paths to the script's location, so it also works when launched from another folder.

## Lessons

| Notebook | Python focus | Run online |
| --- | --- | --- |
| [01 — First Steps](notebooks/01_first_steps.ipynb) | Printing, strings, comments | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/demo-teaching/blob/main/notebooks/01_first_steps.ipynb) |
| [02 — Variables and Calculations](notebooks/02_variables_calculations.ipynb) | Variables, types, operators, conversion | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/demo-teaching/blob/main/notebooks/02_variables_calculations.ipynb) |
| [03 — Student Records](notebooks/03_student_records.ipynb) | Strings, lists, dictionaries | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/demo-teaching/blob/main/notebooks/03_student_records.ipynb) |
| [04 — Decisions and Repetition](notebooks/04_decisions_repetition.ipynb) | Conditions, loops, accumulation | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/demo-teaching/blob/main/notebooks/04_decisions_repetition.ipynb) |
| [05 — Reusable Functions](notebooks/05_reusable_functions.ipynb) | Functions, return values, errors | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/demo-teaching/blob/main/notebooks/05_reusable_functions.ipynb) |
| [06 — Files and Grade Analyzer](notebooks/06_files_grade_analyzer.ipynb) | Text/CSV files and complete analyzer | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mano-octavianojr/demo-teaching/blob/main/notebooks/06_files_grade_analyzer.ipynb) |

Notebook links open the lessons on GitHub. Colab badges open the same notebooks in your browser.

## Expected result

The sample CSV contains Maya (88), Luis (72), Ari (95), and Bea (75). Both lesson 06 and the script produce:

```text
Students: 4
Class average: 82.50
Passing threshold (illustrative): 75
Passing students: 3
Names: Maya, Ari, Bea
```

The report is `outputs/grade_summary.txt`. A final `Saved:` line prints its runtime-specific location. A threshold of **75 is a teaching example**, not institutional policy. With a threshold of 90, only Ari passes and the mean remains 82.50.

CSV headers must be `name,grade`. Grades must be finite numbers from 0 to 100 and names must be nonempty. A header-only file gives `No student records.`. Invalid data produce an explanatory error. Edit a copy of the fictional CSV for practice. The notebook chooses the repository root when started in `notebooks/`, otherwise the current working folder. The script always uses its own folder.

## Presentation

- `presentation.tex`: standalone 16:9 LaTeX Beamer deck, exactly 48 slides. Code uses `listings` and needs no shell escape or Python package. The DLSU CCS logo is the supplied `DLSU-CCS-Logo-Clear.png`; keep it beside the LaTeX source.
- `instructor_guide.md`: slide-by-slide speaking notes, timing, questions, and the 6-minute live demo script. Setup happens before the timed lesson.

The source remains open in Codex's built-in LaTeX editor. Its current single-file compiler cannot load the separate logo PNG, so the branded deck requires a project-capable LaTeX compiler (for example an existing local TeX setup or Overleaf) with the source and PNG together. The student view hides notes by default. The instructor guide explains how to enable notes. With an existing local LaTeX installation, compile twice using `pdflatex presentation.tex` or use `latexmk -pdf presentation.tex`. Do not run these commands inside a Python cell.

| Slides | Content | Suggested time |
| --- | --- | --- |
| 1–6 | The report task, Python background, and execution | 4 min |
| 7–14 | One student: output, values, calculations, and errors | 9 min |
| 15–18 | A class: lists and student dictionaries | 5 min |
| 19–30 | Processing records: decisions and loop traces | 9 min |
| 31–38 | Organizing reusable functions | 6 min |
| 39–43 | Keeping results: text files and CSV input | 5 min |
| 44–48 | Complete analyzer, saved report, practice, and applications | 4 min |

Slide notes target approximately 42 minutes. Running Python setup stays in this README rather than the slides. For 45 minutes add three minutes of guided practice. For 30 minutes summarize designated reference slides. The short route has a separate six-minute schedule in the instructor guide. Timing is a delivery target, not a recorded classroom rehearsal.

The adapted `nu_template_example.tex` is a separate five-slide DLSU CCS Python teaching example. It no longer depends on the unavailable NU life-insurance package and uses the same supplied logo.

## Repository

The materials are hosted at [mano-octavianojr/demo-teaching](https://github.com/mano-octavianojr/demo-teaching) on the `main` branch. All examples use fictional student data.

## Official references

- [Python tutorial](https://docs.python.org/3/tutorial/) — supplementary reference, assumes some programming knowledge.
- [Python files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files), [csv](https://docs.python.org/3/library/csv.html), and [pathlib](https://docs.python.org/3/library/pathlib.html).
- [Django](https://www.djangoproject.com/), [NumPy](https://numpy.org/), and [TensorFlow](https://www.tensorflow.org/).
- [Google Colab FAQ](https://research.google.com/colaboratory/faq.html).
