# SHIELD taint spike (W1-P2-03): Python results (FINISHED)

> Status: **Python part complete.** C/C++ is in `taint_spike_c_plan.md`.
> This file is written so it can be pasted into `docs/taint_spike.md` as the Python section.
> Labels: **OBSERVED** = printed by Joern in our session. **INFERENCE** = my reading of observed output, not tested directly. **UNTESTED** = no evidence either way.

---

## 1. What the spike had to answer

1. Can Joern follow a source to sink flow inside one function? **Yes.**
2. Does it follow flows across functions? **Yes through calls (to a configurable depth), no through shared object state.**
3. What does it miss or over-report, and why? See section 6.
4. Which sources, sinks and sanitizers go into the YAML? See section 4 and section 8.

## 2. Environment

| Item | Value |
|---|---|
| Joern | 4.0.647 (image `shield-joern`, Dockerfile in `docker/joern/`) |
| Host | Windows, PowerShell, Docker Desktop |
| Container start | `docker run --rm -it -v "${PWD}\tests\fixtures\taint:/workspace/sample" shield-joern joern` |
| Python import | `importCode.python("sample/python")` (**not** `importCode.pythonsrc`, which does not exist in this shell; `joern-parse --language pythonsrc` is a different interface and is valid) |
| Default overlays | applied automatically on import; REACHING_DEF edges present |
| Engine defaults | `EngineConfig(maxCallDepth = 4, initialTable = None, shareCacheBetweenTasks = true, maxArgsToAllow = 1000, maxOutputArgsExpansion = 1000)` |

## 3. Shell pitfalls (these cost us several rounds)

1. **A multi-line `def` with `++` at the line ends fails** (`unindent expected, but eof found`). Put every definition on ONE line.
2. Path elements from `reachableByFlows` are typed `AstNode`. `.label`, `.code`, `.lineNumber` and `.astParent` work. `.method` does **not** compile: pattern-match to `CfgNode` first (`import io.shiftleft.codepropertygraph.generated.nodes.CfgNode`) to get `c.method.name` and `c.method.filename`.
3. `.p` output is unreliable for building steps: the `file` column is empty and identifier rows show the whole statement. Build steps from `(label, code, lineNumber)` ourselves.
4. Some `code` strings are multi-line (py06c, py09). Use `.code.split("\n").head`.
5. Always print `src.size` and `snk.size` BEFORE reading flows. An empty result means nothing until both endpoints are known to match.
6. Restart the container after adding fixtures; the CPG is built at import time.
7. Give every handler a unique name. Housekeeping: py01 and py02 both still define `handler`; identify them by `c.method.filename`, or rename them.

## 4. Final Python source and sink definitions

```scala
import io.shiftleft.codepropertygraph.generated.nodes.CfgNode
def src: Iterator[CfgNode] = cpg.call.code("request\\.args\\[.*|request\\.args\\.get\\(.*|request\\.form\\[.*|request\\.get_json\\(.*|input\\(.*|sys\\.argv\\[.*")
def snk: Iterator[CfgNode] = cpg.call.name("execute").argument(1) ++ cpg.call.name("system").code("os\\.system.*").argument(1) ++ cpg.call.name("run").code("subprocess\\.run.*").argument(1) ++ cpg.call.name("open").argument(1) ++ cpg.call.name("loads").code("pickle\\.loads.*").argument(1) ++ cpg.call.name("eval").argument(1)
val flows = snk.reachableByFlows(src).l
```

Rules learned:

