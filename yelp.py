import csv
def calculate_yelp_rewiews(file_path):
    #Part A
    ub = {}#unique business(Q1)
    arpb = {}#avarage review per business(Q2)

    alr = 0#avarage length review(Q3)
    cumlength=0#cumulative length of all text
    qr=0#quantity of rewiews

    ur=set ()#unique reviews(Q4)

    rpr={}#reviews per reviewer(Q5)
    cumR=0#cumulative rewiews
    qp=0#quantity of unique people that rewiewed
    ansQ5=0#answer to the question 5
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            uniqueB = line["business_id"]
            lengthRewiew=len(line["text"])
            cumlength+=lengthRewiew
            qr+=1

            ub.setdefault(uniqueB, 0)
            ub[uniqueB]+=1

            arpb.setdefault(uniqueB, 0)
            
            ur.add(line["text"])

            uniqueR=line["user_id"]
            rpr.setdefault(uniqueR, 0)
            rpr[uniqueR]=line["user_reviews_count"]

        for uniqueB in ub.keys():
            average=int(line["business_reviews_count"])/int(ub[uniqueB])
            arpb[uniqueB] = round(average, 2)
        for uniqueR in rpr.keys():
            cumR+=int(rpr[uniqueR])
            qp+=1
        alr=cumlength/qr
        ansQ5=cumR/qp
    return ub, arpb, alr, len(ur), ansQ5

print(calculate_yelp_rewiews('Yelp.csv'))
