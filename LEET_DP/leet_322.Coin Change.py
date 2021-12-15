class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        #dp정의
        d = [-1]*(amount+1)
        d[0]=0
        #d[coins[0]]=1
        
        for i in range(amount+1):
            if d[i]!=-1:
                continue
            
            tmp = 99999999
            for c in coins:
                if i<c :
                    continue                    
                if d[i-c]==-1:
                    continue
                    
                tmp = min(tmp,d[i-c]+1)
            if tmp ==99999999:
                d[i]=-1
            else:
                d[i]=tmp

        return(d[amount])
        
