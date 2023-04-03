#Dictionary to store key value pair of cards
card_values = {
    'S2': 2, 'S3': 3, 'S4': 4, 'S5': 5, 'S6': 6, 'S7': 7, 'S8': 8, 'S9': 9, 'S10': 10,
    'SJ': 11, 'SQ': 12, 'SK': 13, 'SA': 14
}
#Mehtod/function to check staright sequence of cards
def check_straight(card1, card2, card3):
    sorted_cards = sorted([card1, card2, card3], key=lambda x: card_values[x])
    if card_values[sorted_cards[0]] + 1 == card_values[sorted_cards[1]] and \
       card_values[sorted_cards[1]] + 1 == card_values[sorted_cards[2]]:
        return card_values[sorted_cards[2]]
    return 0
#Method/Function to check 3 cards of same kind
def check_3ofa_kind(card1, card2, card3):
    if card1 == card2 and card2 == card3:
        return card_values[card1]
    else:
        return 0
#Method/Function to check royal flush (straight with the value of 14,) return 14 else 0
def check_royal_flush(card1, card2, card3):
    if check_straight(card1, card2, card3) == card_values['SA']:
        return 14
    else:
        return 0
#Method/Function to choose winer of the game
def play_cards(left1, left2, left3, right1, right2, right3):
    left_cards = [left1, left2, left3]
    right_cards = [right1, right2, right3]
    left_values = [card_values[card] for card in left_cards]
    right_values = [card_values[card] for card in right_cards]
    left_values.sort(reverse=True)
    right_values.sort(reverse=True)
    for i in range(3):
        if left_values[i] > right_values[i]:
            return -1
        elif left_values[i] < right_values[i]:
            return 1
    return 0


