# Fun with algorithms

This repository was created during the study of [Introduction to Algorithms, Third Edition By Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest and Clifford Stein](https://mitpress.mit.edu/books/introduction-algorithms) book.

A well-written book with detailed implementation of algorithms.

## Use Python 3

~~~bash
pip install -r requirements.txt
~~~

## Sort algorithms comparison

Table of complexity of different sorting algorithms:

| Algorithm       | Worst case | Average case |
|-----------------|------------|--------------|
| Insertion Sort  | O(n^2)     | O(n^2)       |
| Merge Sort      | O(n*ln(n)) | O(n*ln(n))   |
| Heap Sort       | O(n*ln(n)) | O(n*ln(n))   |
| Quick Sort      | O(n^2)     | O(n*ln(n))   |
| Counting Sort   | O(k + n)   | O(k + n)     |
| Radix Sort      | O(d(k + n))| O(d(k + n))  |
| Bucket Sort     | O(n^2)     | O(n)         |

For plot beautiful performance chart run following command.

~~~sh
python sort/performance.py
~~~

![Sort performance chart](images/sort-performance.png)

## Matrix multiplication

- Naive matrix multiplication O(n^3)
- Strassen matrix multiplication O(n^2.81)

~~~sh
python matrix/performance.py
~~~

![Matrix multiplication performance](images/matrix-performance.png)

Useful links:

- [Performance comparison Naive and Strassen algorithms in Python, Java and C++](https://martin-thoma.com/strassen-algorithm-in-python-java-cpp/)
- [Matrix Operations in Python](http://www.mathwizurd.com/blog/2015/6/14/matrix-operations-in-python)
- [LU Decomposition in Python and NumPy](https://www.quantstart.com/articles/LU-Decomposition-in-Python-and-NumPy)
- [LU decomposition](https://rosettacode.org/wiki/LU_decomposition)
- [Inverting your very own matrix](http://www.vikparuchuri.com/blog/inverting-your-very-own-matrix/)

### Linked Lists

- [Implementing an Unordered List: Linked Lists](http://interactivepython.org/courselib/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html)

### Binary Tree

- [Binary Search Tree library in Python](http://www.laurentluce.com/posts/binary-search-tree-library-in-python/)
- [Search Tree Implementation](http://interactivepython.org/runestone/static/pythonds/Trees/SearchTreeImplementation.html)
- [Binary search tree](http://www.algolist.net/Data_structures/Binary_search_tree)

### Red Black Tree
