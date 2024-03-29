# In the card game poker, a hand consists of five cards and are ranked,
# from lowest to highest, in the following way:
#     High Card: Highest value card.
#     One Pair: Two cards of the same value.
#     Two Pairs: Two different pairs.
#     Three of a Kind: Three cards of the same value.
#     Straight: All cards are consecutive values.
#     Flush: All cards of the same suit.
#     Full House: Three of a kind and a pair.
#     Four of a Kind: Four cards of the same value.
#     Straight Flush: All cards are consecutive values of same suit.
#     Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

# If two players have the same ranked hands then the rank made up of the highest value wins;
# for example, a pair of eights beats a pair of fives (see example 1 below).
# But if two ranks tie, for example, both players have a pair of queens,
# then highest cards in each hand are compared (see example 4 below);
# if the highest cards tie then the next highest cards are compared, and so on.

# Example hand:
# Player 1: 2D 9C AS AH AC; Three Aces
# Player 2: 3D 6D 7D TD QD; Flush with Diamonds
# Winner: Player 2

# The file, poker.txt, contains one-thousand random hands dealt to two players.
# Each line of the file contains ten cards (separated by a single space):
# the first five are Player 1's cards and the last five are Player 2's cards.
# You can assume that all hands are valid (no invalid characters or repeated cards),
# each player's hand is in no specific order, and in each hand there is a clear winner.
# How many hands does Player 1 win?

from time import time
start = time()

def convert_to_lists(s):
    """
    This function will convert a given string to lists with the value of cards and the suite of the cards
    Example: '5S 6S AC JS' => [['5', '6', 'A', 'J'],['S', 'S', 'C', 'S']]
    """
    cards = s.split(' ')
    card_value = []
    card_type = []
    for hand in cards:
        card_value.append(hand[0])
        card_type.append(hand[1])
    return [card_value, card_type]

hands = []
with open('054.txt', 'r') as f:
    for line in f.readlines():
        player_1 = convert_to_lists(line.strip()[:14])
        player_2 = convert_to_lists(line.strip()[15:])
        hands.append([player_1, player_2])

from collections import Counter

def number_of_pairs(l):
    """
    This function will return the number of pairs a given hand has.
    Also 1 is added to the pairs according to the priority list.
    Example: ['5','5','7','6','3'] => 2(one pair)
    ['5','5','6','6','7'] => 3(two pairs)
    ['4','3','Q','K','T'] => 0
    """
    count = Counter(l) - Counter(set(l))
    pairs = 0
    for i in count:
        if count[i] == 1:
            pairs += 1
    if pairs:
        return pairs + 1
    return 0

def three_of_a_kind(l):
    """
    This function will return 4 if there are three cards of same value.
    Returning of 4 is according to priority list.
    Example: ['5','5','5','T','Q'] => 4
    ['5', '7', 'Q', 'T', 'K'] => 0
    """
    count = Counter(l) - Counter(set(l))
    for i in count:
        if count[i] == 2:
            return 4
    return 0

def straight(l):
    """
    This function will return 5 if all cards are consecutive values.
    Returning 5 is according to priority list.
    Example: ['K', 'Q', 'J', 'T', '9'] => 5
    ['Q', 'T', '3', '2', '1'] => 0
    """
    rating = {14: 'A', 13: 'K', 12: 'Q', 11: 'J', 10: 'T', 9: '9',
              8: '8', 7: '7', 6: '6', 5: '5', 4: '4', 3: '3', 2: '2', 1: '1'}
    hv = high_card(l) # highest value of the hand
    if rating[hv - 1] in l:
        if rating[hv - 2] in l:
            if rating[hv - 3] in l:
                if rating[hv - 4] in l:
                    return 5
    return 0

def flush(l):
    """
    This function will return 6 if all All cards of the same suit.
    Returning 6 is according to priority list.
    Example: ['S', 'S', 'S', 'S', 'S'] => 6
    ['C', 'C', 'S', 'S', 'D'] => 0
    """
    if len(set(l)) == 1:
        return 6
    return 0

def full_house(l):
    """
    This function will return 7 if Three of a kind and a pair.
    Returning 7 is according to priority list.
    Example: ['T', 'T', 'T', 'A', 'A'] => 7
    ['A', '9', '8', 'Q', 'T'] => 0
    """
    if three_of_a_kind(l):
        if number_of_pairs(l) == 2:
            return 7
    return 0

def four_of_a_kind(l):
    """
    This function will return 8 if Four cards of the same value.
    Returning 8 is according to priority list.
    Example: ['K', 'K', 'K', 'K', '3'] => 8
    ['Q', 'K', 'T', '5', '3'] => 0
    """
    dup = Counter(l) - Counter(set(l))
    for i in dup:
        if dup[i] == 3:
            return 8
    return 0

