def helper(number):
    return abs(number - 1)

countries = ["Germany", "Mexico", "Canada"]
numbers = [33, 44, 11, 2, 0, -344]

numbers.sort(reverse = True)
numbers.sort(key = helper)
countries.sort()

print(countries)
print(numbers)