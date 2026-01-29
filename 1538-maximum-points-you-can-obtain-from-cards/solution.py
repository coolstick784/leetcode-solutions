class Solution(object):
    def maxScore(self, cardPoints, k):
        rsum=0
        lsum=0
        for i in range(k):
            lsum+=cardPoints[i]
        r=len(cardPoints)-1
        maxi=lsum
        for i in range(k-1,-1,-1):
            
            lsum-=cardPoints[i]
            rsum+=cardPoints[r]
            r-=1
            maxi=max(maxi,lsum+rsum)
            
        return maxi

