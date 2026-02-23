# Team points list
points = [20, 15, -5, 30, 25, -2, 18]

print("Original Points:")
print(points)

# Replace negative points with 0
for i in range(len(points)):
    if points[i] < 0:
        points[i] = 0

print("Updated Points:")
print(points)

# Sort leaderboard
points.sort(reverse=True)

print("Leaderboard:")
print(points)

# Winner and runner-up
print("Winner Points =", points[0])
print("Runner-up Points =", points[1])