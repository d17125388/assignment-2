import csv

csv_path = 'csv/cleansed.txt'

def get_count():
    data_dict = {}
    try:
        with open(csv_path, newline='', encoding="ISO-8859-1") as csv_file:
            reader = csv.reader(csv_file)

            # Skip first line (header)
            next(reader)

            for row in reader:
                if row[1] == "NA":
                    continue
                if row[1] not in data_dict:
                    data_dict[row[1]] = 1
                else:
                    data_dict[row[1]] += 1

        csv_file.close()

        return sort_dict(data_dict)

    except IOError:
        print("Couldn't find file at: " + csv_path)


# Functions to sort the keys of the dictionary
def sort_dict(dict):
    sorted_dict = {}
    for key in sorted(dict, key=sort_key):
        sorted_dict[key] = dict[key]

    return sorted_dict

def sort_key(x):
    # Needs to check if it's a one digit or two digit number, converts to int
    try:
        return int(x[0:2])
    except:
        try:
            return int(x[0:1])
        except:
            return x
