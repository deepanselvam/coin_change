def main():
    size = int(input())
    arr = list(map(int, input().split()))
    amount = int(input())
    arr.sort()
    sum = 0
    count = 0
    zero = 0
    premax = 0
    max = max(arr)
    while sum < amount and zero < len(arr) and max != 0:
        max = max(arr)
        if sum + max <= amount:
            count += 1
            sum += max
        else:
            index = arr.index(max)
            arr[index] = 0
            zero += 1
    if sum == amount:
        print(count)
    else:
        print(-1)

if __name__ == "__main__":
    main()
