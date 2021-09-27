import sys

ls = list(map(int, input()))

ls.sort(reverse=True)

print(''.join(map(str,ls)))