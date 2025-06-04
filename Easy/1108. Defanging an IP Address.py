class Solution:
    def defangIPaddr(self, address: str) -> str:
        s = ''
        for i in range(len(address)):
            if address[i] != '.':
                s = s+address[i]
            else:
                s = s + '[.]'
        return s
