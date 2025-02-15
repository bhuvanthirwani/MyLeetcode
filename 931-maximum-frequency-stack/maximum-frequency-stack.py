class FreqStack:

    def __init__(self):
        self.max_freq = 0
        self.freq_map={}
        self.freq={}

    def push(self, val: int) -> None:
        if val in self.freq:
            val_freq = self.freq[val]
        else:
            val_freq = 0
        self.max_freq=max(self.max_freq, val_freq+1)
        self.freq[val] = val_freq + 1
        if self.freq[val] in self.freq_map:
            self.freq_map[self.freq[val]].append(val)
        else:
            self.freq_map[self.freq[val]] = [val]


    def pop(self) -> int:
        max_ele = self.freq_map[self.max_freq].pop()
        self.freq[max_ele] -= 1
        if not self.freq_map[self.max_freq]:
            self.max_freq -= 1
        return max_ele
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()