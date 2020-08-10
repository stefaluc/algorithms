#!/usr/bin/python
from random import randint
from random import choice
from copy import copy, deepcopy
from datetime import datetime
import numpy as np

startTime = datetime.now()

scores = []
memLong = set()
branchesTrimmed = 0

# recurse for every possible permutation of card placements
def blitz(deck, pos, score, strikes, streak, board, moves, isEndDeck):
    # terminate if a strike occurs or the deck has been gone through
    if strikes > 0 or pos > len(deck) - 1:
        global scores
        # record score and data for this round
        scores.append({score: [moves, board, strikes, streak]})
        return

    memLat = []
    for i in range(0, 4):
        # if turn has multiple same lanes, only need to recurse into one
        if sum(board[i]) in memLat:
            continue
        memLat.append(sum(board[i]))

        # make copies of state to keep consistent
        boardCopy = deepcopy(board)
        streakCopy = streak

        moves.append(i)
        didStrike, moveScore = placeCard(boardCopy[i], deck[pos])

        # update streak
        if moveScore > 0:
            streakCopy += 1
        else: # streak broke
            streakCopy = 0
        newScore = score + moveScore + calcStreak(streakCopy)

        # if this exact state has been seen before, dont need to check again
        global memLong
        global branchesTrimmed
        key = buildMemKey(pos, newScore, streakCopy, boardCopy)
        if key in memLong:
            branchesTrimmed += 1
            continue
        memLong.add(key)

        # perfect game
        if len(boardCopy[0]) == 0 and len(boardCopy[1]) == 0 and len(boardCopy[2]) == 0 and len(boardCopy[3]) == 0 and didStrike +strikes == 0 and pos == len(deck) - 1 and isEndDeck:
            newScore += 1000

        blitz(deck, pos + 1, newScore, strikes + didStrike, streakCopy, boardCopy, moves[:], isEndDeck)
        moves.pop(len(moves)-1) # keep moves consistent for next loop iteration

def buildMemKey(pos, score, streak, board):
    return str(pos) + ' ' + str(score) + ' ' + str(streak) + ' ' + str(board)

def placeCard(zone, card):
    zone.append(card)
    strikes = 0
    score = 0
    total = sum(zone)

    # account for aces. This probably doesn't work for 2 aces in a lane
    if 11 in zone and total > 21:
        total -= 10

    # 5 card wild 21 clear
    #if len(zone) == 5 and card == 12 and total == 21:
    #    score += 1200
    #    del zone[:]
    ## 5 card wild clear
    #if len(zone) == 5 and card == 12 and total < 22:
    #    score += 800
    #    del zone[:]
    ## 5 card 21 clear
    #elif len(zone) == 5 and total == 21:
    #    score += 1000
    #    del zone[:]
    ## 5 card clear
    #elif len(zone) == 5 and total < 22:
    #    score += 600
    #    del zone[:]
    # 21 clear
    if total == 21:
        score += 400
        del zone[:]
    # wild clear
    elif card == 12:
        score += 200
        del zone[:]
    # bust
    elif total > 21:
        strikes += 1
        del zone[:]

    return strikes, score

def calcStreak(streak):
    if streak < 2:
        return 0
    elif streak == 2:
        return 250
    elif streak == 3:
        return 500
    elif streak == 4:
        return 750
    elif streak == 5:
        return 1000
    elif streak == 6:
        return 1250
    else:
        return 1250

#deck = [10, 10, 10, 2, 2, 11, 7, 10, 5, 10, 6, 5, 2, 4, 11, 10, 4, 5, 10, 5, 3, 10, 10, 10, 12, 9, 6, 10, 10, 12, 7, 6, 8, 10, 3, 8, 11, 11, 4, 9, 10, 8, 6, 9, 2, 8, 4, 9, 3, 7, 7, 3]
deck = [8, 7, 10, 10, 2, 3, 10, 12, 2, 5, 10, 5, 6, 3, 12, 4, 9, 10, 9, 2, 4, 11, 6, 8, 11, 2, 10, 10, 11, 9, 9, 5, 6, 3, 3, 10, 5, 7, 10, 11, 10, 5, 10, 4, 7, 8, 10, 8, 10, 4, 7, 10]

# split deck into chunks to better run resursive function
#deck1 = [10, 10, 10, 2, 2, 11, 7, 10, 5, 10, 6, 5, 2]
deck1 = [10, 10, 10, 2, 2, 11, 7]
deck2 = [4, 11, 10, 4, 5, 10, 5, 3, 10, 10, 10, 12, 9]
deck3 = [6, 10, 10, 12, 7, 6, 8, 10, 3, 8, 11, 11, 4, 9]
deck4 = [10, 8, 6, 9, 2, 8, 4, 9, 3, 7, 7, 3]

#deck1 = [10, 10, 10, 2, 2, 11, 7, 10, 5, 10, 6, 5, 2, 4]
#deck2 = [5, 2, 4, 11, 10, 4, 5, 10, 5, 3, 10, 10, 10, 12]
#deck3 = [10, 10, 12, 9, 6, 10, 10, 12, 7, 6, 8, 10, 3, 8, 11, 11, 4, 9, 10, 8, 6, 9, 2]
#deck4 = [8, 4, 9, 3, 7, 7, 3]

