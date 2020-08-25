

def atal_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1


nums = atal_range(1, 10)

for num in nums:
    print(num)

print(dir(nums))

#iterator should have next and iterable  __iter__, for more information watch great vide of comey on youtube.

print(nums)
# iter(objectname) will creat the next method for us. example in the video : i_num = iter(nums)

