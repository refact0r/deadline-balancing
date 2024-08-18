import csv
import sys
from typing import Dict, List, Tuple


def read_csv(file_path: str) -> Tuple[str, Dict[str, Dict[str, str]]]:
    data = {}
    with open(file_path, "r", newline="", encoding="utf-8-sig") as f:
        version = f.readline().split(",")[0]
        reader = csv.DictReader(f)
        for row in reader:
            if row["name"]:
                data[row["name"]] = row
    return version, data


def format_header(header: str) -> str:
    return " ".join(word.capitalize() for word in header.split("_"))


def compare_rows(
    row1: Dict[str, str], row2: Dict[str, str], compare_cols: List[str]
) -> List[str]:
    changes = []
    for key in compare_cols:
        if not row1:
            if row2.get(key):
                changes.append(f"{format_header(key)}: **{row2.get(key, '0')}**")
        elif row1.get(key, "0") != row2.get(key, "0"):
            changes.append(
                f"{format_header(key)}: **{row1.get(key, '0')}** -> **{row2.get(key, '0')}**"
            )
    return changes


def main(file1: str, file2: str):
    _, data1 = read_csv(file1)
    version, data2 = read_csv(file2)

    compare_cols = list(next(iter(data1.values())).keys())[4:]

    new = []
    changes = []
    for name, row2 in data2.items():
        row_changes = []
        if name in data1:
            row_changes = compare_rows(data1[name], row2, compare_cols)
            if len(row_changes) > 0:
                pretty_name = row2.get("pretty_name") or row2["name"]
                changes.append(
                    f"### {pretty_name}\n\n" + " \\\n".join(row_changes) + "\n"
                )
        else:
            row_changes = compare_rows({}, row2, compare_cols)
            if len(row_changes) > 0:
                pretty_name = row2.get("pretty_name") or row2["name"]
                new.append(f"### {pretty_name}\n\n" + " \\\n".join(row_changes) + "\n")

    output_file = "changelogs/" + version.replace(".", "-") + ".md"
    with open(output_file, "w", encoding="utf-8-sig") as f:
        f.write(f"# {version} Balancing Changes\n\n")
        f.write(f"New attachments: {len(new)}\n\n")
        f.write(f"Attachments changed: {len(changes)}\n\n")
        f.write(f"## New Attachments\n\n")
        f.write("\n".join(new))
        f.write(f"## Changed Attachments\n\n")
        f.write("\n".join(changes))

    print(f"Output written to {output_file}")


main(sys.argv[1], sys.argv[2])
