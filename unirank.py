us_rankings = [1, 2, 3, 5, 7, 8, 9, 10, 11, 12, 14, 15, 17, 18, 19, 20, 23, 29, 30, 31, 33, 35, 36, 39, 46, 49, 54, 56, 59, 62, 64, 65, 66, 76, 84, 87, 93, 100]
uk_rankings = [4, 6, 16, 25, 40, 52, 53, 97]
fr_rankings = [13, 34, 41, 60]
swi_rankings = [21, 55, 58, 67, 95]

sum = 0

for ranking in us_rankings:
    sum += (101 - ranking)**0.1

print(sum)