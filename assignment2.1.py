
import csv 
import matplotlib.pyplot as plt 
years=[]
x=[]
year_count={}
#
reader= csv.DictReader(open('G:\desktop\ipl/matches.csv'))

for raw in reader:
    years.append(raw['season'])
    year=list(set(years))
    if raw['season'] not in year_count.keys():
        year_count[(raw['season'])]=0
    else:
        year_count[raw['season']]=years.count(raw['season'])

plt.bar(year_count.keys(), year_count.values(), color='y')
plt.xlabel("Years")
plt.ylabel("Matches Played")
plt.show()