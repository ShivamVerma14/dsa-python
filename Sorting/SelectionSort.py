def selection_sort(nums):
    n = len(nums)

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        if min_index != i:
            nums[i], nums[min_index] = nums[min_index], nums[i]

def main():
    nums = [7, 12, 9, 11, 3]
    selection_sort(nums)
    print(nums)

if __name__ == "__main__":
    main()