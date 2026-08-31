import heapq

class MedianFinder:

    def __init__(self):
        # max heap
        self.lower = []

        # min heap
        self.upper = []

    def addNum(self, num: int) -> None:
        # always add to lower
        heapq.heappush(self.lower, -num)
        
        # make sure all values in lower is less than or eq to every val in upper
        if self.upper and -self.lower[0] > self.upper[0]:
            value = -heapq.heappop(self.lower)
            heapq.heappush(self.upper, value)

        # rebalance
        if len(self.lower) > len(self.upper) + 1:
            value = -heapq.heappop(self.lower)
            heapq.heappush(self.upper, value)
        
        elif len(self.upper) > len(self.lower):
            value = heapq.heappop(self.upper)
            heapq.heappush(self.lower, -value)

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return float(-self.lower[0])
        
        return float((-self.lower[0] + self.upper[0] ) / 2.0)
        
# hint 1, lower half and upper half signals to me a heap? 
# min heap means the parent is minimum val between its two child nodes
# max heap means the parent is the maximum val between its two child nodes

# for the lower half we want it to be max heap so that the largest smaller half number is easily accessible, and for the upper half we want the min heap so that the smallest larger half is accessible, for calculations