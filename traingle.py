def minimumTotal(triangle):
    # Start from the second-to-last row and work upwards
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            # Update the current element with the minimum path sum
            triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])

    # The top element contains the minimum path sum
    return triangle[0][0]
