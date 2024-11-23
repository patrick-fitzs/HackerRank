candles = [3,2,1,3]

def birthdayCakeCandles(candles):
    numOfTall = 0
    tallestCandle = candles[0]
    for i in range(len(candles)):
        if candles[i]>tallestCandle:
            tallestCandle = candles[i]
        elif candles[i] == tallestCandle:
            numOfTall+=1

    return numOfTall

print(birthdayCakeCandles(candles))
x ="test"
