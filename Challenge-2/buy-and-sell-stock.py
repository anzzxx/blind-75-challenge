

def buyandsell(prices):
    left,right=0,1
    profit=0

    while right<len(prices):
        if prices[right]>prices[left]:
            if prices[right]-prices[left]>profit:
                profit=prices[left]-prices[right]
        else:
            left=right
        right+=1

    return profit                


prices=[7,1,5,3,6,1]
print(buyandsell(prices))    