from pathlib import Path
from csv_profiler.io import read_csv_rows
from csv_profiler.profiler import basic_profile
from csv_profiler.render import write_json, write_markdown

CSV_PATH = Path("data/sample.csv")
JSON_OUTPUT_PATH = Path("outputs/report.json")
MARKDOWN_OUTPUT_PATH = Path("outputs/report.md")

def main() -> None:
    rows = read_csv_rows(CSV_PATH)
    report = basic_profile(rows)
    write_json(report, JSON_OUTPUT_PATH)
    write_markdown(report, MARKDOWN_OUTPUT_PATH)
    print("Wrote outputs/report.json and outputs/report.md")

if __name__ == "__main__":
    main()