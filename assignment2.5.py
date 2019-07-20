import csv 
import matplotlib.pyplot as plt 
matches= csv.DictReader(open('G:\desktop\ipl/matches.csv'))
deliveries= csv.DictReader(open('G:\desktop\ipl/deliveries.csv'))
total_match={}
toss_winners={}
toss_match_winners={}

for x in matches:
    if x['team1'] not in total_match.keys():
        total_match[x['team1']]=1
        toss_match_winners[x['team1']]=0
    else:
        total_match[x['team1']]=total_match[x['team1']]+1
        
    if x['team2'] not in total_match.keys():
        total_match[x['team2']]=1       
        toss_match_winners[x['team2']]=0
    else:
        total_match[x['team2']]=total_match[x['team2']]+1
    if x['toss_winner'] not in toss_winners.keys():
       toss_winners[x['toss_winner']]=1
    else:
        toss_winners[x['toss_winner']]=toss_winners[x['toss_winner']]+1
    if x['toss_winner']==x['winner']:
        toss_match_winners[x['toss_winner']]=toss_match_winners[x['toss_winner']]+1
a = dict({k: float(toss_winners[k])/toss_match_winners[k] for k in toss_match_winners.keys() & toss_winners})
b = dict({k: int(100*(toss_match_winners[k])/toss_winners[k]) for k in toss_winners.keys() & toss_match_winners})
print(""" 
                Predict the match Winner.
                if which team wins the toss that
                how much chances to win the match 
           """)
#print(total_match)
plt.bar(b.keys(),b  .values(),width= 0.5, color='g')
plt.xlabel("Bowlers",fontweight='bold')
plt.xticks(rotation=90)
plt.ylabel("Economy",fontweight='bold')
plt.show()
               
