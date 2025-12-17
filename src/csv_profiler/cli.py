import json
import time
import typer
from pathlib import Path
from typing import Optional

# Importing functions from your other modules
from csv_profiler.io import read_csv_rows
from csv_profiler.profiling import profile_rows
from csv_profiler.render import render_markdown

# Initialize Typer app with English help text
app = typer.Typer(help="Professional CSV Profiling Tool")
@app.command()
def dummy():
    pass

@app.command()
def profile(
    input_path: Path = typer.Argument(..., help="Path to the source CSV file"),
    out_dir: Path = typer.Option(Path("outputs"), "--out-dir", "-o", help="Directory to save reports"),
    report_name: str = typer.Option("report", "--name", help="Base name for the output files"),
    delimiter: str = typer.Option(",", "--delimiter", "-d", help="CSV delimiter (e.g., ',' or ';')"),
):
    """
    Analyze a CSV file and generate professional JSON and Markdown reports.
    """
    try:
        # Start timing the execution (Requirement for Day 3)
        t0 = time.perf_counter_ns()
        
        # 1. Read the CSV data
        rows = read_csv_rows(input_path, delimiter=delimiter)
        
        # 2. Perform profiling analysis
        report = profile_rows(rows)
        
        # Calculate duration in milliseconds
        t1 = time.perf_counter_ns()
        duration_ms = (t1 - t0) / 1_000_000
        report["duration_ms"] = round(duration_ms, 2)

        # 3. Ensure output directory exists
        out_dir.mkdir(parents=True, exist_ok=True)

        # 4. Save JSON Report
        json_path = out_dir / f"{report_name}.json"
        json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
        
        # 5. Save Markdown Report (using render_markdown from render.py)
        md_text = render_markdown(report)
        md_path = out_dir / f"{report_name}.md"
        md_path.write_text(md_text, encoding="utf-8")

        # Success messages in Terminal
        typer.secho(f"✨ Success! Analysis completed in {duration_ms:.2f}ms", fg=typer.colors.GREEN, bold=True)
        typer.echo(f"📂 Reports saved in: {out_dir.absolute()}")

    except Exception as e:
        typer.secho(f"💥 Error: {e}", fg=typer.colors.RED, bold=True)
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()