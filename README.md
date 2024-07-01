# deadline balancing

## port.py

Script to port changes from a change sheet into `balancing.csv` or `testing.csv`. Usage:

```bash
python port.py "changes/changes.csv" "testing.csv"
```

- Will update the date automatically.
- Matches rows by `name`, make sure those are included in the change sheet.
- Order of columns in the change sheet does not matter.
- If you include a column in the change sheet, it will overwrite the value in the target sheet. So be careful with empty columns.
