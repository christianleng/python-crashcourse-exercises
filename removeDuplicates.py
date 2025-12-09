def removeDuplicates(nums):
    window = set()
    guardian = 0

    for n in range(len(nums)):
        if nums[n] not in window:
            window.add(nums[n])
            nums[guardian] = nums[n]
            guardian += 1

    for i in range(guardian):
        for j in range(guardian-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return guardian


nums = [0, 5, 3, 7, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = removeDuplicates(nums)
print(f"k = {k}")
print(f"nums = {nums[:k]}")
