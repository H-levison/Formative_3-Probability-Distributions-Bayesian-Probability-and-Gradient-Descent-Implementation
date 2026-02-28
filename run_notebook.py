"""Run all code cells from bivariate_normal.ipynb."""
import json
import sys

# Use non-interactive backend for matplotlib so plots don't block
import matplotlib
matplotlib.use('Agg')

with open("bivariate_normal.ipynb", "r", encoding="utf-8") as f:
    nb = json.load(f)

globals_dict = {}
for cell in nb.get("cells", []):
    if cell.get("cell_type") != "code":
        continue
    source = "".join(cell.get("source", []))
    if not source.strip():
        continue
    try:
        exec(compile(source, "<cell>", "exec"), globals_dict)
    except Exception as e:
        print(f"Error in cell:\n{source[:200]}...\n{e}", file=sys.stderr)
        sys.exit(1)

print("\nNotebook ran successfully.")
