from pathlib import Path
import csv

def Unique_count(file_path):
    my_dict={}
    dir_path = Path.cwd()
    file_name = dir_path.joinpath(file_path+".csv")
    with open(file_name, encoding="utf8",newline="") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        count = 0
        
        for row in reader:
            if row[0] not in my_dict:
                my_dict[row[0]]= my_dict.get(row[0],[])
                count += 1
            else:
                my_dict[row[0]].append(row[0])
    return count

print(Unique_count("Yelp"))