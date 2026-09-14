class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero = 0
        # one zero, everything but n==0 will be prod. two zeros, everything will be zero
        for n in nums:
            if n==0:
                zero+=1
            else: 
                prod*=n
        res=[]
        for n in nums:
            if zero>=2:
                res.append(0)
            elif zero == 1 and n==0:
                res.append(prod)
            elif zero ==1:
                res.append(0)
            else:
                res.append(prod//n)
        return res
