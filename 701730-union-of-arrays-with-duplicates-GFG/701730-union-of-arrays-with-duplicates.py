class Solution:    
    def findUnion(self, a, b):
        # code here
        return set(a + b)
        # new_array = []
        # for i in a:
        #     if i in new_array:
        #         continue
        #     new_array.append(i)
        # for j in b:
        #     if j in new_array:
        #         continue
        #     new_array.append(j)
            
        # return sorted(new_array)