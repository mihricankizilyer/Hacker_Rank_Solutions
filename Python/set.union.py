


a = int(input())
a1 = set(map(int, input().split()))

b = int(input())
b1 = set(map(int, input().split()))

print(len(a1.union(b1)))

