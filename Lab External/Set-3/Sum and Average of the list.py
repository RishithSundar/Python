def sum_and_average(numbers):
  total = sum(numbers)
  average = total / len(numbers)
  return total, average
my_list = [10, 20, 30, 40, 50]
total_sum, avg = sum_and_average(my_list)
print("Sum:", total_sum)
print("Average:", avg)
