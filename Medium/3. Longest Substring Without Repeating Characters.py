class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            st = ''
            m = 0
            if len(s) == 1:
                return 1
            for i in s:
                if len(st)> m:
                    m = len(st)
                else:
                    m = m
                if i not in st:
                    st = st+i
                else:
                    while i in st:
                        st = st[1:]
                        n = len(st)
                    st = st+i
        #         print(st)
                if len(st)> m:
                    m = len(st)
            return m
