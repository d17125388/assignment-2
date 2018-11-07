
def create_dict(myfile):
    try:
        my_dict = {}
        file = open(myfile, 'r')

        for line in file:
            line = line.split()
            if line[2] in my_dict:
                my_dict[line[2]] += 1
            else:
                my_dict[line[2]] = 1

        file.close()
        my_dict.pop('YearsCodingProf')
        my_dict.pop('NA')

        return my_dict

    except IOError:
        print('That file does not exist')

print(create_dict('insert file name here'))


