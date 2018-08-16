import math

def dcf(cash, growthRate, susGrowthRate, discountRate, year)
    total = 0
    for i in range(1, year)
        total += (cash * math.pow((1 + riseRate), i))/math.pow((1 + discountRate), i)

    total = (total * (1 + susGrowthRate) * (1 + discountRate))/(discountRate - susGrowthRate)
    total  = total/math.pow((1 + discountRate), year + 1)

    print(total)
