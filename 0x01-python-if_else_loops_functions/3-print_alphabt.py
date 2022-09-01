#!/usr/bin/python3
for alpha in range(ord('a'), ord('z') + 1):
    if alpha == ord('e') or alpha == ord('q'):
        continue
    print("{:c}".format(alpha), end="")
