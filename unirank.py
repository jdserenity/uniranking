us_rankings = [1, 2, 3, 5, 7, 8, 9, 10, 11, 12, 14, 15, 17, 18, 19, 20, 23, 29, 30, 31, 33, 35, 36, 39, 46, 49, 54, 56, 59, 62, 64, 65, 66, 76, 84, 87, 93, 100]
uk_rankings = [4, 6, 16, 25, 40, 52, 53, 97]
fr_rankings = [13, 34, 41, 60]
swi_rankings = [21, 55, 58, 67, 95]
chi_rankings = [22, 24, 27, 38, 42, 50, 69, 72, 79, 83, 89, 94, 96, 98]
can_rankings = [26, 48, 74]
jap_rankings = [28, 45]
den_rankings = [32, 80]
aus_rankings = [37, 63, 75, 77, 82]
swe_rankings = [43, 88]
ger_rankings = [44, 47, 51, 61]
net_rankings = [57, 70]
sin_rankings = [68, 92]
isr_rankings = [71, 81, 85]
nor_rankings = [73]
bel_rankings = [78, 90]
kor_rankings = [86]
sau_rankings = [91]
fin_rankings = [99]

sum = 0

for ranking in fin_rankings:
    sum += (101 - ranking)**0.1

print("{:.2f}".format(sum))