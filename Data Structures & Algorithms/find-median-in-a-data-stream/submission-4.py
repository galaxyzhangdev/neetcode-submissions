class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)

    def findMedian(self) -> float:
        self.data.sort()
        l = len(self.data)
        mid = l // 2
        if l % 2 == 0:
            return (self.data[mid] + self.data[mid-1])/2
        if l % 2 == 1:
            return self.data[mid]

        