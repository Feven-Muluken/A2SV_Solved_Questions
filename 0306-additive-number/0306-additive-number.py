class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i in range(1, n):
            for j in range(i+1, n):
                first, second = num[:i], num[i:j]
                
                # Skip invalid numbers with leading zeros
                if (len(first) > 1 and first[0] == '0') or (len(second) > 1 and second[0] == '0'):
                    continue
                
                a, b = int(first), int(second)
                k = j
                
                # Build sequence forward
                while k < n:
                    c = a + b
                    c_str = str(c)
                    
                    # If next part doesn't match, break
                    if not num.startswith(c_str, k):
                        break
                    
                    k += len(c_str)
                    a, b = b, c
                
                # If we consumed the whole string, it's valid
                if k == n:
                    return True
        
        return False
