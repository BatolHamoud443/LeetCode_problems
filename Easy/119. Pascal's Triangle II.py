class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        numRows = rowIndex + 1
        if numRows == 1:
            return [1]
        if numRows == 1:
            return [1,1]
        i = numRows - 2
        ans = [[1], [1,1]]
        q = [1,1]
        while i > 0:
            a = []
            for j in range(len(q)):
                if j == 0:
                    a.append(1)
                else:
                    a.append(q[j]+q[j-1])
            a.append(1)
            ans.append(a)
            q = a
            i -=1
        return ans[rowIndex]
