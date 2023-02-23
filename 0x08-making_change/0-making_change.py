'''Coins - DP
'''


def makeChange(coins, total):
    """ determine the fewest number of
       coins needed to meet a given amount total

    Args:
        coins (List: int): coin denominations
        total (int): targeted total
    """
    n = len(coins)
    if total == 0:
        return 0
    arr = [[0] * (total + 1) for _ in range(n + 1)]
    for i in range(total + 1):
        arr[0][i] = total + 1

    for j in range(1, n+1):
        for a in range(1, total + 1):
            if coins[j - 1] > a:
                arr[j][a] = arr[j - 1][a]
            else:
                arr[j][a] = min(arr[j][a - coins[j - 1]] + 1, arr[j - 1][a])
    if arr[n][total] > 0 and arr[n][total] < total + 1:
        return arr[n][total]
    return -1
