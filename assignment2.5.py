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

#print(total_match)
print(toss_winners)
print(toss_match_winners)
        