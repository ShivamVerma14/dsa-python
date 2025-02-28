def insertion_sort(nums):
    n = len(nums)

    for i in range(1, n):
        element = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > element:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = element

def main():
    nums = [7, 12, 9, 11, 3]
    insertion_sort(nums)
    print(nums)

if __name__ == "__main__":
    main()