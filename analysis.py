"""
Student Performance Analysis
Author: Tahirə Hüseynova
Description: Generates student performance data, runs statistical analysis,
             and exports results to JSON for the dashboard.
"""

import json
import random
import statistics

random.seed(42)

# ── Sample Data ────────────────────────────────────────────────────────────────

STUDENTS = [
    "Aynur M.", "Kamran R.", "Leyla H.", "Tural A.", "Nigar S.",
    "Rashad K.", "Gunel B.", "Elvin C.", "Sevinc O.", "Farid N.",
    "Xumar T.", "Zulfiya E.", "Murad L.", "Aysel P.", "Samir Q.", "Nərmin V.",
]

SUBJECTS = ["Mathematics", "Informatics", "English", "Physics"]

MONTHS = ["Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr", "May"]

# Base scores per student (simulates real variation)
BASE_SCORES = [94, 78, 88, 65, 91, 55, 82, 73, 96, 60, 87, 70, 99, 62, 84, 76]
ATTENDANCE  = [97, 89, 93, 78, 96, 65, 91, 83, 98, 72, 88, 80, 99, 74, 92, 85]

# ── Helper Functions ───────────────────────────────────────────────────────────

def grade(score: float) -> str:
    if score >= 90: return "A"
    if score >= 75: return "B"
    if score >= 60: return "C"
    return "D"

def subject_score(base: int, subject: str) -> int:
    """Simulate per-subject variation from a student's base score."""
    offsets = {"Mathematics": 0, "Informatics": -3, "English": +2, "Physics": -5}
    noise = random.randint(-6, 6)
    return max(30, min(100, base + offsets[subject] + noise))

# ── Build Student Records ──────────────────────────────────────────────────────

students = []
for i, name in enumerate(STUDENTS):
    base = BASE_SCORES[i]
    scores = {subj: subject_score(base, subj) for subj in SUBJECTS}
    avg = round(statistics.mean(scores.values()), 1)
    students.append({
        "name":       name,
        "scores":     scores,
        "average":    avg,
        "grade":      grade(avg),
        "attendance": ATTENDANCE[i],
    })

# ── Monthly Trend (class average, improving over the year) ────────────────────

def trend(start: int, end: int, n: int) -> list[int]:
    return [round(start + (end - start) * i / (n - 1)) for i in range(n)]

monthly_trends = {
    "Mathematics": trend(68, 87, len(MONTHS)),
    "Informatics": trend(65, 84, len(MONTHS)),
    "English":     trend(70, 85, len(MONTHS)),
    "Physics":     trend(63, 82, len(MONTHS)),
}

# ── Statistical Summary ────────────────────────────────────────────────────────

all_averages = [s["average"] for s in students]

summary = {
    "total_students": len(students),
    "class_average":  round(statistics.mean(all_averages), 1),
    "median_score":   round(statistics.median(all_averages), 1),
    "std_deviation":  round(statistics.stdev(all_averages), 1),
    "pass_rate":      round(sum(1 for s in students if s["average"] >= 60) / len(students) * 100, 1),
    "grade_counts": {
        "A": sum(1 for s in students if s["grade"] == "A"),
        "B": sum(1 for s in students if s["grade"] == "B"),
        "C": sum(1 for s in students if s["grade"] == "C"),
        "D": sum(1 for s in students if s["grade"] == "D"),
    },
    "subject_averages": {
        subj: round(statistics.mean(s["scores"][subj] for s in students), 1)
        for subj in SUBJECTS
    },
}

# ── Export ─────────────────────────────────────────────────────────────────────

output = {
    "students":       students,
    "monthly_trends": monthly_trends,
    "months":         MONTHS,
    "subjects":       SUBJECTS,
    "summary":        summary,
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

# ── Print Report ───────────────────────────────────────────────────────────────

print("=" * 48)
print("  STUDENT PERFORMANCE REPORT — 2024/25")
print("=" * 48)
print(f"  Total students   : {summary['total_students']}")
print(f"  Class average    : {summary['class_average']}")
print(f"  Median score     : {summary['median_score']}")
print(f"  Std deviation    : {summary['std_deviation']}")
print(f"  Pass rate        : {summary['pass_rate']}%")
print()
print("  Grade distribution:")
for g, count in summary["grade_counts"].items():
    bar = "█" * count
    print(f"    {g}  {bar}  ({count})")
print()
print("  Subject averages:")
for subj, avg in summary["subject_averages"].items():
    print(f"    {subj:<15} {avg}")
print()
print("  Top 5 students:")
top5 = sorted(students, key=lambda s: s["average"], reverse=True)[:5]
for rank, s in enumerate(top5, 1):
    print(f"    {rank}. {s['name']:<14} {s['average']}  ({s['grade']})")
print("=" * 48)
print("  data.json exported successfully.")
print("=" * 48)
