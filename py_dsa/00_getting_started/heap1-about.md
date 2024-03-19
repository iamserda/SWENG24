# Heaps

## README for Heaps

Heaps are a special tree-based data structure that satisfy the heap property: in a max heap, for any given node C, if P is a parent node of C, then the key (the value) of P is greater than or equal to the key of C. In a min heap, the key of P is less than or equal to the key of C. The node at the "top" of the heap (the root node) contains the largest key (max heap) or the smallest key (min heap). Heaps are commonly used to implement priority queues, where the node with the highest priority is always at the front.

## Key Operations

- **Insertion**: O(log n), as elements need to be compared upwards along the path from the inserted node to the root.
- **Deletion (Removing the root)**: O(log n), due to the need to reheapify the tree.
- **Find Max/Min**: O(1), as the max/min element is always at the root.
- **Search**: O(n), as heaps are not ordered and a full traversal is necessary to find an element.

## Use Cases

- Implementing priority queues.
- Sorting elements using heap sort.
- Finding the kth largest/smallest element in a collection.

## Python Implementation (Min Heap Example)

Python's `heapq` module provides an implementation of the heap queue algorithm, also known as the priority queue algorithm. Below is a simple example demonstrating how to use `heapq` to create a min heap:

```python
import heapq

# Create a min heap
min_heap = []
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 4)

# View the smallest element
print("Smallest element:", min_heap[0])  # Output: Smallest element: 1

# Remove and return the smallest element
print("Removed element:", heapq.heappop(min_heap))  # Output: Removed element: 1

# After removing the smallest element
print("Smallest element now:", min_heap[0])  # Output: Smallest element now: 3

# If you need a max heap, you can insert and pop elements with their sign inverted or use a custom class to invert the comparison.
```

## Further Steps

- Experiment with implementing a max heap by inverting the values during insertions and deletions.
- Explore heap sort algorithm and its implementation using heaps.
- Implement a priority queue for more complex scheduling tasks.

Heaps are a powerful tool for managing data in applications where time efficiency of access, insertion, and deletion (especially for the root element) is critical, such as in priority queues. Next Up Graphs?