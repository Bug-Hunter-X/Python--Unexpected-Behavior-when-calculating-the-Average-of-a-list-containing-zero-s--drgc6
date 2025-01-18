def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    if total == 0:
        return 0 # Handle case where all numbers are zero
    return total / len(numbers)

my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_list_with_zero = [1,0,3,0,5]
average_zero = calculate_average(my_list_with_zero)
print(f"The average with zeros is: {average_zero}")

my_all_zeros = [0,0,0,0,0]
average_all_zeros = calculate_average(my_all_zeros)
print(f"The average of all zeros is: {average_all_zeros}"