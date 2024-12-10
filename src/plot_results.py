import matplotlib.pyplot as plt

def plot_comparison_graph(sizes, results, save_path=None):
    """
    Plot a comparison graph showing processing times for all sorting methods.

    Args:
        sizes (list): List of problem sizes tested.
        results (dict): A dictionary containing processing times for each method.
        save_path (str, optional): File path to save the plot instead of displaying.
    """
    plt.figure(figsize=(10, 6))

    # Plot processing times for each method
    plt.plot(sizes, results["Conventional"], label="Conventional Sorting", marker="o")
    plt.plot(sizes, results["Entropy-Based"], label="Entropy-Based Sorting", marker="o")
    plt.plot(sizes, results["Pairwise"], label="Pairwise Sorting", marker="o")

    # Add labels and title
    plt.xlabel("Problem Size (Number of Silos and Balls per Silo)")
    plt.ylabel("Processing Time (seconds)")
    plt.title("Sorting Performance Comparison")
    plt.legend()
    plt.grid(True)

    # Save or show the graph
    if save_path:
        plt.savefig(save_path)
        print(f"Plot saved to {save_path}")
    else:
        print("Plot ready to display. Call plt.show() to view it.")
