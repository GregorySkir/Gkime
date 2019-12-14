#Question 1, I didn't understand the question till the end, but I counted this shit in my way. You can try in in vsCode and see which answers you will get
import csv
def bachdel_test(file_path):
    pmpy = {}#PASS movies pre year
    fmpy = {}#FAIL movies pre year
    prpy={}#PASS revenue per year
    frpy = {}#FAIL revenue per year
    parpy = {}#PASS avarage movies pre year
    farpy={}#FAIL avarage movies pre year
    countamount_f_p={}
    count_revenue_wins_f_p={}
    mp=0
    mf=0
    rp=0
    rf=0
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            year = line["year"]
            if line["binary"] == "PASS":
                pmpy.setdefault(year, 0)
                pmpy[year]+=1
                if line["domgross"].isdigit():
                    domgross = int(line["domgross"])
                else:
                    domgross=0
                if line["intgross"].isdigit():
                    intgross = int(line["intgross"]) 
                else:
                    intgross=0
                revenue = domgross+intgross
                prpy.setdefault(year, 0)
                prpy[year]+=revenue
                for year in pmpy.keys():
                    average = prpy[year]/pmpy[year]
                    parpy[year] = round(average, 2)
            else:
                fmpy.setdefault(year, 0)
                fmpy[year]+=1
                if line["domgross"].isdigit():
                    domgross = int(line["domgross"])
                else:
                    domgross=0
                if line["intgross"].isdigit():
                    intgross = int(line["intgross"]) 
                else:
                    intgross=0
                revenue = domgross+intgross
                frpy.setdefault(year, 0)
                frpy[year]+=revenue
                for year in fmpy.keys():
                    average = frpy[year]/fmpy[year]
                    farpy[year] = round(average, 2)
        for year in fmpy.keys():
            try:
                if fmpy[year]<pmpy[year]:
                    countamount_f_p.setdefault(year,'')
                    countamount_f_p[year]+='more PASS' #of films that passed the test'
                    mp+=1
                else:
                    countamount_f_p.setdefault(year,'')
                    countamount_f_p[year]+='more FAIL' #of films that NOT passed the test'
                    mf+=1
                if farpy[year]<parpy[year]:
                    count_revenue_wins_f_p.setdefault(year,'')
                    count_revenue_wins_f_p[year]+='revenue of PASS' #films that passed the test is bigger'
                    rp+=1
                else:
                    count_revenue_wins_f_p.setdefault(year,'')
                    count_revenue_wins_f_p[year]+='revenue of FAIL' #films that NOT passed the test is bigger'
                    rf+=1
            except KeyError:
                pass
    return countamount_f_p, count_revenue_wins_f_p, mp,mf,rp,rf

A, R, Mp,Mf,Rp,Rf =bachdel_test('movies-bechdel.csv')
for year in A.keys():
    print(str(year)+' '+A[year]+'\n')
for year in R.keys():
    print(str(year)+' '+R[year]+'\n')
print('MORE PASS =' + str(Mp) + '\nMORE FAIL=' + str(Mf) + '\nREVENUE PASS =' + str(Rp) + '\nREVENUE FAIL=' + str(Rf))
