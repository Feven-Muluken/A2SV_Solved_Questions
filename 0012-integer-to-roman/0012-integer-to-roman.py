class Solution:
    def intToRoman(self, num: int) -> str:
        dicti = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        ans = ''
        for i, j in dicti.items():

            if i > num:
                continue
            roman = num//i
            ans += (j * roman)
            num = num % i
        return ans