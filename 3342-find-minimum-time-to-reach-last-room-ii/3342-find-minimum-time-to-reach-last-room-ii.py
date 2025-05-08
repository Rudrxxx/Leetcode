class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n,m = len(moveTime), len(moveTime[0])
        q = [((0,True),0,0)] 

        s = set() 

        while q : 
            (t,a),i,j = heapq.heappop(q)   
            
            if (i,j) not in s :   
                if i == n - 1 and j == m - 1 :   
                    return t
                
                s.add((i,j)) 

                for k in [1,-1] :  
                    if 0 <= i + k < n : 
                        heapq.heappush(q, ((max(moveTime[i + k][j], t) + (1 if a else 2), not a), i + k, j)) 
                    if 0 <= j + k < m : 
                        heapq.heappush(q, ((max(moveTime[i][j + k], t) + (1 if a else 2), not a), i , j + k))  
        
        return -1