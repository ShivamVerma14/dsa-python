def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1

    for j in range(low, high):
        if nums[low] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1

def quick_sort(nums, low=0, high=None):
    if not high:
        high = len(nums) - 1

    if low < high:
        pivot_index = partition(nums, low, high)
        quick_sort(nums, low, pivot_index - 1)
        quick_sort(nums, pivot_index + 1, high)

def main():
    nums = [11, 9, 12, 7, 3]
    quick_sort(nums)
    print(nums)

if __name__ == "__main__":
    main()