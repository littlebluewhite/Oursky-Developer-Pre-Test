def recur(n, cur=0):
    if n < 2:
        raise Exception("Invalid input")
    return cur + 1 - 1/n
