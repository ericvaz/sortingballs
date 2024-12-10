import random

# Define the available ball colors
BALL_COLORS = ["red", "blue", "green", "yellow", "purple"]

def generate_silos(num_silos, balls_per_silo, colors):
    """
    Generate a list of silos filled with randomly selected ball colors.

    Args:
        num_silos (int): Number of silos to generate.
        balls_per_silo (int): Number of balls in each silo.
        colors (list): List of ball colors to choose from.

    Returns:
        list: A list of silos, where each silo contains a list of ball colors.
    """
    silos = []
    for _ in range(num_silos):
        silo = [random.choice(colors) for _ in range(balls_per_silo)]
        silos.append(silo)
    return silos

if __name__ == "__main__":
    # Settings for generating silos
    NUM_SILOS = 10
    BALLS_PER_SILO = 10

    # Generate silos with random balls
    silos = generate_silos(NUM_SILOS, BALLS_PER_SILO, BALL_COLORS)

    # Display the generated silos
    print("Randomly Generated Silos of Balls:")
    for idx, silo in enumerate(silos, start=1):
        print(f"Silo {idx}: {silo}")
