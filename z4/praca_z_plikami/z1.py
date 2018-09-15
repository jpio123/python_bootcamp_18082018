import sys

print(sys.argv)

with open(sys.argv[1], encoding='utf-8') as f:
    for i, line in enumerate(f, start=1):
        print(i, line, end='')
        i += 1
