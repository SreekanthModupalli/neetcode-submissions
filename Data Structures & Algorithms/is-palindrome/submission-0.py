class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_str = s.replace(" ", "").lower()
        sv = ""
        for i in valid_str:
            if i.isalnum():
                sv+=i
        reversed_text = sv[::-1]
        if reversed_text == sv:
            return True
        return False
    