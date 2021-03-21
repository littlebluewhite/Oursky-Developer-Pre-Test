# Oursky-Developer-Pre-Test
### Question 1
Write a function that takes two arrays as input, each array contains a list of A-Z; Your program should return True if the 2nd array is a subset of 1st array, or False if not.

For example:

isSubset([A,B,C,D,E], [A,E,D]) = true

isSubset([A,B,C,D,E], [A,D,Z]) = false

isSubset([A,D,E], [A,A,D,E]) = true

Please explain the computational complexity of your answer in Big-O notation, i.e. O(log n) or O(n ^2)?

### Question 2
Design and implement a data structure for cache.

●get(key) - Get the value of the key if the key exists in the cache, otherwise return -1

●put(key, value, weight) - Set or insert the value, when the cache reaches its capacity, it should invalidate the least scored key. The score is calculated as:

  ○when current_time != last_access_time: weight / ln(current_time - last_access_time)
  
  ○else: weight / -100
  
Your data structure should be optimized for the computational complexity of get(key) i.e. Average case for computational complexity of get(key) could be O(1).

In your code, you can assume common data structure such as array, different type of list, hash table are available.

Please explain the computational complexity of get(key) and put(...) in Big-O notation.

### Question 3
Please understand the following program
```
function recur(n, cur) {
  if (!cur) {
   cur = 0;
  }
  if (n < 2) {
throw new Error('Invalid input');
  }
  if (n === 2) {
   return 1 / n + cur;
  }
  return recur(n - 1, cur + 1 / (n * (n -1)));
}
```
● Write a program doing the same calculation without recursion.
