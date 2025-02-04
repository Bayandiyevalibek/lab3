def solve(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads) // 2
    chickens = numheads - rabbits
    
    if rabbits >= 0 and chickens >= 0 and 2 * chickens + 4 * rabbits == numlegs:
        return chickens, rabbits
    else:
        return "ERROR"

heads = int(input())
legs = int(input())
print(solve(heads, legs))
