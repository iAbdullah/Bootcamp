import streamlit as st
import csv
import json
from io import StringIO
from pathlib import Path
from csv_profiler.profiling import profile_rows
from csv_profiler.render import render_markdown

st.set_page_config(page_title="CSV Profiler", layout="wide")

st.title("CSV Profiler")
st.caption("Week 01 - Day 04 - Streamlit GUI")

st.sidebar.header("Inputs")
uploaded = st.sidebar.file_uploader("Upload a CSV", type=["csv"])

if uploaded is not None:
    text = uploaded.getvalue().decode("utf-8-sig")
    rows = list(csv.DictReader(StringIO(text)))
    
    n_rows = len(rows)
    n_cols = len(rows[0]) if n_rows > 0 else 0
    
    c1, c2 = st.columns(2)
    c1.metric("Rows", n_rows)
    c2.metric("Columns", n_cols)

    st.subheader("Data Preview")
    st.write(rows[:5])

    if st.button("Generate Report"):
        st.session_state["report"] = profile_rows(rows)

    if "report" in st.session_state:
        report = st.session_state["report"]
        
        st.divider()
        st.subheader("Analysis Report")
        st.dataframe(report["columns"])
        
        with st.expander("Markdown Preview"):
            st.markdown(render_markdown(report))
            
        st.sidebar.divider()
        st.sidebar.header("Export Options")
        
        md_text = render_markdown(report)
        st.sidebar.download_button(
            label="Download Markdown Report",
            data=md_text,
            file_name="report.md",
            mime="text/markdown"
        )
        
        json_text = json.dumps(report, indent=2, ensure_ascii=False)
        st.sidebar.download_button(
            label="Download JSON Data",
            data=json_text,
            file_name="report.json",
            mime="application/json"
        )

        if st.sidebar.button("Save to outputs/"):
            out_dir = Path("outputs")
            out_dir.mkdir(parents=True, exist_ok=True)
            (out_dir / "report.md").write_text(md_text, encoding="utf-8")
            (out_dir / "report.json").write_text(json_text, encoding="utf-8")
            st.sidebar.success("Saved successfully")
else:
    st.info("Please upload a CSV file to begin")