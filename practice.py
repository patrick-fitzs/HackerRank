def getMaxRequests(serverCapacity, incomingRequests, k):
    n = len(serverCapacity)

    handle_requests = sum(min(serverCapacity[i], incomingRequests[i]) for i in range(n))
    print(handle_requests)

    gains = [
        min(2 * serverCapacity[i], incomingRequests[i]) - min(serverCapacity[i], incomingRequests[i])
        for i in range(n)
    ]
    print(gains)
    bestgain = sorted(gains, reverse= True)[:k]
    print(bestgain)

    print(handle_requests+ sum(bestgain))

n=4
serverCapacity = [10,4,3,7]
incomingRequests=[3,10,4,5]

print(getMaxRequests(serverCapacity,incomingRequests,2))