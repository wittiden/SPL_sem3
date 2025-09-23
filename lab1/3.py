nums = [1,2,3,45,5,6,6,7,7,8,8, 8, 65,3,3]
print(nums)

for i in nums:
    if nums.count(i) > 2:
        while nums.count(i) != 0:
            nums.remove(i)
print(nums)
nums.sort(reverse=True)
print("Сортируем по убыванию: ", nums)