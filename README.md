# **Sorting Balls**

## **Idea**

The **"Sorting Balls"** project benchmarks several algorithms for efficiently organizing colored balls into silos. Each method showcases a unique approach to reducing disorder, improving organization, and optimizing performance as the scale of the problem grows.  

The inspiration came, quite unexpectedly, during a moment of procrastination at the end of the semester. While watching YouTube, I saw a kid sorting balls and thought, *"Why not turn this into a problem worth solving?"*  

This led to the development of a series of approaches that are relevant to analysis in the following fundamental fields:

1. **Computer Science**  
   Sorting and entropy reduction are foundational challenges in data structures and algorithms. Optimal organization directly impacts search, clustering, and overall computational efficiency.  

2. **Logistics and Operations Research**  
   Efficient resource allocation, load balancing, and inventory management rely on minimizing disorder to reduce waste and improve performance.  

3. **Data Science and Machine Learning**  
   Problems like clustering, grouping, and classification require organizing data into meaningful categories. Reducing entropy in these systems often improves model performance and predictive accuracy.  

4. **Physics and Systems Theory**  
   The concept of entropy originates in physics, where it measures disorder. This project uses entropy as a heuristic for understanding and improving organization.  

5. **Game Theory and Heuristics**  
   Novel approaches like the **MRSA Filter** combine randomness with optimization, echoing strategies in game theory where iterative improvements lead to stable and optimal outcomes.  

6. **Artificial Intelligence**  
   Sorting and entropy-reducing techniques are directly applicable to AI, where self-organizing systems and heuristics solve complex real-world problems efficiently.

---

## **Why is this relevant?**

Sorting and organizing problems are foundational in computer science, logistics, and real-world applications. From efficiently allocating resources to balancing loads in systems or networks, understanding how to minimize "disorder" (or entropy) can lead to better performance and efficiency.  

Problems like these are analogous to challenges in data clustering, supply chain logistics, and even machine learning, where distributing elements into meaningful groups is key. By experimenting with both conventional and novel approaches, this project serves as a practical testing ground for exploring optimization strategies.

---

## **Overview**

This project compares and benchmarks four sorting methods for organizing colored balls into silos:

1. **Conventional Sorting** - Alphabetically sorts balls in each silo.  
2. **Entropy-Based Sorting** - Minimizes disorder (entropy) by redistributing balls by color.  
3. **Pairwise Sorting** - Balances silos iteratively by swapping adjacent balls.  
4. **Novel Approaches** - A testing ground for experimental and creative techniques designed to optimize sorting further.  

   -(i) **MRSA Filter (Minimum Random Swaps for Alignment)**:  
     A heuristic method that uses *trial-and-error* randomness to reduce system entropy.  
     - Balls are **randomly swapped** between silos.  
     - If a swap reduces the overall entropy (disorder), it's kept.  
     - If not, the swap is **undone**, ensuring only beneficial swaps persist.  
     - The process repeats iteratively, allowing silos to "self-organize" into a more balanced state over time.
     - The MRSA Filter is inspired by natural systems that stabilize through randomness, combining simplicity with effectiveness.
       It’s a novel approach to solving sorting problems where traditional methods might fall short.
   -(ii) ... More to come, pending inspiration and time... <3

---

## **Features**

- Generates silos filled with random colored balls.
- Measures and compares the performance of sorting algorithms.
- Saves a visual graph of the results.

---

## **Installation**

Clone the repository and install the dependencies:
```bash
git clone https://github.com/ericvaz/sortingballs.git
cd sortingballs
pip install -r requirements.txt
python src/main.py
```
<img src="image.png" alt="Sorting Balls" width="500"/>
