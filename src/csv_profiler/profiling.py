from typing import List, Dict, Any

MISSING = {"", "na", "n/a", "null", "none", "nan"}

def is_missing(value: str | None) -> bool:
    if value is None:
        return True
    return value.strip().casefold() in MISSING

def try_float(value: str) -> float | None:
    try:
        return float(value)
    except ValueError:
        return None

def infer_type(values: List[str]) -> str:
    usable = [v for v in values if not is_missing(v)]
    if not usable:
        return "text"
    for v in usable:
        if try_float(v) is None:
            return "text"
    return "number"

def profile_rows(rows: List[Dict[str, str]]) -> Dict[str, Any]:
    """هذه هي الدالة التي يبحث عنها الـ CLI"""
    if not rows:
        return {"n_rows": 0, "n_cols": 0, "columns": []}
        
    columns = list(rows[0].keys())
    col_profiles = []
    
    for col in columns:
        values = [row.get(col, "") for row in rows]
        usable = [v for v in values if not is_missing(v)]
        missing_count = len(values) - len(usable)
        inferred = infer_type(values)
        
        profile = {
            "name": col,
            "type": inferred,
            "missing": missing_count,
            "missing_pct": (missing_count / len(rows)) * 100 if rows else 0,
            "unique": len(set(usable))
        }
        
        if inferred == "number":
            nums = [try_float(v) for v in usable if try_float(v) is not None]
            if nums:
                profile.update({
                    "min": min(nums),
                    "max": max(nums),
                    "mean": sum(nums) / len(nums)
                })
        
        col_profiles.append(profile)
        
    return {
        "n_rows": len(rows),
        "n_cols": len(columns),
        "columns": col_profiles
    }