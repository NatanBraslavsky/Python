def fatorial(num):
    if num == 0 or num == 1:
        return 1
    return num * fatorial(num - 1)

print(fatorial(5)) 