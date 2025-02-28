def counting_sort(nums):
    max_value = max(nums)
    min_value = min(nums)

    range_of_values = max_value - min_value + 1
    count = [0] * range_of_values
    
    for num in nums:
        count[num - min_value] += 1
    
    index = 0
    for i in range(range_of_values):
        while count[i] > 0:
            nums[index] = i + min_value
            index += 1
            count[i] -= 1

def main():
    nums = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
    counting_sort(nums)
    print(nums)

if __name__ == "__main__":
    main()