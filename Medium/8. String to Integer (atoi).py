class Solution:

    def myAtoi(self, s: str) -> int:
        if s == '' or s== '+' or s=='-' or s == ' ':
            return 0
        flag = 'p'
        F = 'b'
        v = ['-','+','0','1','2','3','4','5','6','7','8','9']
        if s[0] not in v and s[0] != ' ':
            return 0
        o = ''
        for i in s:
            if i == ' ' and F == 'b':
                continue
            elif i in v:
                o = o + i
                F = 'n'
            else:
                break

        if len(o) == 0:
            return 0
        if o[0:2] == '-+' or o[0:2] == '+-':
            return 0
        
        
        del(v[0])
        del(v[0])
#         print(v)
        dic = {'-' : 0, '+' : 0}
        for i in range(len(o)):
            if o[i] == '-':
                dic['-'] +=1
            elif o[i] == '+':
                dic['+'] +=1
            if o[i] in v:
                if i>0:
                    if o[i-1] == '-':
                        flag = 'n'
                    elif o[i-1] == '+':
                        flag = 'p'
                o = o[i:]
                break
                
        if flag == 'p' and dic['+']%2 == 0 and dic['+'] != 0:
            return 0
        elif flag == 'n' and dic['-']%2 == 0 and dic['-'] != 0:
            return 0 
        
        final = ''
        for i in o:
            if i in v:
                final = final + i
            else:
                break
        if len(final) == 0:
            return 0
                
        final = int(final)
        if flag == 'n':
            final = -1*final
            if final < -2**31:
                final = -2**31
        else:
            if final > (2**31)-1:
                final = (2**31)-1
            
        return final
            
        return final

        
