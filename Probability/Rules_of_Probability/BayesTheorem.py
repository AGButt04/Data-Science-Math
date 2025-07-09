# Applies Bayes’ Theorem: P(A | B) = P(B | A) * P(A) / P(B)

def bayes_theorem(p_b_given_a: float, p_a: float, p_b: float) -> float:
    """Returns P(A | B) using Bayes’ Theorem."""
    return (p_b_given_a * p_a) / p_b

# Example: Disease and test
# P(Disease) = 0.01
# P(Positive | Disease) = 0.99
# P(Positive | No Disease) = 0.05
# P(No Disease) = 0.99

p_disease = 0.01
p_no_disease = 0.99
p_pos_given_disease = 0.99
p_pos_given_no_disease = 0.05

# Total probability of positive test
p_positive = (p_pos_given_disease * p_disease) + (p_pos_given_no_disease * p_no_disease)

# Bayes' Theorem: P(Disease | Positive)
p_disease_given_positive = bayes_theorem(p_pos_given_disease, p_disease, p_positive)
print(f"P(Disease | Positive Test) = {round(p_disease_given_positive, 4)}")