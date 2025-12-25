C📊 CSV Profiler Tool
A comprehensive Python-based tool designed to analyze, profile, and summarize CSV data. This project was developed as part of the AI Professionals Bootcamp (SDAIA) to demonstrate core Python mastery, OOP principles, and modern application development.

🌟 Overview
The CSV Profiler allows users to quickly understand the structure and quality of their datasets. It identifies data types, calculates key statistics for numerical columns, and identifies missing data. The tool offers two interfaces: a powerful Command Line Interface (CLI) and an interactive Web GUI.

✨ Features
Smart Type Inference: Automatically detects if a column is numeric, text, or boolean.

Data Statistics: Calculates Min, Max, Mean, and Median for numerical data.

Missing Value Analysis: Reports the count and percentage of missing values per column.

Dual Interface:

CLI: Fast, terminal-based profiling using Typer.

Web GUI: User-friendly dashboard built with Streamlit.

Exportable Reports: Generates professional summaries in both JSON and Markdown formats.

🛠️ Tech Stack
Language: Python 3.12+

Environment Management: uv (Fast Python package installer)

CLI Framework: Typer

Web Framework: Streamlit

Data Handling: Native csv & json modules, pathlib for file system management.
