from datetime import datetime
from typing import Dict, Any

def render_markdown(report: Dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append(f"# 📊 CSV Profiling Report\n")
    lines.append(f"Generated: {datetime.now().isoformat(timespec='seconds')}\n")
    
    # قسم الملخص (Summary)
    lines.append("## 📈 Summary\n")
    lines.append(f"- Rows: **{report['n_rows']}**")
    lines.append(f"- Columns: **{report['n_cols']}**")
    if "timing_ms" in report:
        lines.append(f"- Execution Time: **{report['timing_ms']:.2f}ms**")
    lines.append("\n")
    
    # جدول الأعمدة (Columns Table)
    lines.append("## 📋 Columns Overview\n")
    lines.append("| Name | Type | Missing | Missing % | Unique |")
    lines.append("|:--- |:--- |:---:|:---:|:---:|")
    
    for c in report["columns"]:
        m_pct = c.get('missing_pct', 0)
        lines.append(f"| `{c['name']}` | {c['type']} | {c['missing']} | {m_pct:.1f}% | {c['unique']} |")
    
    return "\n".join(lines)