from __future__ import annotations
import json
from pathlib import Path
from typing import dict, Any

def write_json(report: dict[str, Any], path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")

def write_markdown(report: dict[str, Any], path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True) 

    md_content = "# CSV Profiling Report\n\n"
    
    row_count = report.get('rows', 0)
    
    md_content += "## Overview\n"
    md_content += f"- Rows: **{row_count}**\n\n"
    
    md_content += "## Column Statistics\n\n"
    
    md_content += "| Column Name | Missing Count |\n"
    md_content += "| :--- | :---: |\n" 
    
    column_stats = report.get('column_stats', {})
    column_names = report.get('column_names', []) 

    for name in column_names:
        missing = column_stats.get(name, {}).get('missing', 0)
        md_content += f"| {name} | {missing} |\n"
        
    path.write_text(md_content, encoding="utf-8")