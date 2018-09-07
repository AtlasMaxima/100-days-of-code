
# 100 Days Of Code - Log
<a name="toc"></a>
### Table of Contents
|Day|Focus|Day|Focus|
|:---:|:-----:|:---:|:-----:|
|[Day 1](#day-1) - **09/05/18**|Balanced Parentheses & Stack|
|[Day 2](#day-2) - **09/06/18**|Stack & Queue & Kadane's Algorithm|


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
2. How does Kadane's Algorithm work?

[Table of Contents](#toc)

----------
<a name="day-3"></a>
### Day 3: September 07, 2018

**Today's Focus**: Stack & Queue & Kadane's Algorithm

**Details**:



[Table of Contents](#toc)
