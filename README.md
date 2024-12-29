# deadline balancing

attachment stats for deadline. game link: <https://www.roblox.com/games/3837841034>

## changelogs

- [0.24.0](changelogs/0-24-0.md)
- [0.23.3](changelogs/0-23-3.md)
- [0.23.2](changelogs/0-23-2.md)
- [0.23.1](changelogs/0-23-1.md)
- [0.23.0](changelogs/0-23-0.md)

## guide

### balancing.csv

Master balancing sheet. Should always be up to date with the latest changes.

### testing.csv

Testing sheet. Gets imported into dev branch when updated.

### port.py

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

### diff.py

Script to compare two sheets and output a changelog. Usage:

```bash
python diff.py (old sheet) (new sheet)
python diff.py "archive/0-22-12.csv" "balancing.csv"
```

- Outputs a changelog to `changelogs/version-changelog.md`.
- Matches rows by `name` column.
- Uses the `pretty_name` column for display in the changelog, falling back to `name`.
