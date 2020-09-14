#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
    The conditional statement of the while loop suggests a time complexity of 
    O(n^3) but the iterating variable is squared at every iteration.  The rate at which the iterating variable grows compared to the initial growth of the declared iterable space causes this algorithm to run in linear time.

b) O(n log n)
    This algorithm will always loop through n amount of iterations in it's for loop and it's while loop iterates less than n times because the iterating variable doubles at each iteration.

c) O(n)
    This algorithm runs in linear time as it will only call itself once in each call and the variable used in it's base case decrements linearly until returning back down the callstack.

## Exercise II

A binary search with a queue would be best in this situation.  

We could decide to iterate through n amount of floors and test if the egg would break at each level, making the algorithm O(n) worst case.

A binary search would allow for a runtime of O(log n)
runnning a binary search would cut down the search space at half each iteration and a queue would allow us to track the result at each floor we test.
