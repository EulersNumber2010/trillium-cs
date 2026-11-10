from pathlib import Path
p = Path("./defect-detector")
files = p.rglob('*.py')
for f in files:
    print(f)