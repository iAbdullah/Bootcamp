import csv
from pathlib import Path

def read_csv_rows(path: Path, delimiter: str = ",") -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"CSV not found: {path}")
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        rows = list(reader)
        if not rows:
            raise ValueError("CSV has no data rows")
        return rows