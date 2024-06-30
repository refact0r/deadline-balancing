import csv


def update_csv(changes, original):
    with open(changes, "r") as f:
        reader = csv.reader(f)
        headers = next(reader)
        name_index = headers.index("name")
        data = {row[name_index]: row[name_index:] for row in reader}

    with open(original, "r") as f:
        reader = csv.reader(f)
        lines = list(reader)

    for i in range(2, len(lines)):
        name = lines[i][name_index]
        if name in data:
            lines[i] = lines[i][:name_index] + data[name]

    with open(original, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(lines)


update_csv("m4 stocks - port.csv", "testing.csv")
