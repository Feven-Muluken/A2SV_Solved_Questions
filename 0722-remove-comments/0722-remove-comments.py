# class Solution:
#     def removeComments(self, source: List[str]) -> List[str]:
#         new_list = []
#         block_string = False
#         new_line = []
#         for i in source:
#             if not block_string:
#                 new_line = []
#             j = 0
#             while j < len(i)-1:
#                 if not block_string:
#                     if source[j:j+2] == '/*':
#                         block_string = True
#                         j+=1
#                     elif source[j:j+2] == '//':
#                         break
#                     else: 
#                         new_line.append(i[j])
#                 else:
#                     if source[j:j+2] == '*/':
#                         block_string = False
#                         j+=1
#                 j+=1   
#             if not block_string and new_line:
#                 new_list.append("".join(new_line))
#         return new_list
def removeComments(source):
    result = []
    in_block = False
    new_line = []
    
    for line in source:
        if not in_block:
            new_line = []
        i = 0
        while i < len(line):
            if not in_block:
                if i + 1 < len(line) and line[i:i+2] == '/*':
                    in_block = True
                    i += 1
                elif i + 1 < len(line) and line[i:i+2] == '//':
                    break
                else:
                    new_line.append(line[i])
            else:
                if i + 1 < len(line) and line[i:i+2] == '*/':
                    in_block = False
                    i += 1
            i += 1
        
        if not in_block and new_line:
            result.append("".join(new_line))
            
    return result
