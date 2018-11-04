import csv


try:
    with open('csv.txt', newline='', encoding="ISO-8859-1") as file1:
        file2 = open('file2.txt', 'w')
        reader = csv.reader(file1)
        
        for row in reader:
            # print(row[0],',',row[11],file=file2)
            # Prevents Python from adding unnecessary spaces
            print(row[0]+','+row[11],file=file2)

    file1.close()
    file2.close()

except IOError:
    print('That file does not exist')
