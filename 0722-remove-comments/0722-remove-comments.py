class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        new_list = []
        block_string = False
        new_line = []
        for i in source:
            if not block_string:
                new_line = []
            j = 0
            while j < len(i):
                if not block_string:
                    if j+1 < len(i) and i[j:j+2] == '/*':
                        block_string = True
                        j+=1
                    elif j+1 < len(i) and i[j:j+2] == '//':
                        break
                    else: 
                        new_line.append(i[j])
                else:
                    if i[j:j+2] == '*/':
                        block_string = False
                        j+=1
                j+=1   
            if not block_string and new_line:
                new_list.append("".join(new_line))
        return new_list