import os
from flask import Flask



def flatten_data(file):
    data = []
    keys = set()

    output_file = f"{os.path.splitext(file)[0]}_processed.txt"

    with open(file, "r") as file:
        for line in file:
            entries = line.strip().split("^^")
            row_dict = {}

            for entry in entries:
                if "=" in entry:
                    key, value = entry.split("=", 1) 
                    clean_value = value.replace("^", "").replace("=", "")
                    row_dict[key] = clean_value.strip()
                    keys.add(key)

            data.append(row_dict)

    # keys = sorted(keys)

    with open(output_file, "w") as out:
        out.write("|".join(keys) + "\n")
        for row in data:
            out.write("|".join(row.get(key, "") for key in keys) + "\n")

    print(f"Processed data saved to: {output_file}")


flatten_data("sample_input.txt")
