import csv 
import matplotlib.pyplot as plt 
matches= csv.DictReader(open('G:\desktop\ipl/matches.csv'))
deliveries= csv.DictReader(open('G:\desktop\ipl/deliveries.csv'))
extra_run={}
match_id_list=[]
for x in matches:

    if x['season']=='2016':
        match_id_list.append(x['id'])
#print(match_id_list)

for raw in deliveries:
    if raw['match_id'] in match_id_list:
        if raw['bowling_team'] not in extra_run.keys():
            extra_run[raw['bowling_team']]=0
        else:
            extra_run[raw['bowling_team']]
            extra_run[raw['bowling_team']]=(extra_run[raw['bowling_team']]+int(raw['extra_runs']))

plt.bar(extra_run.keys() , extra_run.values() ,color = 'y')
plt.xticks(rotation='90')
plt.title(" Extra run in 2016",fontweight = 'bold')
plt.xlabel("Teams",fontweight = 'bold')
plt.ylabel("Extra_run",fontweight = 'bold')
plt.show()        
