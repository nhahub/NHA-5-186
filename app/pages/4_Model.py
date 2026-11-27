import os
from pathlib import Path

import pandas as pd
import requests
import streamlit as st

DOCS = Path(__file__).resolve().parents[2] / "docs" / "modeling"
FAMILY_FILE = DOCS / "v1_per_family.md"
CWE_FILE = DOCS / "v1_per_cwe.md"
API_URL = os.environ.get("SHIELD_API_URL", "http://127.0.0.1:8000")

TEXT_COLUMNS = ["family", "CWE", "reliable"]
SCORE_FORMAT = {
    name: st.column_config.NumberColumn(format="%.3f") for name in ["precision", "recall", "f1"]
}


def read_tables(path):
    """Read a report file and return one table per language."""
    rows = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            language = line[3:]
            rows[language] = []
        elif line.startswith("|") and "---" not in line:
            rows[language].append([cell.strip() for cell in line.strip("|").split("|")])

    tables = {}
    for language, lines in rows.items():
        table = pd.DataFrame(lines[1:], columns=lines[0])
        for column in table.columns:
            if column not in TEXT_COLUMNS:
                table[column] = pd.to_numeric(table[column], errors="coerce")
        tables[language] = table
    return tables


def show_tables(path):
    for language, table in read_tables(path).items():
        st.markdown(f"**{language}**")
        st.dataframe(table, hide_index=True, column_config=SCORE_FORMAT)


st.title("Model")

try:
    model = requests.get(f"{API_URL}/v1/model", timeout=5).json()
    st.metric("Model in use", model["default"])
except requests.RequestException:
    st.warning("Cannot reach the API, so the model version is unknown.")

run_name = FAMILY_FILE.read_text(encoding="utf-8").split("`")[1]
st.info(f"Results from run `{run_name}` on the test split. These numbers are not final yet.")

st.subheader("Results by CWE family")
show_tables(FAMILY_FILE)

with st.expander("Results by exact CWE"):
    st.caption(
        "Exact-CWE scores are lower because every function in a fix commit gets the commit's "
        "CWE, and many CWEs have only a few commits. Do not trust rows with reliable = no."
    )
    show_tables(CWE_FILE)
