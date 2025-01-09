# T-Way Combinatorial Testing with Artificial Immune Algorithm (AIA)

## Overview
T-way combinatorial testing is an effective software testing approach that ensures interaction faults are detected by covering all combinations of parameter subsets of size `t`. It reduces the need for exhaustive testing, making it practical for systems with numerous configurable parameters. Despite its effectiveness, challenges such as combinatorial explosion and constraint handling make it computationally demanding.

The **Artificial Immune Algorithm (AIA)** is a metaheuristic inspired by the biological immune system. It employs mechanisms like affinity-based selection, cloning, and mutation to solve optimization problems, making it an ideal approach for t-way combinatorial testing.

## Artificial Immune Algorithm (AIA)
AIA mimics the human immune system's ability to detect and neutralize harmful pathogens. Key components of the algorithm include:
- **Affinity-Based Selection**: Prioritizes test cases based on their ability to cover uncovered parameter combinations.
- **Cloning and Mutation**: High-affinity test cases are cloned and mutated to enhance diversity and coverage.
- **Constraint Handling**: Ensures generated test cases respect given constraints, avoiding invalid combinations.

This adaptability allows AIA to efficiently generate compact test suites while maintaining 100% t-way interaction coverage.

## Implementation of AIA for T-Way Testing
Our implementation of AIA for t-way testing involves the following steps:
1. **Generate T-Way Combinations**: All possible t-way parameter combinations are generated for testing.
2. **Initialize Population**: An initial population of random, constraint-respecting test cases is created.
3. **Calculate Affinity**: Affinity scores are computed based on how well each test case covers uncovered combinations.
4. **Clone and Mutate**: Test cases with high affinity are cloned and mutated to explore diverse solutions.
5. **Selection and Test Suite Update**: Test cases with the highest affinity are selected and added to the test suite, reducing the set of uncovered combinations.
6. **Iteration and Optimization**: The process continues iteratively until all t-way combinations are covered or the maximum number of iterations is reached.

## Features
- **Efficient Test Suite Generation**: Ensures full t-way interaction coverage with minimal test cases.
- **Constraint Handling**: Avoids invalid or forbidden combinations during test generation.
- **Diversity Preservation**: Prevents duplicates and promotes variety in test cases.

## Running the Code
1. Clone this repository.
2. Open Google colab past the code.
3. Run the script using the input.
4. Below a input given.

## Input
To run the algorithm, configure the following inputs in the script:

  ```python
t = 2  # Strength of interaction
population_size = 20
max_iterations = 75
parameters = [
    ['a1', 'a2', 'a3'],
    ['b1', 'b2', 'b3'],
    ['c1', 'c2', 'c3'],
    ['d1', 'd2', 'd3'],
]
forbidden_combinations = []

