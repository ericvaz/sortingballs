from generate_silos import generate_silos
from sorting_methods import conventional_sorting, entropy_based_sorting, pairwise_sorting
from novel_methods import mrsa_filter
from measure_performance import measure_processing_time
from plot_results import plot_comparison_graph
import time

def main():
    # Settings
    COLORS = ["red", "blue", "green", "yellow", "purple"]
    SIZES = [10, 20, 50, 100, 200]
    RESULTS = {"Conventional": [], "Entropy-Based": [], "Pairwise": [], "MRSA Filter": []}

    print("Measuring sorting performance...\n")
    for size in SIZES:
        print(f"Testing size: {size}x{size}")
        silos = generate_silos(size, size, COLORS)

        # Conventional Sorting
        start_time = time.time()
        conventional_sorting(silos)
        RESULTS["Conventional"].append(time.time() - start_time)

        # Entropy-Based Sorting
        start_time = time.time()
        entropy_based_sorting(silos, COLORS)
        RESULTS["Entropy-Based"].append(time.time() - start_time)

        # Pairwise Sorting
        start_time = time.time()
        pairwise_sorting([silo.copy() for silo in silos])
        RESULTS["Pairwise"].append(time.time() - start_time)

        # MRSA Filter
        start_time = time.time()
        mrsa_filter([silo.copy() for silo in silos])
        RESULTS["MRSA Filter"].append(time.time() - start_time)

    # Save and show the graph
    plot_comparison_graph(SIZES, RESULTS, save_path="graph.png")

if __name__ == "__main__":
    main()
