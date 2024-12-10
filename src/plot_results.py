import matplotlib.pyplot as plt

def plot_comparison_graph(sizes, results, save_path="graph.png"):
    """
    Plot a comparison graph showing processing times for all sorting methods.

    Args:
        sizes (list): List of problem sizes tested.
        results (dict): A dictionary containing processing times for each method.
        save_path (str): Path to save the graph file.
    """
    # Create the plot
    plt.figure(figsize=(10, 6))

    # Plot processing times
    plt.plot(sizes, results["Conventional"], label="Conventional Sorting", marker="o")
    plt.plot(sizes, results["Entropy-Based"], label="Entropy-Based Sorting", marker="o")
    plt.plot(sizes, results["Pairwise"], label="Pairwise Sorting", marker="o")
    plt.plot(sizes, results["MRSA Filter"], label="MRSA Filter", marker="o")

    # Add labels and title
    plt.xlabel("Problem Size (Number of Silos and Balls per Silo)")
    plt.ylabel("Processing Time (seconds)")
    plt.title("Sorting Performance Comparison")
    plt.legend()
    plt.grid(True)

    # Save the graph and notify
    plt.savefig(save_path)
    print(f"\nThe graph has been saved as '{save_path}' in the current folder.")
