import streamlit as st

# Example result in the same shape as POST /v1/scan.
# Used until the Home page saves a real scan in st.session_state["last_result"].
EXAMPLE_RESULT = {
    "vulnerable": True,
    "cwe": "CWE-89",
    "cwe_family": "input_injection",
    "confidence": 0.91,
    "findings": [
        {
            "cwe": "CWE-89",
            "cwe_family": "input_injection",
            "confidence": 0.91,
            "language": "python",
            "start_line": 1,
            "end_line": 2,
            "taint_paths": [
                {
                    "source": "request.args",
                    "sink": "cursor.execute",
                    "sanitizer_present": False,
                    "steps": [
                        {"line": 1, "code": 'query = "SELECT ... " + request.args["id"]'},
                        {"line": 2, "code": "cursor.execute(query)"},
                    ],
                }
            ],
        }
    ],
}

st.title("Findings")

result = st.session_state.get("last_result")
if result is None:
    st.caption("Showing example data. Scan some code on the Home page to see real findings.")
    result = EXAMPLE_RESULT

if not result["findings"]:
    st.success("No findings: the model did not flag this code.")

for finding in result["findings"]:
    with st.container(border=True):
        st.subheader(finding.get("cwe_family", "unknown family"))
        st.write(f"Most likely CWE: {finding['cwe']}")
        st.write(f"Confidence: {finding['confidence']:.0%}")
        if finding["start_line"] is not None:
            st.write(f"Lines {finding['start_line']} to {finding['end_line']}")

        # Taint path: how unsafe input reaches a dangerous call. Only shown when present.
        for path in finding["taint_paths"]:
            st.markdown(f"**Data flow:** `{path['source']}` → `{path['sink']}`")
            if path["sanitizer_present"]:
                st.write("A sanitizer was found on this path.")
            steps = [f"line {step['line']}: {step['code']}" for step in path["steps"]]
            st.code("\n".join(steps))
