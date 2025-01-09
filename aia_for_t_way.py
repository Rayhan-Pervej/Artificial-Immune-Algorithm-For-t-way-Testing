import random
import itertools

def generate_t_way_combinations(parameters, t):
    """Generate all t-way parameter combinations."""
    parameter_indices = range(len(parameters))
    t_combinations = list(itertools.combinations(parameter_indices, t))
    value_combinations = []
    for combination in t_combinations:
        values = itertools.product(*[parameters[i] for i in combination])
        for value in values:
            value_combinations.append((combination, value))
    return value_combinations

def calculate_affinity(test_case, uncovered_combinations):
    """Calculate affinity as the number of newly covered combinations."""
    newly_covered = sum(
        all(test_case[i] == v for i, v in zip(combination, values))
        for combination, values in uncovered_combinations
    )
    return newly_covered

def generate_initial_population(parameters, population_size, forbidden_combinations):
    """Generate an initial population of test cases."""
    population = []
    while len(population) < population_size:
        candidate = [random.choice(param) for param in parameters]
        if not violates_constraints(candidate, forbidden_combinations):
            population.append(candidate)
    return population

def mutate(test_case, parameters, mutation_prob, forbidden_combinations):
    """Apply mutation to a test case."""
    mutated = test_case.copy()
    for i in range(len(mutated)):
        if random.random() < mutation_prob:
            mutated[i] = random.choice(parameters[i])
    if violates_constraints(mutated, forbidden_combinations):
        return mutate(test_case, parameters, mutation_prob, forbidden_combinations)  # Retry mutation if constraints violated
    return mutated

def violates_constraints(test_case, forbidden_combinations):
    """Check if a test case violates any forbidden combinations."""
    return any(all(test_case[i] == v for i, v in combination) for combination in forbidden_combinations)

def is_duplicate(test_case, test_suite, distance_threshold=1):
    """Check if a test case is a near-duplicate based on Hamming distance."""
    for existing_case in test_suite:
        distance = sum(existing_case[i] != test_case[i] for i in range(len(existing_case)))
        if distance < distance_threshold:
            return True
    return False

def aia_algo(parameters, t, population_size, max_iterations, forbidden_combinations):
    """Run the Artificial Immune Algorithm for t-way test suite generation."""
    # Generate all t-way combinations
    uncovered_combinations = set(generate_t_way_combinations(parameters, t))
    total_combinations = len(uncovered_combinations)

    # Initialize population
    population = generate_initial_population(parameters, population_size, forbidden_combinations)
    test_suite = []

    for iteration in range(max_iterations):
        print(f"Iteration {iteration + 1}: Uncovered combinations remaining: {len(uncovered_combinations)}")

        # Calculate affinity for each test case
        affinities = [calculate_affinity(tc, uncovered_combinations) for tc in population]

        # Clone and mutate based on affinity
        clones = []
        for test_case, affinity in zip(population, affinities):
            clone_count = max(1, int(affinity))
            for _ in range(clone_count):
                mutated_clone = mutate(test_case, parameters, 1/1+affinity, forbidden_combinations)
                if not is_duplicate(mutated_clone, clones):
                    clones.append(mutated_clone)

        # Select the best solutions based on affinity
        population = sorted(clones, key=lambda tc: calculate_affinity(tc, uncovered_combinations), reverse=True)
        population = population[:population_size]

        # Add high-coverage test cases to the test suite
        for test_case in population:
            newly_covered = {
                (combination, values)
                for combination, values in uncovered_combinations
                if all(test_case[i] == v for i, v in zip(combination, values))
            }
            if newly_covered and not is_duplicate(test_case, test_suite):
                test_suite.append(test_case)
                uncovered_combinations -= newly_covered

        # Stop if all combinations are covered
        if not uncovered_combinations:
            print("All t-way combinations are covered!")
            break

    print(f"Final Test Suite Size: {len(test_suite)}")
    print(f"Coverage Achieved: {total_combinations - len(uncovered_combinations)}/{total_combinations} ({(total_combinations - len(uncovered_combinations)) / total_combinations * 100:.2f}%)")
    return test_suite

# Input
parameters = [
    ['a1', 'a2', 'a3'],
    ['b1', 'b2', 'b3'],
    ['c1', 'c2', 'c3'],
    ['d1', 'd2', 'd3'],

]
t = 2 # Strength of interaction
population_size = 20
max_iterations = 75
forbidden_combinations = [
    ]

test_suite = aia_algo(parameters, t, population_size, max_iterations, forbidden_combinations)

print("\nGenerated Test Suite:")
for idx, test_case in enumerate(test_suite, start=1):
    print(f"Test Case {idx}: {test_case}")
