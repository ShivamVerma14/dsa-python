def merge(nums, low, mid, high):
    i, j = low, mid + 1
    temp = []

    while i <= mid and j <= high:
        if nums[i] <= nums[j]:
            temp.append(nums[i])
            i += 1
        else:
            temp.append(nums[j])
            j += 1
    
    while i <= mid:
        temp.append(nums[i])
        i += 1
    
    while j <= high:
        temp.append(nums[j])
        j += 1

    nums[low:high + 1] = temp

def merge_sort(nums, low=0, high=None):
    if high is None:
        high = len(nums) - 1

    if low < high:
        mid = (low + high) // 2
        merge_sort(nums, low, mid)
        merge_sort(nums, mid + 1, high)
        merge(nums, low, mid, high)

def main():
    nums = [12, 8, 9, 3, 11, 5, 4]
    merge_sort(nums)
    print(nums)

if __name__ == "__main__":
    main()