def straight_flush(l, v):
    """
    This function will return 9 if all cards are consecutive values of same suit.
    Returning 9 is according to priority list.
    Example:
    ['4', '5', '6', '7', '8']['S', 'S', 'S', 'S', 'S'] => 9
    ['3', '9', 'Q', 'T', '2']['C', 'D', 'H', 'S', 'S'] => 0
    """
    if straight(l) and flush(v):
        return 9
    return 0

def royal_flush(l, v):
    """
    This function will return 10 if Ten, Jack, Queen, King, Ace, in same suit.
    Returning 10 is according to priority list.
    Example:
    ['T', 'J', 'Q', 'K', 'A']['H', 'H', 'H', 'H', 'H'] => 10
    ['3', 'T', '9', '8', 'A']['S', 'D', 'H', 'S', 'S'] => 0
    """
    if set(['T', 'J', 'Q', 'K', 'A']) == set(l):
        if len(set(v)) == 1:
            return 10
    return 0

def paired_number(l):
    """
    This function will return largest number, if there is a pair in the hand.
    The number returned will be in the format of high_card function.
    Example: ['5', '5', '6', '7', 'K'] => 5
    ['K', 'K', 'T', 'T', '8'] => 13
    """
    repeated = (Counter(l) - Counter(set(l))).keys()
    rating = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9,
              '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, '1': 1}
    highest = 0
    for i in repeated:
        if rating[i] > highest:
            highest = rating[i]
    return highest

def high_card(hand):
    """
    This function will return the value of highest valued card in the given hand
    Example: ['5', '6', 'A', 'J'] => 14('A')
    """
    highest = 0
    for i in hand:
        if i == 'A':
            return 14
        elif i == 'K':
            if 13 >= highest:
                highest = 13
        elif i == 'Q':
            if 12 >= highest:
                highest = 12
        elif i == 'J':
            if 11 >= highest:
                highest = 11
        elif i == 'T':
            if 10 >= highest:
                highest = 10
        elif int(i) > highest:
            highest = int(i)
    return highest

counter = 0 # number of times player 1 wins
for hand in hands:
    p1v = hand[0][0] # card values of player 1
    p2v = hand[1][0] # card values of player 2
    p1s = hand[0][1] # suites of player 1
    p2s = hand[1][1] # suites of player 2
    
    p1 = 0 # score of player 1
    p2 = 0 # score of player 2
    flag = False # in case we need to check the paired cards
    
    # conditions for player 1
    if number_of_pairs(p1v):
        p1 = number_of_pairs(p1v)
        flag = True
    if three_of_a_kind(p1v):
        p1 = three_of_a_kind(p1v)
        flag = True
    if straight(p1v):
        p1 = straight(p1v)
    if flush(p1s):
        p1 = flush(p1s)
    if full_house(p1v):
        p1 = full_house(p1v)
        flag = True
    if four_of_a_kind(p1v):
        p1 = four_of_a_kind(p1v)
        flag = True
    if straight_flush(p1v, p1s):
        p1 = straight_flush(p1v, p1s)
    if royal_flush(p1v, p1s):
        p1 = royal_flush(p1v, p1s)

    # conditions for player 2
    if number_of_pairs(p2v):
        p2 = number_of_pairs(p2v)
        flag = True
    if three_of_a_kind(p2v):
        p2 = three_of_a_kind(p2v)
        flag = True
    if straight(p2v):
        p2 = straight(p2v)
    if flush(p2s):
        p2 = flush(p2s)
    if full_house(p2v):
        p2 = full_house(p2v)
        flag = True
    if four_of_a_kind(p2v):
        p2 = four_of_a_kind(p2v)
        flag = True
    if straight_flush(p2v, p2s):
        p2 = straight_flush(p2v, p2s)
    if royal_flush(p2v, p2s):
        p2 = royal_flush(p2v, p2s)

    # score more for player 1
    if p1 > p2:
        counter += 1
    elif p1 == p2: # both players same score
        if flag: # cards having pairs
            if paired_number(hand[0][0]) > paired_number(hand[1][0]):  # highest in a pair
                counter += 1
            elif paired_number(hand[0][0]) == paired_number(hand[1][0]): # equal highest in a pair
                if high_card(hand[0][0]) > high_card(hand[1][0]):
                    counter += 1
        else: # cards not having pairs
            if high_card(hand[0][0]) > high_card(hand[1][0]):
                counter += 1

print(counter)

print(time() - start)

# Answer: 376
