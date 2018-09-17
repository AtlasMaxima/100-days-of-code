
# 100 Days Of Code - Log
<a name="toc"></a>
### Table of Contents
|Day|Focus|Day|Focus|
|:---:|:-----:|:---:|:-----:|
|[Day 1](#day-1) - **09/05/18**|Balanced Parentheses & Stack|
|[Day 2](#day-2) - **09/06/18**|Stack & Queue & Kadane's Algorithm|
|[Day 3](#day-3) - **09/07/18**|Rotate 1D Array|
|[Day 4](#day-4) - **09/10/18**|First Unique Character|


----------
<a name="day-1"></a>
### Day 1: September 05, 2018

**Today's Focus**: Balanced Parentheses & Stack

**Details**:

Stack
1. What is a stack?
A stack follows the Last-in-First-out (LIFO) process order
2. How does LIFO work?
The new element added to the stack will be added to the end.
The element that is removed from the stack will always be the last one.
3. What is a stack in Python?
A stack in Python can be set to an array or a list.

Balanced Parentheses
1. Uses a stack

----------
<a name="day-2"></a>
### Day 2: September 06, 2018

**Today's Focus**: Stack & Queue & Kadane's Algorithm

**Details**:

Queue
1. What is a Queue?
A queue follows the First-in-First-out (FIFO) process order
2. How does FIFO work?
Enqueue is adding a new element to the back of the queue.
Dequeue is removing the first element of the queue.
For example, if we have a queue such that `Q = [5,13,8,2,10]`.
Enqueue will add the new element to `Q[len(Q)]` while dequeue will remove `Q[0]`.

3. What is a queue in Python?

4. What is an inefficient way of implementing a queue?
When we dequeue an element, there will be extra empty space.
For example, `Q = [5,13,8,2,10]` and dequeue `Q[0]` will leave `Q = ['', 13,8,2,10]`.
And if we further dequeue more elements such that `Q = ['','','',2,10]` will leave 3 extra empty spaces with no purpose. If we continue to enqueue such that `Q = ['','','',2,10,13,9]` will continue to have more empty and unused spaces.
[Another explanation](https://github.com/tim-hr/stuff/wiki/Time-complexity:-Queues)

5. What is an efficient way of implementing a queue?
Use a fixed-size array and two points of starting and ending positions.

6. What applications are queue useful for?
Breadth-first Search (BFS)

Kadane's Algorithm
1. What is Kadane's Algorithm used for ?
Kadane's algorithm is useful for finding the maximum subarray .


2. How does Kadane's Algorithm work?

[Table of Contents](#toc)

----------
<a name="day-3"></a>
### Day 3: September 07, 2018

**Today's Focus**: Rotate 1D Array

**Details**:
Given a list such that `list = [7,6,5,4,3,2,1]` and an integer `k = 3`, we want to rotate **3** times in the list.
The end output should be as follows:
1. `k = 0` - `list = [1,7,6,5,4,3,2]`
2. `k = 1` - `list = [2,1,7,6,5,4,3]`
3. `k = 2` - `list = [3,2,1,7,6,5,4]`
----------
<a name="day-4"></a>
### Day 4: September 10, 2018

**Today's Focus**: First Unique Character

**Details**:

[Table of Contents](#toc)

----------
<a name="day-5"></a>
### Day 5: September 11, 2018

**Today's Focus**: Merged Two Sorted Arrays

**Details**:
Given two sorted arrays of `m` and `n`, merge the `m` and `n` together whereas the length of `m` will be `m + n`.


[Table of Contents](#toc)

----------
<a name="day-6"></a>
### Day 6: September 12, 2018

**Today's Focus**: Time Complexity & Find the Median of Two Sorted Arrays

**Details**:
1. What is `O(log n)` time complexity?
`log n` in `O(log n)` is in base 2 given that computers store integers in binary 1 or 0. `x = log n` can also be seen as `b^x = n`. `O(log n)` represents the algorithm behavior as a 'quantity representing the power to which the base must be raise to produce a given number'. [What does the time compleixity o log n mean?](https://hackernoon.com/what-does-the-time-complexity-o-log-n-actually-mean-45f94bb5bfbf)

[Table of Contents](#toc)

----------
<a name="day-7"></a>
### Day 7: September 14, 2018

**Today's Focus**: Lowest Common Ancestors & Pre-Order Traversal

**Details**:
1. What is pre-order traversal?
Pre-order traversal is a way to traverse through a binary tree.
2. How does pre-order traversal work?
From root, it traverses to the left subtree, and then the right subtree. For example, given `tree = [A,B,C,D]` as input. And the output of pre-order traversal will be `output = [A, B, D, C]`.

[Table of Contents](#toc)

----------
<a name="day-8"></a>
### Day 8: September 16, 2018

**Today's Focus**: Integer to Binary

**Details**:
1. How can we convert an integer to binary using only bitwise operators?

[Table of Contents](#toc)

----------
<a name="day-9"></a>
### Day 9: September 17, 2018

**Today's Focus**: Sum of Two Integers & Binary to Integer

**Details**:
1. How can we add two integers together without using the basic arithmetic operands such as plus or minus? 

[Table of Contents](#toc)
