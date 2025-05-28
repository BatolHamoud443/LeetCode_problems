class Solution:
    def intToRoman(self, num: int) -> str:
        s = ''
        while num:
            k = num//1000
            for i in range(k):
                s = s+'M'
            if num >= 1000:            
                num = num-k*1000
            h = num//100
            if h == 9:
                s = s+'CM'
            elif h >=5:
                s = s+ 'D'
                for i in range(h-5):
                    s = s+'C'
            elif h == 4:
                s = s+'CD'
            else:
                for i in range(h):
                    s = s+'C'
            if num >=100:
                num = num-h*100
                
            d = num//10
            if d == 9:
                s = s+'XC'
            elif d>=5:
                s = s +'L'
                for i in range(d-5):
                    s = s+'X'
            elif d == 4:
                s = s+'XL'
            else:
                for i in range(d):
                    s = s+'X'
            if num >=10:
                num = num-d*10
                
            if num == 9:
                s = s+'IX'
            elif num >=5:
                s = s+ 'V'
                for i in range(num-5):
                    s = s+'I'
            elif num == 4:
                s = s+'IV'
            else:
                for i in range(num):
                    s = s+'I'
            num = 0
        return s
