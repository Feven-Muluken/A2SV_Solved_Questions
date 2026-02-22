class FrequencyTracker:
    from collections import Counter

    def __init__(self):
        self.num = Counter()
        self.freq = Counter()

    def add(self, number: int) -> None:
        if self.num[number] > 0:
            self.freq[self.num[number]] -= 1
        
        self.num[number] += 1
        self.freq[self.num[number]] += 1        

    def deleteOne(self, number: int) -> None:
        if self.num[number] > 0:
            self.freq[self.num[number]] -= 1

            self.num[number] -= 1

            if self.num[number] > 0:
                self.freq[self.num[number]] += 1    

        # return self.freq[freq]
    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)