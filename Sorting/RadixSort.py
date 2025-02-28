def radix_sort(nums):
    max_value = max(nums)
    exp = 1

    while max_value // exp > 0:
        buckets = [[] for _ in range(10)]
        for num in nums:
            index = (num // exp) % 10
            buckets[index].append(num)

        nums.clear()
        for bucket in buckets:
            nums.extend(bucket)

        exp *= 10

def main():
    nums = [170, 45, 75, 90, 802, 24, 2, 66]
    radix_sort(nums)
    print(nums)

if __name__ == "__main__":
    main()