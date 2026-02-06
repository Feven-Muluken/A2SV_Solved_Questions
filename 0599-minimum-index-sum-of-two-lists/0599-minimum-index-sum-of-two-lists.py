class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        strind = dict()
        newlist = []
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    strind[list1[i]] = i+j
        newlist = [x for x in strind if strind[x] == min(strind.values())]
        return newlist
        # return [min(strind, key=strind.get)]
                    
                