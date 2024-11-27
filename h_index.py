

citations = [3,0,6,1,5]

class Solution:
    def hIndex(self, citations):
        citations.sort(reverse=True)
        h_index = 0
        for i in range(len(citations)):
            if i + 1 <= citations[i]:
                h_index = i + 1 
            else:
                break 
        return h_index
    
x =  Solution()
print(x.hIndex(citations))


