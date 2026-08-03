class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ''.join(filter(str.isalnum, s))
        reversed_s = cleaned_s[::-1] 
        return cleaned_s.lower() == reversed_s.lower()
