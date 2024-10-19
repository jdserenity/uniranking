### UniRank: A formula for ranking countries based on how many universities they have in the top 100 of the shanghai ranking list (weighted by how high they are on the list)

This is good for seeing how countries perform globablly against each other. I don't think it's very useful for picking a specific university though.

$S = \sum^n_{i=1} (101 - R_i)^p$
- $S$ is the country's total score
- $n$ is the number of universities from the country in the top 100
- $R_i$ is the Rank of the current university in the loop (i) (1st university gets 100 points, while 100th university gets 1 point)
- $p$ is a power factor to adjust the weight of universities higher on the list than others

I find that using a power factor of 0.1 achieves a good balance between the number of universities and their ranks.

This would be the output of the formula for each country (p=0.1):

1. United States: 56.65
2. China: 19.43
3. United Kingdom: 11.86
4. Switzerland: 7.09
5. Australia: 7.06
6. France: 6.04
7. Germany: 5.91
8. Canada: 4.42
9. Israel: 4.07
10. Japan: 3.03
11. Denmark: 2.88
12. Netherlands: 2.87
13. Sweden: 2.79
14. Singapore: 2.66
15. Belgium: 2.64
16. Norway: 1.40
17. South Korea: 1.31
18. Saudia Arabia: 1.26
19. Finland: 1.07