import csv
def calculate_mean_year(file_path):
    mpy = {}
    arpy = {}
    rpy = {}
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            year = line["year"]
            mpy.setdefault(year, 0)
            mpy[year]+=1
            if line["domgross"].isdigit():
                domgross = int(line["domgross"])
            else:
                domgross=0
            if line["intgross"].isdigit():
                intgross = int(line["intgross"]) 
            else:
                intgross=0
            revenue = domgross+intgross
            rpy.setdefault(year, 0)
            rpy[year]+=revenue
        for year in mpy.keys():
            average = rpy[year]/mpy[year]
            arpy[year] = round(average, 2)
    return mpy, arpy

def write_revenues_to_file(file_path, movies_counts, movies_revenues):
    with open(file_path, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Year","Number of movies","Average revenues"])
        for key in sorted(movies_counts.keys()):
            writer.writerow([key,movies_counts[key],movies_revenues[key]])
        return()

movies_counts, movies_revenues = calculate_mean_year('movies-bechdel.csv')
write_revenues_to_file('new_file.csv', movies_counts, movies_revenues)