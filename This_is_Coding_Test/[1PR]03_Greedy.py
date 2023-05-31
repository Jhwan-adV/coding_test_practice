# Greedy 1. Given the input, write a program that returns the least number of coins

def get_least_coin(change=500): # Greedy 1 Answer

    coins = [500, 100, 50, 10]
    count = 0

    for coin in coins:
        print(f'current change; {change} | current coin: {coin}')
        while change >= coin:
            c, change = divmod(change, coin)
            print(c, change)
            count += c

    return count


print(get_least_coin(1240))


# Greedy 2. With the given N-item array, add the largest numbers up to K times resulting the whole process M times

# Different index => Different Number
def biggest_number(array, m=8, k=3):
    array.sort() # Sort - Ascending
    result = 0

    while m != 0:
        for i in range(k):
            result += array[-1]
            m -= 1
            if m == 0:
                break
        result += array[-2]
        m -= 1

    return result


print(biggest_number([5,2,3,4]))


def biggest_number_2(array, m=8, k=3):
    array.sort()

    times_largest = int(m // (k+1) * k) + (m % (k+1))
    times_sec_largest = m - times_largest

    return (array[-1] * times_largest) + (array[-2] * times_sec_largest)


print(biggest_number_2([5,2,3,4]))


# Greedy 3. Number Cards - Pick a card of the largest number from the array.

def number_cards(rows=5, cols=4):
    import numpy as np
    array = np.random.randint(1, 10000, size=(rows, cols))
    print(array)

    result = 0
    for row in array:
        tmp = min(row)
        result = max(tmp, result)

        # if tmp > result:
        #    result = tmp

    return result


print(number_cards())


# Greedy 4. Until 1 - Given N and K, find the least number to make N=1
# 1을 빼는 것보다 n으로 나누는 것이 항상 효율적이라는 걸 입증할 필요가 있음
def until_one(n=25, k=3):
    count = 0

    while n != 1:
        if n % k != 0:
            n -= 1
        else:
            n //= k
        count += 1

    return count


def until_one_2(n=100000020, k=354):
    result = 0
    while True:
        target = (n // k) * k # The nearest number

        while n != target:
            n -= 1
            result += 1

        if n < k:
            break

        target //= k
        result += 1
        n = target

    result += n-1

    return result


print(until_one(100000020, 354))
print(until_one_2())


