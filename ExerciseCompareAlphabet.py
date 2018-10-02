s = "acebdfz"

long = ""
solution = ""
pre = "a"
# smallest character

for c in s:
    #compare third character to s
    if c > pre:
        solution = solution+c

    else:
