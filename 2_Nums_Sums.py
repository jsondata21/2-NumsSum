
def findPair(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(n):
            if nums[i] + nums[j] == target and nums[i] != nums[j]:
                return f"pair found {nums[i]} and {nums[j]}"


lista = [5,11, 8, 3, 5, 6, 2]
target = 10
print(findPair(lista, target))
