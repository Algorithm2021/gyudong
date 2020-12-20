
def cycle(N):
    first, second = divmod(N, 10)
    result = first+second

    result = (second*10)+(result%10)

    return result


N = int(input())
result = N

i = 0
while True:
    i += 1

    result = cycle(result)
    if result==N:
        break

print(i)
