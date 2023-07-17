def count_smaller_elements(nums):
    result = []
    for i in range(len(nums)):
        count = 0
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                count += 1
        result.append(count)
    return result
nums = list(map(int, input().split()))
result = count_smaller_elements(nums)
print(result)
