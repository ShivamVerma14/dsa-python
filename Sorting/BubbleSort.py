def bubble_sort(nums):
    n = len(nums)

    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break

def main():
    nums = [7, 3, 9, 12, 11]
    bubble_sort(nums)
    print(nums)

if __name__ == "__main__":
    main()