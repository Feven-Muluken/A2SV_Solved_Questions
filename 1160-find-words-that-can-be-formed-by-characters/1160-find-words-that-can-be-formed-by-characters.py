class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        n = []
        flag = False
        sum1 = 0
        for i in words:
            flag = all(j in chars and chars.count(j) >= i.count(j) for j in i)
            if flag == True:
                n.append(len(i))
            sum1 = sum(m for m in n)
        return sum1