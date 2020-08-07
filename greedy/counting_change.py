def returnChange(change, denominations):
    result = []
    for coin in reversed(sorted(denominations)):
        if change > 0:
            while coin <= change:
                result.append(coin)
                change = change - coin
    if change > 0:
        raise Exception('Out of stock change: {0}'.format(change))
    return result


denominations = [100, 20, 5, 10, 2, 1, 50]
print(returnChange(38, denominations))
print(returnChange(41, denominations))
print(returnChange(39, denominations))
print(returnChange(57, denominations))
print(returnChange(50, denominations))
print(returnChange(100, denominations))


def returnChangeEn(change, denominations):
    result = []
    for coin in reversed(sorted(denominations)):
        if change > 0:
            while denominations[coin] > 0 and coin <= change:
                denominations[coin] = denominations[coin] - 1
                result.append(coin)
                change = change - coin
    if change > 0:
        raise Exception('Out of stock change: {0}'.format(change))
    return result


print('-----------------------')
denominations = {100: 2, 20: 0, 5: 1, 10: 3, 2: 2, 1: 2, 50: 1}
print(returnChangeEn(40, denominations))
denominations = {100: 2, 20: 1, 5: 1, 10: 3, 2: 2, 1: 2, 50: 1}
print(returnChangeEn(40, denominations))
denominations = {100: 2, 20: 0, 5: 1, 10: 1, 2: 10, 1: 10, 50: 1}
print(returnChangeEn(39, denominations))