- **A source is the node that PRODUCES the value** (`request.args["id"]`), not a sub-expression. With the field access `request.args` alone as the source, the flow query returned nothing (OBSERVED), although that node exists. Why: unknown. Do not guess in the report.
- **A sink is name + code prefix + argument index.** `db.cursor().execute(q)` is lowered so the receiver is argument 0 (`tmp0`) and `q` is argument 1. Selecting `.argument` without an index gave a second, duplicate flow ending on the receiver. Module-qualified calls (`os.system`, `subprocess.run`, `pickle.loads`) also have the module at index 0; bare calls (`open`, `eval`) do not. The payload is argument 1 in all five (OBSERVED).
- Name alone is not enough for some sinks: our own `run(cur, q)` helper in py04 would match a bare `name("run")`. Hence `code("subprocess\\.run.*")`.
- **Keyword arguments get index -1** (`shell = True` printed as `(-1, "True")`). A tainted value passed by keyword (`subprocess.run(args=x)`) would be missed by `argument(1)`. UNTESTED beyond the printed index.
- The sink receiver type is unknown: `execute` has `methodFullName = <unknownFullName>`, `typeFullName = ANY`, `DYNAMIC_DISPATCH`. Sinks can only be matched by name; any unrelated `.execute(...)` will match.

## 5. Fixture results

Folder: `tests/fixtures/taint/python/`. Each file has `# EXPECT:` written before running. Ground truth is what a human reading the code concludes.

Totals: **33 sources, 33 sinks, 26 flows** at the default depth. The 7 sinks without a flow are py02, py05, py10, py13 (all correct) and py11, py12b, py12e (known misses). With `maxCallDepth = 8`, py12b and py12e were recovered and py11 stayed missing.

| ID | Shape | Ground truth | Joern | Verdict |
|---|---|---|---|---|
| py01 | direct, `+` concatenation | flow | flow | ok |
| py02 | source read, constant reaches sink | no flow | no flow | ok (negative control) |
| py03 | defined helper returns tainted value | flow | flow | ok; path enters `wrap` |
| py04 | sink inside callee (argument to parameter) | flow | flow | ok; sink method is `run` |
| py05 | tainted value overwritten before sink | no flow | no flow | ok (negative control) |
| py06a/b/c | f-string / `%` / `.format` | flow | flow x3 | ok |
| py07 | dict literal, read the same key | flow | flow | ok (my "missed" hypothesis was wrong) |
| py07b | dict, read the SAFE key | no flow | **flow** | false positive: not key-sensitive |
| py08 | helper in another file via import | flow | flow | ok; path enters `build` body (resolved) |
| py09 | `request.args.get("id")` source | flow | flow | ok |
| py10 | tainted object is the RECEIVER, constant argument | no flow | no flow | ok (negative control) |
| py11 | `self.uid` written in one method, read in another | flow | **no flow** | miss; not fixed by depth 8 |
| py11b | same, write and read in one method | flow | flow | ok; isolates the cause of py11 |
| py12a/c/d | helper chains: 2, 3, 4 functions entered | flow | flow | ok |
| py12b/e | chains: 6 and 5 functions entered | flow | no flow at depth 4, flow at depth 8 | depth limit |
| py13 | parameterized query, taint in argument 2 | no flow | no flow | correct (by sink definition) |
| py14 | `int()` cast before use | not exploitable | flow | expected false positive; `int(...)` is visible in the path |
| py15a | `self.build(...)` instance method | flow | flow | path enters `build` (resolved) |
| py15b | `r = Repo(); r.build(...)` | flow | flow | path enters `build` (resolved) |
| py16a-e | `os.system`, `subprocess.run`, `open`, `pickle.loads`, `eval` | flow | flow x5 | ok |
| py17a-d | `input()`, `sys.argv[1]`, `request.form[...]`, `request.get_json()` | flow | flow x4 | ok |

Prediction record: py15a and py15b were predicted to possibly resolve differently; **wrong**, both enter the callee body (`... return ... -> RET -> self.build(...)` and `-> r.build(...)`).

## 6. Findings

### Works (OBSERVED)

- Intra-function flows through assignment, `+`, f-string, `%`, `.format`, container literal, and attribute access within one method.
- Cross-function flows through calls: argument to parameter (py04), return value back (py03), chains of up to 4 functions entered (py12a/c/d), cross-file import inside a single CPG (py08), instance-method calls via `self` and via an object (py15).
- Four negative controls gave no flow: constant to sink (py02), overwrite (py05), tainted receiver with constant argument (py10), parameterized query (py13).
- Patterns for CWE-89 (`execute`), CWE-78 (`os.system`, `subprocess.run`), CWE-22 (`open`), CWE-502 (`pickle.loads`) and CWE-95 (`eval`) all match and flow.
- **The sink call can be recovered from every flow.** For all 26 flows, `f.elements.last.astParent` is a `Call`, giving the sink's name and code (e.g. `("execute", "cur.execute(q)")`, `("system", "os.system(request.args[\"x\"])")`). Caveat: the fixtures use `cur.execute(...)` with a simple receiver. The chained-receiver shape `db.cursor().execute(q)`, where the receiver is lowered to `tmp0`, is not covered by this check (see 9).

