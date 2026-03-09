class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        boolian = False
        for i in ransomNote:
            if i in magazine and ransomNote.count(i) <= magazine.count(i):
                boolian = True
            else:
                return False
        return boolian