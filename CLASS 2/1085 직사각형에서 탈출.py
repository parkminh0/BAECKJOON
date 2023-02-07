x, y, w, h = map(int, input().split())

V = min((w-x), x)
H = min((h-y), y)

print(min(V, H))