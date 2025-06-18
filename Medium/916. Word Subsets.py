class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count = {}
        output = []
        words1 = list(set(words1))
        words2 = list(set(words2))
        foutput = []
        m = list(set(join_strings(words2, "")))
        count_m = {}
        for i in m:
            count_m[i] = 0
            
        for q in words2:
            for k in q:
                if count_m[k] < len(list(find_indices(q,k))):
                    count_m[k] = len(list(find_indices(q,k)))
                    
        for i in words1:
            print(i)
            r = 0
            for j in m:
                if len(list(find_indices(i,j))) >= count_m[j]:
                    r +=1 
            
            if r == len(m):
                output.append(i)
        return output

def join_strings(array, separator=""):
    return separator.join(array)


def find_indices(string, char):
    for i, c in enumerate(string):
        if c == char:
            yield i
