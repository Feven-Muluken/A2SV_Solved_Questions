class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = []
        for i in cpdomains:
            a = i.split(' ')
            b = a[1].split('.')
            for l in range(len(b)):
                all_doms = a[0] + ' ' + ".".join(b[l:]) 
                ans.append(all_doms)
                l += 1

        counts = {}
        for web in ans:
            count, domain = web.split()
            count = int(count)
            counts[domain] = counts.get(domain, 0) + count
        answer = [f'{total} {dom}' for dom, total in counts.items()]
        return answer