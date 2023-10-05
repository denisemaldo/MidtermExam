'''
DENISE MALDO - BCS24

Write an algorithm, pseudocode, and code in Python to find the maximum element in a two-dimensional array. The array should 3 x 3 and student can provide their own given.


Instructions:
You are given a two-dimensional array, array, containing integer elements.

1. Write an algorithm to find the maximum element in the array.
2. Implement the algorithm in pseudocode.
3. Translate the pseudocode into Python code.
4. Test your code with the provided array.
5. Print the maximum element found in the array.
6. Ensure that your code is efficient and handles all possible edge cases.

ALGORITHM:

STEP 1: Initialize a variable max_element with the value at the first element (0,0) of the array.
STEP 2: Iterate through each element in the array.
STEP 3: If the current element is greater than max_element, update max_element with the current element.
STEP 4: After iterating through all elements, max_element will contain the maximum value.


PSEUDOCODE:
   - Initialize the maximum element with the first element in the array
   maxElement = array[0][0]

   - Loop through each row in the 2D array
   for each row in array:

       - Check each element in the row
       for each element in row:
           - If the current element is greater than the assumed maximum, update the maximum
           if element > maxElement:
               maxElement = element

   - Return the largest element found in the entire array
   return maxElement


'''


def maximum_element(array):
   max_element = array[0][0]
   for row in array:
       for element in row:
           if element > max_element:
               max_element = element
   return max_element

max_num = [
   [25, 24, 23],
   [1, 3, 6],
   [200, 500, 900]
]

result = maximum_element (max_num)
print("Maximum element :", result)