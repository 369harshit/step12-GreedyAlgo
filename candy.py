def min_candies(ratings):
    n = len(ratings)
    candies = [1] * n  # Initialize candies array with 1 candy for each child

    # Traverse from left to right, checking if the current child has a higher rating than the previous one
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Traverse from right to left, checking if the current child has a higher rating than the next one
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)

# Example input
ratings = [1, 0, 2]
result = min_candies(ratings)
print("Minimum number of candies needed:", result)
