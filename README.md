# deadline balancing

attachment stats for deadline. game link: <https://www.roblox.com/games/3837841034>

## port.py

Script to port changes from a change sheet into `balancing.csv` or `testing.csv`. Usage:

```bash
python port.py (change sheet) (target sheet) [header row]  
python port.py "changes/changes.csv" "testing.csv" 2
```

- Updates the date in the target sheet automatically.
- Matches rows by `name` column, make sure those are included in the change sheet.
- Order of columns in the change sheet does not matter.
- Empty cells will overwrite existing data. Be careful.
- `[header row]` is the row # of the column headers in the change sheet. Useful for extra labels or dates above the headers. Optional, defaults to 1.

## diff.py

Script to compare two sheets and output a changelog. Usage:

```bash
python diff.py (old sheet) (new sheet)
python diff.py "balancing-old.csv" "balancing.csv"
```

- Outputs a changelog to `changelogs/version-changelog.md`.
- Matches rows by `name` column.
- Uses the `pretty_name` column for display in the changelog, falling back to `name`.
