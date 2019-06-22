# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                                                                                 #
#                          WHITEBOARDING FOR UNIT 3 HOMEWORK  -  PyPoll                           #
#                                                                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# PyPoll
# DONE import the election data
# DONE calculate the total number of votes cast (this will be a sum of the entire votes column)
# PARTIAL list unique candidates that recieved votes
# DONE calculate total votes per unique candidate
# calculate percentage of total that each candidate recieved
# find the winner based on popular vote (this will be the candidate with the highest number of votes (alternately the highest percentage of votes)
# print results to both the terminal and to a text file

# election_data file is
# 3 columns [Voter ID, County, Candidate]
# this is included in a header row


# import the election data
import os
import csv

election_data_path = os.path.join('election_data.csv')

with open(election_data_path, 'r') as file:
    election_data = csv.reader(file, delimiter=',')
    header = next(election_data)
    each_vote = list(election_data)
    voter_id, county, candidate_vote = zip(*each_vote)    
    
# calculate the number of votes cast per candidate, then total...
    candidate_count = {}
    for candidate in candidate_vote:
        candidate_count.setdefault(candidate, 0)
        candidate_count[candidate] = candidate_count[candidate] + 1
        
# calculate the total number of votes cast (this will be a sum of the entire votes per candidate)
    total_votes_ALL = candidate_count.get('Khan') + candidate_count.get('Correy') + candidate_count.get('Li') + candidate_count.get("O'Tooley")
    
# create list of unique candidates that recieved votes
    candidate = list(dict.keys(candidate_count))
    
# create list of votes counts per candidate in list
    votesPER = list(dict.values(candidate_count))
    
# calculate percentage for each candidate
    pct_vote = []
    for votes in votesPER:
        pct = votes/total_votes_ALL
        pct_vote.append('{:.3%}'.format(pct))
        
# get index of winning vote count; calling winner in print function
    w = votesPER.index(max(votesPER))


    print('Election Results')
    print('- - - - - - - - - - - - - - - - - - - -')
    print('Total Votes: ', total_votes_ALL)
    print('- - - - - - - - - - - - - - - - - - - -')
    i = 0
    for person in candidate:
        print(candidate[i], ' ', pct_vote[i], ' ', votesPER[i])
        i += 1
    print('- - - - - - - - - - - - - - - - - - - -')
# find the winner based on popular vote (candidate with most votes/alternately the highest percentage of votes)
    print('Winner: ', candidate[w])
    print('- - - - - - - - - - - - - - - - - - - -')
    
    with open('ElectionResults.txt', 'w') as f:    
        print('Election Results', file=f)
        print('- - - - - - - - - - - - - - - - - - - -', file=f)
        print('Total Votes: ', total_votes_ALL, file=f)
        print('- - - - - - - - - - - - - - - - - - - -', file=f)
        i = 0
        for person in candidate:
            print(candidate[i], ' ', pct_vote[i], ' ', votesPER[i], file=f)
            i += 1
        print('- - - - - - - - - - - - - - - - - - - -', file=f)
        print('Winner: ', candidate[w], file=f)
        print('- - - - - - - - - - - - - - - - - - - -', file=f)