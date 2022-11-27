import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, new_line="\n", delimiter=",") -> list[dict]:
    with open(filename) as file:
        headers = file.readline().replace(new_line, "").split(delimiter)
        list_of_values = []
    for line in file:
        list_of_values.append(line.replace(new_line, "").split(delimiter))
    list_ = []
    for f in list_of_values:
        dict_ = {}
        for i in range(len(headers)):
            dict_[headers[i]] = f[i]
        list_.append(dict_)
    return list_

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
