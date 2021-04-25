input_NX = input().split()
N = int(input_NX[0])
X = float(input_NX[1])

ans = -1
Xi = 0.0
for i in range(N):
    d = input().split()
    Vi = float(d[0])
    Pi = float(d[1])/100
    Xi += Vi * Pi

    if (X < Xi) & (ans == -1):
        ans = i+1

print(ans)