#blitz(deck[:15], 0, 0, 0, 0, [[], [], [], []], [], False)
#blitz(deck[15:30], 0, 0, 0, 3, [[8], [], [], []], [], False)
blitz(deck[30:], 0, 0, 0, 2, [[], [10,9], [], []], [], True)

#blitz(deck[:18], 0, 0, 0, 0, [[], [], [], []], [])
#blitz(deck[18:34], 0, 0, 0, 0, [[4], [5], [], []], [])
#blitz(deck[34:], 0, 0, 0, 3, [[8], [10], [9], []], [])

#blitz(deck1, 0, 0, 0, 0, [[], [], [], []], [])
#blitz(deck2, 0, 0, 0, 2, [[], [], [], [7, 10]], [])
#blitz(deck3, 0, 0, 0, 3, [[10], [], [10,5], []], [])
#blitz(deck4, 0, 0, 0, 0, [[4,9], [10,5], [], []], [])
#blitz(deck5, 0, 0, 0, 0, [[6], [8], [4], []], [])

#blitz(deck2, 0, 0, 0, 1, [[], [10], [], []], [])
# blitz(deck3, 0, 0, 0, 0, [[3, 10], [10, 10], [], [4]], [])
# blitz(deck4, 0, 0, 0, 3, [[], [], [8], []], [])
print len(scores)

# print score data
maxScore = -1
maxMoves = []
for play in scores:
    score = play.keys()[0]
    if play.keys()[0] >= maxScore and play.values()[0][2] < 1:
        if play.keys()[0] == maxScore:
            print play
        maxScore = score
        maxMoves = play
print maxScore
print maxMoves
print len(memLong)
print branchesTrimmed
print
print len(scores)
print datetime.now() - startTime
#print len(deck1) + len(deck2)+len(deck3)+len(deck4)+len(deck5)
#print len(deck)
#outcomes = blitz(deck)
#highScore = max(outcomes[0])
#optimalIndex = max(range(len(outcomes[0])), key=outcomes[0].__getitem__)
#optimal = outcomes[1][optimalIndex]

#print outcomes
#print (highScore, optimal)


# algorithm to try a bunch of random moves

# def blitz(deck):
#     outcomes = []
#     scores = []
#     for i in range(0, 5000000):
#         zero = []
#         one = []
#         two = []
#         three = []
#         board = [zero, one, two, three]
#         strikes = 0
#         score = 0
#         moves = []
#         streak = 0
# 
#         for card in deck:
#             # strategy
#             if strikes > 2:
#                 break
#             placement = -1
#             if sum(zero) + card < 21 and (len(zero)+1) == 5:
#                 placement = 0
#             elif sum(one) + card < 21 and (len(one)+1) == 5:
#                 placement = 1
#             elif sum(two) + card < 21 and (len(two)+1) == 5:
#                 placement = 2
#             elif sum(three) + card < 21 and (len(three)+1) == 5:
#                 placement = 3
#             if sum(zero) + card == 21:
#                 placement = 0
#             elif sum(one) + card == 21:
#                 placement = 1
#             elif sum(two) + card == 21:
#                 placement = 2
#             elif sum(three) + card == 21:
#                 placement = 3
#             elif sum(zero) + card == 11:
#                 placement = 0
#             elif sum(one) + card == 11:
#                 placement = 1
#             elif sum(two) + card == 11:
#                 placement = 2
#             elif sum(three) + card == 11:
#                 placement = 3
#             else:
#                 placement = randint(0, 3)
#                 invalid = [placement]
#                 for i in range(0, 2):
#                     if sum(board[placement]) > 20:
#                         invalid.append(placement)
#                         try:
#                             placement = choice([i for i in range(0, 4) if i not in invalid])
#                         except:
#                             placement = randint(0,3)
#             moves.append(placement)
# 
#             if placement == 0:
#                 strike, moveScore = placeCard(zero, card)
#                 if moveScore > 0:
#                     streak += 1
#                 else:
#                     streak = 0
#                 strikes += strike
#                 score += moveScore
#             elif placement == 1:
#                 strike, moveScore = placeCard(one, card)
#                 if moveScore > 0:
#                     streak += 1
#                 else:
#                     streak = 0
#                 strikes += strike
#                 score += moveScore
#             elif placement == 2:
#                 strike, moveScore = placeCard(two, card)
#                 if moveScore > 0:
#                     streak += 1
#                 else:
#                     streak = 0
#                 strikes += strike
#                 score += moveScore
#             elif placement == 3:
#                 strike, moveScore = placeCard(three, card)
#                 if moveScore > 0:
#                     streak += 1
#                 else:
#                     streak = 0
#                 strikes += strike
#                 score += moveScore
# 
#             #print str(zero) + str(one) + str(two) + str(three)
#             score += calcStreak(streak)
# 
#         # perfect game
#         if len(moves) == 52 and strikes == 0:
#             score += 1000
# 
#         outcomes.append(moves)
#         scores.append(score)
#     return (scores, outcomes)

