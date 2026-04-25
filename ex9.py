SIMPLE PROBABILITY
import random
def coin_toss_probability():
    n = int(input("Enter the number of coin tosses: "))

    heads = 0
    tails = 0

    for i in range(n):
        toss = random.choice(['H', 'T'])
        print(f"Toss {i+1}: {toss}")

        if toss == 'H':
            heads += 1
        else:
            tails += 1

    print("\nResults:")
    print("Number of Heads:", heads)
    print("Number of Tails:", tails)

    print("\nProbabilities:")
    print("P(Heads) =", heads / n)
    print("P(Tails) =", tails / n)

coin_toss_probability()

--BAYES RULE--
def bayes_probability():
    print("Bayes Theorem Calculator P(A|B)\n")


    A = input("Enter event A (e.g., Cavity): ")
    B = input("Enter event B (e.g., Toothache): ")

    p_B_given_A = float(input(f"Enter P({B} | {A}): "))
    p_A = float(input(f"Enter P({A}): "))
    p_B = float(input(f"Enter P({B}): "))


    if p_B == 0:
        print("Error: P(B) cannot be zero.")
        return


    p_A_given_B = round((p_B_given_A * p_A) / p_B,4)

    print(f"\nP({A} | {B}) = {p_A_given_B}")


bayes_probability()

----JOINT PROBABILITY----------

from itertools import product

def parse_condition(cond):
    cond = cond.strip().lower()
    if cond.startswith('~'):
        return cond[1:], False
    return cond, True

def check_conditions(row, conditions):
    for var, val in conditions:
        if row[var] != val:
            return False
    return True

def compute_joint(kb, cond_a, cond_b):
    """P(A ∩ B) — both conditions hold simultaneously."""
    total = 0
    for row in kb:
        if check_conditions(row, cond_a) and check_conditions(row, cond_b):
            total += row['prob']
    return round(total, 4)

def compute_conditional(kb, cond_a, cond_b):
    """P(A | B) = P(A ∩ B) / P(B)."""
    p_joint = compute_joint(kb, cond_a, cond_b)
    p_b = 0
    for row in kb:
        if check_conditions(row, cond_b):
            p_b += row['prob']
    p_b = round(p_b, 4)
    if p_b == 0:
        return 0
    return round(p_joint / p_b, 4)

def compute_marginal(kb, conditions):
    """P(A) — marginal probability."""
    total = 0
    for row in kb:
        if check_conditions(row, conditions):
            total += row['prob']
    return round(total, 4)

def parse_query(query):
    """Parse queries like: P(A), P(A|B), P(A,B), P(A|~B)"""
    query = query.strip().lower().replace("p(", "").replace(")", "")

    if '|' in query:
        left, right = query.split('|')
        # support multiple givens: P(A|B,C)
        cond_a = [parse_condition(left.strip())]
        cond_b = [parse_condition(c.strip()) for c in right.split(',')]
        return 'conditional', cond_a, cond_b

    elif ',' in query:
        parts = [parse_condition(c.strip()) for c in query.split(',')]
        # joint: P(A, B)
        cond_a = [parts[0]]
        cond_b = parts[1:]
        return 'joint', cond_a, cond_b

    else:
        cond = [parse_condition(query.strip())]
        return 'marginal', cond, None

def main():
    print("=" * 50)
    print("  Joint & Conditional Probability Calculator")
    print("=" * 50)

    print("\nEnter number of variables:")
    num_vars = int(input())

    variables = []
    print("Enter variable names (one per line):")
    for _ in range(num_vars):
        variables.append(input().strip().lower())

    combinations = list(product([True, False], repeat=num_vars))
    kb = []

    print("\nEnter probabilities for each combination:\n")
    total_prob = 0
    for comb in combinations:
        row = {}
        condition_str = []
        for i, val in enumerate(comb):
            row[variables[i]] = val
            condition_str.append(f"{variables[i]}={'T' if val else 'F'}")
        print(", ".join(condition_str))
        prob = float(input("Probability: "))
        row['prob'] = prob
        total_prob += prob
        kb.append(row)

    print(f"\n[Info] Sum of all probabilities = {round(total_prob, 4)}")
    if abs(total_prob - 1.0) > 0.01:
        print("[Warning] Probabilities do not sum to 1.0")

    print("\n" + "=" * 50)
    print("  Query Section")
    print("=" * 50)
    print("  Supported formats:")
    print("    P(A)        → marginal probability")
    print("    P(A,B)      → joint probability P(A ∩ B)")
    print("    P(A|B)      → conditional probability P(A|B)")
    print("    P(A|~B)     → conditional with negation")
    print("    P(A|B,C)    → conditional with multiple givens")
    print("  Type 'exit' to stop.\n")

    while True:
        query = input("Enter query: ").strip()
        if query.lower() == 'exit':
            break

        try:
            qtype, cond_a, cond_b = parse_query(query)

            if qtype == 'marginal':
                result = compute_marginal(kb, cond_a)
                print(f"  Marginal P = {result}\n")

            elif qtype == 'joint':
                result = compute_joint(kb, cond_a, cond_b)
                a_str = query.split(',')[0].replace('p(','').replace('(','')
                b_str = ','.join(query.split(',')[1:]).replace(')','')
                print(f"  Joint  P({a_str.upper()} ∩ {b_str.upper()}) = {result}\n")

            elif qtype == 'conditional':
                result = compute_conditional(kb, cond_a, cond_b)
                # also show components
                p_joint = compute_joint(kb, cond_a, cond_b)
                p_b     = compute_marginal(kb, cond_b)
                print(f"  P(B)         = {p_b}")
                print(f"  P(A ∩ B)     = {p_joint}")
                print(f"  P(A | B)     = {p_joint} / {p_b} = {result}\n")

        except Exception as e:
            print(f"  [Error] Could not parse query: {e}\n")

if __name__ == "__main__":
    main()
