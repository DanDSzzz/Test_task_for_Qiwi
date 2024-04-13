# Дан массив целых чисел. Найдите непрерывный подмассив (содержащий хотя бы одно число), который имеет наибольшую сумму и верните его сумму.
# Подмассив это непрерывная часть массива.
# Пример:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] имеет наибольшее значение суммы равное 6.
# Функция для нахождения максимальной суммы непрерывного подмассива
def max_subarray_sum(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Пример массива
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Вызов функции
output = max_subarray_sum(nums)
print(output)