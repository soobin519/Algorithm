class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total = len(cost)
        d= [0]*(total+1)
        for i in range(2,total+1):          
            d[i] = min(d[i-1]+cost[i-1],d[i-2]+cost[i-2])
        return d[total]
        
