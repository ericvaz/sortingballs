import matplotlib.pyplot as plt
import os

def plot_comparison_graph(sizes, results):
    """
    Plot a comparison graph showing processing times for all sorting methods.
    Save the graph to the user's desktop for convenience.

    Args:
        sizes (list): List of problem sizes tested.
        results (dict): A dictionary containing processing times for each method.
    """
    # Find the desktop directory
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    save_path = os.path.join(desktop_path, "performance_comparison.png")
    
    # Create the plot
    plt.figure(figsize=(10, 6))

    plt.plot(sizes, results["Conventional"], label="Conventional Sorting", marker="o")
    plt.plot(sizes, results["Entropy-Based"], label="Entropy-Based Sorting", marker="o")
    plt.plot(sizes, results["Pairwise"], label="Pairwise Sorting", marker="o")

    plt.xlabel("Problem Size (Number of Silos and Balls per Silo)")
    plt.ylabel("Processing Time (seconds)")
    plt.title("Sorting Performance Comparison")
    plt.legend()
    plt.grid(True)

    # Save the graph to the desktop
    plt.savefig(save_path)
    print(f"\nFor your convenience, the graph has been saved on the Desktop: {save_path}")
