import random
from collections import Counter
from math import log2

def mrsa_filter(silos, max_iterations=1000):
    """
    MRSA Filter: Minimum Random Swaps for Alignment.

    This method iteratively reduces disorder (entropy) in silos by randomly swapping 
    balls between silos. If a swap improves the overall alignment (reduces entropy), 
    it's kept. Otherwise, it's undone. Think of it as 'trial and error' for better balance.

    Args:
        silos (list): A list of silos, each containing colored balls.
        max_iterations (int): How many swaps to attempt before stopping.

    Returns:
        list: The silos with improved alignment (lower entropy).
    """
    def calculate_total_entropy(silos):
        """
        Calculate the total entropy of the system by summing entropy for each silo.
        Entropy measures the disorder in a silo: lower entropy means better alignment.
        """
        total_entropy = 0
        for silo in silos:
            if len(silo) > 0:  # Avoid division by zero
                counts = Counter(silo)
                probabilities = [count / len(silo) for count in counts.values()]
                total_entropy += -sum(p * log2(p) for p in probabilities)
        return total_entropy

    current_entropy = calculate_total_entropy(silos)
    num_silos = len(silos)

    for _ in range(max_iterations):
        # Pick two random silos
        silo_a_idx, silo_b_idx = random.sample(range(num_silos), 2)
        silo_a, silo_b = silos[silo_a_idx], silos[silo_b_idx]

        # Skip if one of the silos is empty
        if not silo_a or not silo_b:
            continue

        # Randomly swap a ball between the two silos
        ball_a = random.choice(silo_a)
        ball_b = random.choice(silo_b)
        silo_a.remove(ball_a)
        silo_b.remove(ball_b)
        silo_a.append(ball_b)
        silo_b.append(ball_a)

        # Recalculate the total entropy
        new_entropy = calculate_total_entropy(silos)

        # Keep the swap if entropy decreases; otherwise, undo it
        if new_entropy < current_entropy:
            current_entropy = new_entropy  # Accept the swap
        else:
            # Undo the swap
            silo_a.remove(ball_b)
            silo_b.remove(ball_a)
            silo_a.append(ball_a)
            silo_b.append(ball_b)

    return silos


if __name__ == "__main__":
    from generate_silos import generate_silos

    # Test settings
    NUM_SILOS = 5
    BALLS_PER_SILO = 10
    COLORS = ["red", "blue", "green", "yellow", "purple"]

    # Generate initial silos
    print("Original Silos:")
    silos = generate_silos(NUM_SILOS, BALLS_PER_SILO, COLORS)
    for i, silo in enumerate(silos, 1):
        print(f"Silo {i}: {silo}")

    # Run the MRSA filter
    print("\nApplying MRSA Filter...")
    filtered_silos = mrsa_filter(silos)
    for i, silo in enumerate(filtered_silos, 1):
        print(f"Silo {i}: {silo}")
