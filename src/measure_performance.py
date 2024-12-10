import time
from generate_silos import generate_silos
from sorting_methods import conventional_sorting, entropy_based_sorting, pairwise_sorting

def measure_processing_time(sizes, colors):
    """
    Measure and record the processing time for each sorting method.

    Args:
        sizes (list): List of problem sizes (number of silos and balls per silo).
        colors (list): List of available ball colors.

    Returns:
        dict: A dictionary with processing times for each method.
    """
    results = {
        "Conventional": [],
        "Entropy-Based": [],
        "Pairwise": []
    }

    for size in sizes:
        print(f"Testing problem size: {size}x{size}")
        silos = generate_silos(size, size, colors)

        # Conventional Sorting
        start_time = time.time()
        conventional_sorting(silos)
        results["Conventional"].append(time.time() - start_time)

        # Entropy-Based Sorting
        start_time = time.time()
        entropy_based_sorting(silos, colors)
        results["Entropy-Based"].append(time.time() - start_time)

        # Pairwise Sorting
        silos_copy = [silo.copy() for silo in silos]  # Avoid modifying original silos
        start_time = time.time()
        pairwise_sorting(silos_copy)
        results["Pairwise"].append(time.time() - start_time)

    return results

if __name__ == "__main__":
    # Test parameters
    COLORS = ["red", "blue", "green", "yellow", "purple"]
    SIZES = [10, 20, 50, 100, 200]  # Problem sizes

    print("Measuring sorting performance...\n")
    results = measure_processing_time(SIZES, COLORS)

    # Display results
    print("\nPerformance Results:")
    for i, size in enumerate(SIZES):
        print(f"Size: {size}x{size}")
        print(f"  Conventional Sorting: {results['Conventional'][i]:.6f} seconds")
        print(f"  Entropy-Based Sorting: {results['Entropy-Based'][i]:.6f} seconds")
        print(f"  Pairwise Sorting: {results['Pairwise'][i]:.6f} seconds")
