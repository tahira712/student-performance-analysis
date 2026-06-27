# Student Performance Dashboard

An interactive data analytics dashboard built to analyse student academic performance across multiple subjects. This project demonstrates end-to-end data analysis skills — from raw data processing in Python to interactive visualisation in the browser.

## Live Demo
<img width="1901" height="862" alt="image" src="https://github.com/user-attachments/assets/458e1dc2-17f3-4874-86e8-c655d04269b6" />

Open `index.html` in any browser. No server required.

## Features

- **KPI summary cards** — total students, class average, pass rate, attendance
- **Bar chart** — average score per subject
- **Doughnut chart** — grade distribution (A / B / C / D)
- **Line chart** — monthly score trend across the academic year
- **Student records table** — sortable, filterable, with progress bars
- **Filters** — by subject, grade level, and sort order

## Project Structure

```
student-performance-dashboard/
├── analysis.py     # Python script: generates data, runs statistics, exports JSON
├── data.json       # Generated dataset (16 students, 4 subjects, 9 months)
├── index.html      # Interactive dashboard (HTML + Chart.js)
└── README.md
```

## Tech Stack

| Layer       | Technology              |
|-------------|-------------------------|
| Data analysis | Python 3 (statistics, json, random) |
| Visualisation | Chart.js 4.4            |
| Frontend    | HTML5, CSS3, Vanilla JS |

## How to Run

### 1. Generate the data (optional — `data.json` is already included)

```bash
python analysis.py
```

This prints a statistical report to the terminal and writes `data.json`.

### 2. Open the dashboard

Simply open `index.html` in your browser:

```bash
# macOS
open index.html

# Windows
start index.html

# Linux
xdg-open index.html
```

> The dashboard includes a built-in fallback dataset, so it works even without running `analysis.py` first.

## Sample Output (Python report)

```
================================================
  STUDENT PERFORMANCE REPORT — 2024/25
================================================
  Total students   : 16
  Class average    : 76.8
  Median score     : 78.0
  Std deviation    : 13.6
  Pass rate        : 87.5%

  Grade distribution:
    A  ███  (3)
    B  █████  (5)
    C  ██████  (6)
    D  ██  (2)

  Subject averages:
    Mathematics     79.1
    Informatics     73.6
    English         81.8
    Physics         72.9
================================================
```

## About

Built by **Tahirə Hüseynova** as a data analytics portfolio project.

- BSc Mathematics & Informatics — Azerbaijan State Pedagogical University
- Skills: Python, data analysis, statistical thinking, data visualisation
- Contact: tahireh961@gmail.com
