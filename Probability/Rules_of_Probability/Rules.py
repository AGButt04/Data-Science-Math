# Addition Rule = P(a) + P(b) - P(a intersection b)
def prob_a_or_b(a, b, all_possible) -> float:
    # Probability of event a
    prob_a = len(a)/ len(all_possible)
    # Probability of event b
    prob_b = len(b) / len(all_possible)
    # Probability of intersection
    intersection = a.intersection(b)
    prob_intersection = len(intersection) / len(all_possible)

    prob = prob_a + prob_b - prob_intersection
    return prob

# Probability of rolling a die once and getting an even number or an odd number
evens = {2, 4, 6}
odds = {1, 3, 5}
all_possible_rolls = {1, 2, 3, 4, 5, 6}
print(prob_a_or_b(evens, odds, all_possible_rolls))

# Probability of rolling a die once and getting an odd number or a number greater than 2
greater_than_two = {3, 4, 5, 6}
print(prob_a_or_b(odds, greater_than_two,all_possible_rolls))

# Probability of Selecting a diamond card or a face card from a standard deck of cards
diamond_cards = {'ace_diamond', '2_diamond', '3_diamond', '4_diamond', '5_diamond', '6_diamond', '7_diamond',
                 '8_diamond', '9_diamond', '10_diamond', 'jack_diamond', 'queen_diamond', 'king_diamond'}
face_cards = {'jack_diamond', 'jack_spade', 'jack_heart', 'jack_club', 'queen_diamond', 'queen_spade',
              'queen_heart', 'queen_club', 'king_diamond', 'king_spade', 'king_heart', 'king_club'}

# All cards in a deck representing the entire sample space
all_possible_cards = {'ace_diamond', '2_diamond', '3_diamond', '4_diamond', '5_diamond', '6_diamond', '7_diamond',
                      '8_diamond', '9_diamond', '10_diamond', 'jack_diamond', 'queen_diamond', 'king_diamond', 'ace_heart',
                      '2_heart', '3_heart', '4_heart', '5_heart', '6_heart', '7_heart', '8_heart', '9_heart', '10_heart',
                      'jack_heart', 'queen_heart', 'king_heart', 'ace_spade', '2_spade', '3_spade', '4_spade', '5_spade',
                      '6_spade', '7_spade', '8_spade', '9_spade', '10_spade', 'jack_spade', 'queen_spade', 'king_spade',
                      'ace_club', '2_club', '3_club', '4_club', '5_club', '6_club', '7_club', '8_club', '9_club', '10_club',
                      'jack_club', 'queen_club', 'king_club'}

print(prob_a_or_b(diamond_cards, face_cards, all_possible_cards))

# Calculates probability of A and B using multiplication rule
# For dependent events: P(A and B) = P(A) * P(B | A)

def multiplication_rule(p_a: float, p_b_given_a: float) -> float:
    return p_a * p_b_given_a

# Example: Drawing 2 blue marbles without replacement from 2 blue and 3 red
# P(Blue1) = 2/5, P(Blue2 | Blue1) = 1/4
p_a = 2 / 5
p_b_given_a = 1 / 4

result = multiplication_rule(p_a, p_b_given_a)
print(f"P(Blue1 and Blue2) = {round(result, 4)}")