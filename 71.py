import csv
from pathlib import Path

def calculate_mean_year(file_path=Path.cwd().joinpath('movies-bechdel.csv')):
    
    movies_revenues = {}
    
    with open(file_path) as csvfile :
        reader = csv.DictReader(csvfile)

        for line in reader:
            if all([line["domgross"]!="#N/A", line["intgross"]!="#N/A"]):
                if ((line["year"]),(line["binary"])) not in movies_revenues:
                    movies_revenues[((line["year"]),(line["binary"]))]= []
                movies_revenues[((line["year"]),(line["binary"]))].append(float(line["domgross"])+float(line["intgross"]))
        
        for ((year),(test_result)) in movies_revenues.keys():
            movies_revenues[((year),(test_result))] = sum(movies_revenues[((year),(test_result))])
        return movies_revenues

print(calculate_mean_year())