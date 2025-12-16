from typing import list, dict

def basic_profile(rows: list[dict[str, str]]) -> dict:
    """
    Compute row count, column names, and missing values per column.
    Missing is defined as: empty string after stripping whitespace.
    """

    # 1. فحص الصفوف الفارغة (Row Count and Empty Check)
    row_count = len(rows)

    if not rows:
        return {"rows": 0, "columns": {}, "notes": ["Empty dataset"]}

    columns = list(rows[0].keys())
    
    missing = {c: 0 for c in columns}
    non_empty = {c: 0 for c in columns}

    for row in rows:
        for c in columns:
            v = (row.get(c) or "").strip()
            
            if v == "":
                missing[c] += 1
            else:
                non_empty[c] += 1
                
    col_stats = {
        c: {
            "missing": missing[c],
            "non_empty": non_empty[c]
        } for c in columns
    }
    
    return {
        "rows": row_count,
        "column_names": columns,
        "column_stats": col_stats,
        "notes": []
    }