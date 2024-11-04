

names = ['John','Bob','kiran','arun','tarun']
print(names[:-1])
print(names)


numbers = [3,4,5,6,7,8,9,10]
max = numbers[0]
for number in numbers:
    if number>max:
        max = number
print(max)
# Write a function that takes a list of integers and returns the sum of all the elements.
def sum_of_elements(numbers):
    return sum(numbers)
numbers = [1,2,3,4,5,6,7,8,9,10]
result = sum_of_elements(numbers)
print("Sum of elements: ", result)

# Write a function that finds the largest and smallest elements in a list of integers.

def find_largest_and_smallest(numbers):
    if not numbers:
        return None, None  # Return None if the list is empty

    largest = smallest = numbers[0]  # Initialize both as the first element
    for num in numbers[1:]:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num

    return largest, smallest
