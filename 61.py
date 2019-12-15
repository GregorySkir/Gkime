import csv
def read_bechdel(file_path):
    n=0
    k=0
    a=0
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            n+=1
            k+=int(line[6])
        a=k/n
    return (n,a)

print(read_bechdel('movies-bechdel.csv'))
