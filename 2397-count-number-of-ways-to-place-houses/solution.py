class Solution:
    def countHousePlacements(self, n: int) -> int:
        
        # 1. for each i in n (0 and n inclusive), there can be a house in the 0th-nth(inclusive) plot on the other side
     

        answers = [0, 2, 3]
        for _ in range(n):
            answers.append(answers[-1] + answers[-2])

        return answers[n]**2 % (10**9+7)
 
        #1: 2^2 
        #2: 3^2 
        # 3: 5^2  
        #4:8^2 
        #5: 13^2  
        #6: 21^2 
