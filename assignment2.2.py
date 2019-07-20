import csv 
import matplotlib.pyplot as plt 
winner=[]
years=[]
winner_count={}
reader= csv.DictReader(open('G:\desktop\ipl/matches.csv'))
for raw in reader:
    winner.append(raw['winner'])
 #   print(winner)
    year=list(set(years))
    if raw['winner'] not in winner_count.keys():
        winner_count[(raw['winner'])]=0
    else:
        winner_count[raw['winner']]=winner.count(raw['winner'])

plt.bar(winner_count.keys(), winner_count.values(), color='y')
plt.xlabel("Years")
plt.xticks(rotation='90')
plt.ylabel("Matches Played")
plt.show()
