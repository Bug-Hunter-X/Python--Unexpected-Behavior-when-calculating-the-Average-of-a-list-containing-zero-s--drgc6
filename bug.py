def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}") #This will return 0

my_list_with_zero = [1,0,3,0,5]
average_zero = calculate_average(my_list_with_zero)
print(f"The average with zeros is: {average_zero}") #This will return the actual average