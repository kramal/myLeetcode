class Solution:
    def getNumericCount(self, ) -> int:
        return 1
    def romanToInt(self, s: str) -> int:
        number_mapping = { 
            'I' : 1, 
            'II' : 2, 
            'III' :  3, 
            'IV' : 4,
            'V' : 5,
            'VI' : 6,
            'VII' : 7,
            'VIII' : 8,
            'IX' : 9,
            'X' : 10,
            'XL' : 40,
            'L' : 50,
            'XC' : 90,
            'C' : 100,
            'CD' : 400,
            'D' : 500,
            'CM' : 900,
            'M' : 1000
        }
        s = s + ' '
        i = 0
        result = 0
        while i < len(s)-1 :
            if s[i].split() == '':
                break
                
            if s[i] == 'M':  #1000
                result = result + number_mapping[s[i]]
                i = i + 1
                continue
            elif s[i] == 'C' and s[i + 1] == 'M': #900
                result = result + number_mapping[s[i] + s[i + 1]]
                i = i + 2
                continue
            elif s[i] == 'C' and s[i + 1] == 'D': #400 
                result = result + number_mapping[s[i] + s[i + 1]]
                i = i + 2
                continue
            elif s[i] == 'C' and s[i + 1] != 'M' and s[i + 1] != 'D': #100
                result = result + number_mapping[s[i]]
                i = i + 1
                continue
            elif s[i] == 'D': #500
                result = result + number_mapping[s[i]]
                i = i + 1
                continue
            elif s[i] == 'X' and s[i + 1] == 'C': #90
                result = result + number_mapping[s[i] + s[i + 1]]
                i = i + 2
                continue
            elif s[i] == 'X' and s[i + 1] == 'L':
                result = result + number_mapping[s[i] + s[i + 1]]
                i = i + 2
                continue
            elif s[i] == 'L':
                result = result + number_mapping[s[i]]
                i = i + 1
                continue
            elif s[i] == 'X':
                result = result + number_mapping[s[i]]
                i = i + 1
                continue
            elif s[i] == 'I' and s[i + 1] == 'X':
                result = result + number_mapping[s[i] + s[i + 1]]
                i = i + 2
                continue
            elif s[i] == 'I' and s[i + 1] == 'V':
                result = result + number_mapping[s[i] + s[i + 1]]
                i =  i + 2
                continue
            elif s[i] == 'V':
                result = result + number_mapping[s[i]]
                i = i + 1
                continue
            elif s[i] == 'I':
                result = result + number_mapping[s[i]]
                i = i + 1
                continue
        
        return result
            
            
        
