# 🔍 Binary Search Algorithm

Binary Search is a highly efficient "divide and conquer" search algorithm used to find the position of a target value within a **sorted** array. 

Unlike a linear search that checks every single element one by one, binary search works by repeatedly dividing the search space in half. It compares the target value to the middle element of the array; if they are unequal, the half in which the target cannot lie is eliminated, and the search continues on the remaining half.

---

## ⚠️ Important Prerequisite
**The array must be sorted** before applying Binary Search. If the data is unsorted, you must sort it first (e.g., using Merge Sort or Quick Sort) or default to a Linear Search.

---

## ⏱️ Complexity

* **Time Complexity:** * **Best Case:** $O(1)$ (The target is the very first middle element chosen)
  * **Average/Worst Case:** $O(\log n)$ (The search space is halved every step)
* **Space Complexity:** * **Iterative approach:** $O(1)$ (Requires no extra memory)
  * **Recursive approach:** $O(\log n)$ (Memory required for the function call stack)

---

