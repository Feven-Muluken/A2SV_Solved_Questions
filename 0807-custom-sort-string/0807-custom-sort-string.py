class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # from collections import Counter
        # s_count = Counter(s)
        # order_count = Counter(order)
        orderlist = []
        for i in order:
            if i in s: 
                orderlist.append(i)
            if s.count(i) > order.count(i):
                orderlist.append((s.count(i) - order.count(i))*i)
        for j in s:
            if j not in order:
                orderlist.append(j)
        return "".join(orderlist)