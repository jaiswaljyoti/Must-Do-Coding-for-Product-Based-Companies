#User function Template for python3

class Solution:
	def fractionToDecimal(self, numerator, denominator):
		# Code here
        res = numerator//denominator
	    if(numerator%denominator==0):
	        return res
	    s = str(res)
	    s+="."
	    lookup = {}
	    rem = numerator%denominator
        while(rem!=0 and rem not in lookup):
            lookup[rem] = len(s)
            rem = rem * 10
            res_part = rem // denominator
            s += str(res_part)
            rem = rem % denominator
        if (rem == 0):
            return s
        else:
            return(s[:lookup[rem]]+"("+s[lookup[rem]:]+")")