### Limits

1. **Call depth is a configured limit.** `maxCallDepth = 4` gives flows through chains entering 2-4 functions and none through 5-6. Setting 8 with `EngineContext(config = EngineConfig(maxCallDepth = 8))` and `reachableByFlows(src)(using deepCtx)` recovered both. The plan's k=2 (W4-P2-01) is well inside the default. (OBSERVED)
2. **State shared across methods is invisible** (py11): no call connects the writer and the reader, and depth does not help. (OBSERVED)
3. **Unresolved calls are pass-throughs** (`escape(s)` in `calls.py`, which is never defined, sits inside a flow path). So "a flow exists" never means "unsanitized". `sanitizer_present` must be computed by us from the path (section 7). (OBSERVED)
4. **Not key-sensitive for containers** (py07b false positive). INFERENCE: the dict object `tmp0` is tainted as a whole.
5. **Joern cannot know that `int()` sanitizes** (py14): the flow is reported, and `int(request.args["id"])` appears as a path element, so a sanitizer-name scan can catch it. (OBSERVED)
6. **Sinks match by name only** (receiver type unknown, section 4). (OBSERVED)
7. **Keyword arguments are not positional** (index -1), so sinks defined as `argument(1)` miss keyword-passed taint. UNTESTED beyond the printed index.

### Lowering artifacts seen in paths

- Temporaries: `tmp0`, `tmp0 = {}`, `tmp0 = request.args` appear as path elements (py06c, py07, py09).
- A synthetic method `<metaClassAdapter>` per class (e.g. `handler_py11b<metaClassAdapter>`); it must not be counted as a real function in `graph_schema.md`.
- Consecutive duplicate elements (`q -> q`, `uid -> uid`).
- py16 paths have ONE element: the sink argument node **is** the source node. Because we select `argument(1)`, every path ends at the argument, which is why the sink call is recovered through `astParent`.

### Not tested (do not claim in the report)

Callbacks, decorators, framework entry points (Flask routes), cross-file flows when files are scanned separately, scale and time (fixtures are tiny; Week 2 measures cost), keyword-argument sinks, the `maxArgsToAllow` and `maxOutputArgsExpansion` caps, `*args`/`**kwargs`, generators, `async`, the chained-receiver sink shape under `astParent`.

### Bottom line

Joern's Python taint is usable for D13 as a **feature generator** (a path exists, its length, a sanitizer-like call in the path, the source and sink kinds). It is not usable as a finding by itself: it over-reports through dicts and unknown sanitizers, and under-reports through object state.

## 7. Mapping a Joern flow to `TaintPath` (`shield_core/interface.py`)

| `TaintPath` field | Source in the Joern flow |
|---|---|
| `source` | `code` of the first element (first line only) |
| `sink` | `name` and first line of `code` of `f.elements.last.astParent` (a `Call`, OBSERVED on 26/26 flows) |
| `steps` | one `TaintStep(file, line, code)` per element: file = `method.filename` (needs the `CfgNode` cast), line = `lineNumber`, code = first line of `code`; drop `tmpN` temporaries; collapse consecutive duplicates |
| `sanitizer_present` | true if any CALL element's name matches a sanitizer regex from the YAML. Observed examples: `escape(s)` (undefined helper), `int(...)` |

## 8. Design decisions this implies (log in plan Section 2 and Section 15)

