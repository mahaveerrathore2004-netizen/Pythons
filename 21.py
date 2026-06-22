N = int(input())
X = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
max_balloon = 0
for i in range(N):
    for j in range(i + 1, n):
        total_cost = B[i] + B[j]
        if total_cost <= X:
            total_balloons = A[i] + A[j]
            if total_balloons > max_balloon:
                max_balloon = total_balloons
print(max_balloon)