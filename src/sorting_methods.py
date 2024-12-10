from collections import Counter
import math

def calculate_entropy(silo):
    """
    Calculate the Shannon entropy of a single silo (a measure of disorder).

    Args:
        silo (list): A list of ball colors in a silo.

    Returns:
        float: The calculated entropy value.
    """
    count = Counter(silo)
    total_balls = len(silo)
    probabilities = [freq / total_balls for freq in count.values()]
    return -sum(p * math.log2(p) for p in probabilities)

def conventional_sorting(silos):
    """
    Sort each silo's balls alphabetically.

    Args:
        silos (list): A list of silos, where each silo contains ball colors.

    Returns:
        list: A new list of silos with sorted ball colors.
    """
    return [sorted(silo) for silo in silos]

def entropy_based_sorting(silos, colors):
    """
    Redistribute all balls into silos by color, minimizing entropy.

    Args:
        silos (list): A list of silos with ball colors.
        colors (list): The list of available ball colors.

    Returns:
        list: A list of silos with balls grouped by color.
    """
    # Collect all balls into a single list
    all_balls = [ball for silo in silos for ball in silo]

    # Group balls by color
    color_buckets = {color: [] for color in colors}
    for ball in all_balls:
        color_buckets[ball].append(ball)

    # Redistribute balls into silos
    sorted_silos = []
    for color in colors[:len(silos)]:
        sorted_silos.append(color_buckets[color][:len(silos[0])])
    
    return sorted_silos

def pairwise_sorting(silos):
    """
    Balance the ball colors between adjacent silos by swapping balls iteratively.

    Args:
        silos (list): A list of silos with ball colors.

    Returns:
        list: A new list of silos with balanced ball distributions.
    """
    num_silos = len(silos)
    max_iterations = 10  # Prevent infinite swapping

    for _ in range(max_iterations):
        changes = 0
        for i in range(num_silos - 1):
            silo_a, silo_b = silos[i], silos[i + 1]
            a_counter, b_counter = Counter(silo_a), Counter(silo_b)

            # Swap balls to balance color distribution between silo_a and silo_b
            for color in set(a_counter.keys()).union(b_counter.keys()):
                while a_counter[color] > b_counter[color] + 1:
                    silo_a.remove(color)
                    silo_b.append(color)
                    a_counter[color] -= 1
                    b_counter[color] += 1
                    changes += 1

                while b_counter[color] > a_counter[color] + 1:
                    silo_b.remove(color)
                    silo_a.append(color)
                    b_counter[color] -= 1
                    a_counter[color] += 1
                    changes += 1

        if changes == 0:
            break  # Stop if no changes were made
    
    return silos

if __name__ == "__main__":
    # Example usage for testing
    from generate_silos import generate_silos

    # Generate silos
    NUM_SILOS = 5
    BALLS_PER_SILO = 10
    COLORS = ["red", "blue", "green", "yellow", "purple"]

    silos = generate_silos(NUM_SILOS, BALLS_PER_SILO, COLORS)
    print("Original Silos:")
    for idx, silo in enumerate(silos, 1):
        print(f"Silo {idx}: {silo}")

    # Apply sorting methods
    print("\nConventional Sorting:")
    for idx, silo in enumerate(conventional_sorting(silos), 1):
        print(f"Silo {idx}: {silo}")

    print("\nEntropy-Based Sorting:")
    for idx, silo in enumerate(entropy_based_sorting(silos, COLORS), 1):
        print(f"Silo {idx}: {silo}")

    print("\nPairwise Sorting:")
    for idx, silo in enumerate(pairwise_sorting(silos), 1):
        print(f"Silo {idx}: {silo}")

