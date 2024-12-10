import os
from generate_silos import generate_silos
from sorting_methods import conventional_sorting, entropy_based_sorting, pairwise_sorting
from measure_performance import measure_processing_time
from plot_results import plot_comparison_graph
import matplotlib.pyplot as plt

def main():
    # Project settings
    COLORS = ["red", "blue", "green", "yellow", "purple"]
    SIZES = [10, 20, 50, 100, 200, 300, 400, 500]  # Problem sizes
    OUTPUT_DIR = "output"
    PLOT_PATH = os.path.join(OUTPUT_DIR, "performance_comparison.png")
    
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Measure performance for sorting methods
    print("Measuring sorting performance...\n")
    results = measure_processing_time(SIZES, COLORS)

    # Print results
    print("\nPerformance Results:")
    for i, size in enumerate(SIZES):
        print(f"Size: {size}x{size}")
        print(f"  Conventional Sorting: {results['Conventional'][i]:.6f} seconds")
        print(f"  Entropy-Based Sorting: {results['Entropy-Based'][i]:.6f} seconds")
        print(f"  Pairwise Sorting: {results['Pairwise'][i]:.6f} seconds")

    # Generate comparison graph
    print("\nGenerating comparison graph...")
    plot_comparison_graph(SIZES, results, save_path=PLOT_PATH)
    print(f"Graph saved to {PLOT_PATH}")

    print("\nDone. Check the output directory for results.")

if __name__ == "__main__":
    main()
