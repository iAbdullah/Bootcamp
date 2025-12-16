from __future__ import annotations
from csv import DictReader
from pathlib import Path

def read_csv_rows(path: str | Path) -> list[dict[str, str]]:
    # 1. Convert the path argument to a Path object for easier handling
    path = Path(path)
    
    # 2. Open the file, ensuring correct encoding and newline handling
    with path.open("r", encoding="utf-8", newline="") as f:
        # 3. Create a DictReader object
        reader = DictReader(f)
        
        # 4. Iterate over the reader and convert each row (OrderedDict) 
        #    to a standard dict, returning the full list.
        return [dict(row) for row in reader] 

# Example of how you would use this function (assuming a file named 'data.csv' exists)
# rows = read_csv_rows("data.csv")
# print(rows)