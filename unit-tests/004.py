'''Exercise 3
The implementation of the max_min_diff() function is given:

Modify the implementation of the max_min_diff() function. 
By using the assert statement inside this function, 
add the ability to check the length of the numbers argument before returning the result. 
If the length of the numbers object is 0 raise the AssertionError without any message. 
Otherwise, return the correct result.

In response call max_min_diff() function passing an empty list.

'''
def max_min_diff(numbers):
    """
    Calculates the difference between the maximum and minimum number
    in the given list.
 
    :param numbers: A list of numbers.
    :return: The difference between the maximum and minimum number
    in the list.
    """
    assert len(numbers) > 0


    return max(numbers) - min(numbers)


max_min_diff([])