from pathlib import Path
from csv_profiler.io import read_csv_rows
from csv_profiler.profiling import basic_profile
from csv_profiler.render import write_json, write_markdown

CSV_PATH = Path("data/sample.csv")
JSON_OUTPUT_PATH = Path("outputs/report.json")
MARKDOWN_OUTPUT_PATH = Path("outputs/report.md")

def run_profiler(file_path: Path):
    rows = read_csv_rows(file_path)
    report = basic_profile(rows)
    
    write_json(report, JSON_OUTPUT_PATH)
    
    write_markdown(report, MARKDOWN_OUTPUT_PATH, file_path.name)
    
    print(f"✅ Success! Report generated for: {file_path}")

if __name__ == "__main__":
    run_profiler(CSV_PATH)