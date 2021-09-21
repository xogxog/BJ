x,y,w,h = map(int, input().split())

# my_min = 1000

w_x = w-x
h_y = h-y

print(min(x,y,w_x,h_y))

