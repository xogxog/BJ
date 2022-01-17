a = int(input())
x = int(input())
b = int(input())
y = int(input())
T = int(input())

print(a+ ((x*(T-30))*21 if max(T-30,0) else 0), b+ ((y*(T-45))*21 if max(T-45,0) else 0))