1. **YAML source/sink format.** Current `LanguageSpec` has `sources: tuple[str]` and `sinks: tuple[str]`. We need structured entries. Proposal (NOT yet agreed): a sink is `{name: regex, code: regex (optional), arg: int}`; a source is `{kind: call | argument | parameter, name or code: regex, arg: int (optional)}`. Python only needs `call`. The C batch decides whether `argument` and `parameter` are needed.
2. **Add `sanitizers`** (list of call-name regexes) to the registry. `registry._parse_spec` rejects unknown keys and `_REQUIRED_KEYS` must change, so `tests/test_registry.py` needs updating too. The registry belongs to P4. `graph_schema.md` already defines the `is_sanitizer` node flag.
3. **Draft `python.yaml` content** (proposal; illustrative syntax until decision 1 is agreed):

```yaml
sources:
  - {kind: call, code: 'request\.args\[.*'}
  - {kind: call, code: 'request\.args\.get\(.*'}
  - {kind: call, code: 'request\.form\[.*'}
  - {kind: call, code: 'request\.get_json\(.*'}
  - {kind: call, code: 'input\(.*'}
  - {kind: call, code: 'sys\.argv\[.*'}
sinks:
  - {name: execute, arg: 1}                                  # CWE-89
  - {name: system, code: 'os\.system.*', arg: 1}             # CWE-78
  - {name: run, code: 'subprocess\.run.*', arg: 1}           # CWE-78
  - {name: open, arg: 1}                                     # CWE-22
  - {name: loads, code: 'pickle\.loads.*', arg: 1}           # CWE-502
  - {name: eval, arg: 1}                                     # CWE-95
sanitizers: []   # observed as path elements: int(...), a helper named escape(...)
                 # candidates NOT yet tested: html.escape, shlex.quote, os.path.basename, os.path.realpath
```

4. **Interface naming inconsistency** in `shield_core/interface.py`: `Finding.taint_paths` (snake_case) but `Result.taintPaths` (camelCase). Raise it before the Friday freeze (W1-P4-01).

## 9. Python items still open (all small)

- [ ] **Chained-receiver sink check** (closes the caveat in section 6). On `calls.py`, where the sink is `db.cursor().execute(q)`:
  ```powershell
  docker run --rm -it -v "${PWD}\tests\fixtures\joern:/workspace/sample" shield-joern joern
  ```
  ```scala
  import io.shiftleft.codepropertygraph.generated.nodes.{CfgNode, Call}
  importCode.python("sample/calls.py")
  def s1 = cpg.call.code("request\\.args\\[.*")
  def k1 = cpg.call.name("execute").argument(1)
  k1.reachableByFlows(s1).map(f => f.elements.last.astParent match { case c: Call => (c.name, c.code.split("\n").head); case o => (o.label, o.code.split("\n").head) }).l
  ```
  Confirm the result is `("execute", "db.cursor().execute(q)")` and not the `tmp0` assignment. The 26/26 result suggests it will be the call, but this shape is untested.
- [ ] Add `tests/fixtures/taint` to the ruff exclude in `pyproject.toml` (fixtures use undefined names on purpose).
- [ ] Rename the two `handler` functions in py01/py02, or keep identifying them by file name.
- [ ] Optional extra fixtures: keyword-argument sink, callback, Flask-route entry point, `*args`.
- [ ] Fill `languages/python.yaml` once decisions 1 and 2 in section 8 are made.

## 10. Reproduction commands

```powershell
docker run --rm -it -v "${PWD}\tests\fixtures\taint:/workspace/sample" shield-joern joern
```
```scala
import io.shiftleft.codepropertygraph.generated.nodes.{CfgNode, Call}
importCode.python("sample/python")
// paste the two one-line defs from section 4, then:
src.size                         // expect 33
snk.size                         // expect 33
val flows = snk.reachableByFlows(src).l
flows.size                       // expect 26
flows.map(f => f.elements.last match { case c: CfgNode => c.method.name; case _ => "?" }).sorted.l
flows.map(f => f.elements.last.astParent match { case c: Call => (c.name, c.code.split("\n").head); case o => (o.label, o.code.split("\n").head) }).l
// depth experiment
import io.joern.dataflowengineoss.queryengine.{EngineConfig, EngineContext}
val deepCtx = EngineContext(config = EngineConfig(maxCallDepth = 8))
snk.reachableByFlows(src)(using deepCtx).size
```
