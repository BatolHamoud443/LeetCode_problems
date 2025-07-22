import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r'[^a-z0-9]', '', s.lower())
        if cleaned[:] == cleaned[::-1]:
            return True
        else:
            return False
