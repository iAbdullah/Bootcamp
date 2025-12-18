import streamlit as st
import csv
import json
from io import StringIO
from pathlib import Path
from csv_profiler.profiling import profile_rows
from csv_profiler.render import render_markdown

st.set_page_config(page_title="CSV Profiler", layout="wide")
st.title("CSV Profiler")

st.sidebar.header("Inputs")
uploaded = st.sidebar.file_uploader("Upload CSV file", type=["csv"])

if uploaded is not None:
    text = uploaded.getvalue().decode("utf-8-sig")
    rows = list(csv.DictReader(StringIO(text)))
    if st.button("Generate Report"):
        st.session_state["report"] = profile_rows(rows)

if "report" in st.session_state:
    report = st.session_state["report"]
    st.metric("Rows", report["n_rows"])
    st.metric("Columns", report["n_cols"])
    st.table(report["columns"])
    
    if st.button("Save to outputs/"):
        out_dir = Path("outputs")
        out_dir.mkdir(exist_ok=True)
        (out_dir / "report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
        st.success("Saved successfully!")
