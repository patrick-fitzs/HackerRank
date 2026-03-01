

def getMaxRequests(serverCapacity, incomingRequests, k):
    n = len(serverCapacity)

    handle_requests = sum(min(serverCapacity[i], incomingRequests[i]) for i in range(n))
    print("Starting handle requests: ", handle_requests)

    newServ = [2* serverCapacity[i] for i in range(n)]
    newReq = sum(min(newServ[i], incomingRequests[i]) for i in range(n))
    gain = [min(newServ[i], incomingRequests[i]) - min(serverCapacity[i], incomingRequests[i]) for i in range(n)]
    bestgainers = sorted(gain)[k:]
    return "Handle requests after 'k' servers doubles ", handle_requests+sum(bestgainers)



n=4
serverCapacity = [10,4,3,3,7]
incomingRequests=[3,4,10,4,5]

print(getMaxRequests(serverCapacity,incomingRequests,2))