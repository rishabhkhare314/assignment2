import csv 
import matplotlib.pyplot as plt 
matches= csv.DictReader(open('G:\desktop\ipl/matches.csv'))
deliveries= csv.DictReader(open('G:\desktop\ipl/deliveries.csv'))
bowler_name={}
economy={}
match_id_list=[]
for x in matches:
    if x['season']=='2015':
        #print("this is x",x)
        match_id_list.append(x['id'])
for raw in deliveries:
    if raw['match_id'] in match_id_list:
        #print(raw)
        if raw['bowler'] not in bowler_name.keys():
            bowler_name[raw['bowler']]=[0,0]
            
        else:
            bowler_name[raw['bowler']][0]=(bowler_name[raw['bowler']][0]+int(raw['total_runs']))
            bowler_name[raw['bowler']][1]=(bowler_name[raw['bowler']][1]+1)
            if int(raw['noball_runs'])>0 or  int(raw['wide_runs'])>0:
                bowler_name[raw['bowler']][1]=(bowler_name[raw['bowler']][1]-1)
        
bowler=bowler_name.keys()
for bowl in bowler:
    economy[bowl]=(bowler_name[bowl][0])/bowler_name[bowl][1]*6
plt.bar(economy.keys(),economy.values(),width= 0.5, color='g')
plt.xlabel("Bowlers",fontweight='bold')
plt.xticks(rotation=90)
plt.ylabel("Economy",fontweight='bold')
plt.show()
    