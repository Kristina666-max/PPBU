n = int(input())
a = list(map(int, input().split()))
c = 0
for i in range(1, n):
    if a[i] < a[c]:
    c = i
    print(i)
    






