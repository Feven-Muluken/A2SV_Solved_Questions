class Solution:
    def decodeString(self, s):
        stack = []
        curr_num = 0
        curr_str = ''
        for char in s:
            if char == '[':
                stack.append((curr_str, curr_num))
                curr_str = ''
                curr_num = 0
            elif char == ']':
                prev_str, num = stack.pop()
                curr_str = prev_str + num * curr_str
            elif char.isdigit():
                curr_num = curr_num * 10 + int(char)
            else:
                curr_str += char
        return curr_str