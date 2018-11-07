import csv


def csv_to_dict(myfile):

    try:
        with open('file2.txt', newline='', encoding="ISO-8859-1") as file1:
            reader = csv.reader(file1)
            my_dict = {}

            for row in reader:
                if (row[1] in my_dict):
                    my_dict[row[1]] += 1
                else:
                    my_dict[row[1]]  = 1

            file1.close()
            my_dict.pop('YearsCodingProf')
            my_dict.pop('NA')
            return my_dict

    except IOError:
        print('That file does not exist')

print(csv_to_dict('insert file name here'))



