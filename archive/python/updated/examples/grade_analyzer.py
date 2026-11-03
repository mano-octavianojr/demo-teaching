"""Fictional grade analyzer. Run with Python 3.10+; no packages required."""

from pathlib import Path
import csv
import math

PASSING_GRADE = 75  # Illustrative teaching rule, not institutional policy.
SAMPLE_CSV = "name,grade\nMaya,88\nLuis,72\nAri,95\nBea,75\n"


def ensure_sample_data(path):
    """Create fictional sample data only when the file is missing."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        with path.open("w", encoding="utf-8", newline="") as file:
            file.write(SAMPLE_CSV)


def read_students(path):
    """Read name/grade CSV records and reject incomplete or invalid data."""
    students = []
    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        if reader.fieldnames != ["name", "grade"]:
            raise ValueError("CSV headers must be: name,grade")
        for row_number, row in enumerate(reader, start=2):
            name = (row.get("name") or "").strip()
            try:
                grade = float(row["grade"])
            except (TypeError, ValueError) as error:
                raise ValueError(f"Row {row_number}: grade must be a number") from error
            if not name or None in row or not math.isfinite(grade) or not 0 <= grade <= 100:
                raise ValueError(f"Row {row_number}: use a name and a grade from 0 to 100")
            students.append({"name": name, "grade": grade})
    return students


def summarize(students, passing_grade=PASSING_GRADE):
    """Return a report, including a helpful result for an empty class."""
    if not students:
        return "No student records.\n"
    total = 0
    passing_names = []
    for student in students:
        total += student["grade"]
        if student["grade"] >= passing_grade:
            passing_names.append(student["name"])
    average = total / len(students)
    names = ", ".join(passing_names) if passing_names else "None"
    return (
        f"Students: {len(students)}\n"
        f"Class average: {average:.2f}\n"
        f"Passing threshold (illustrative): {passing_grade}\n"
        f"Passing students: {len(passing_names)}\n"
        f"Names: {names}\n"
    )


def write_report(path, report):
    """Replace the generated report on every run."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        file.write(report)


def main():
    # Resolve the repository root from this file, even from another working folder.
    base = Path(__file__).resolve().parent.parent
    csv_path = base / "data" / "grades.csv"
    report_path = base / "outputs" / "grade_summary.txt"
    ensure_sample_data(csv_path)
    try:
        students = read_students(csv_path)
    except (OSError, ValueError) as error:
        raise SystemExit(f"Cannot read grades: {error}") from error
    report = summarize(students)
    write_report(report_path, report)
    print(report, end="")
    print(f"Saved: {report_path}")


if __name__ == "__main__":
    main()
