class Solution:
    def fourSum(self, num: List[int], target: int) -> List[List[int]]:
        num.sort()
        result=[]
        for i in range(len(num)-3):
            if i>0 and num[i]==num[i-1]:
                continue
            for j in range(i+1,len(num)-2):
                if j>i+1 and num[j]==num[j-1]:
                    continue
                l=j+1
                h=len(num)-1
                
                temptarget=target-num[i]-num[j]
                while(l<h):
                     
                    if num[l]+num[h]==temptarget:
                        result.append([num[i],num[j],num[l],num[h]])
                        l+=1
                        h-=1
                        while l<h and num[l]==num[l-1]:
                            l+=1
                    elif num[l]+num[h]<temptarget:
                        l+=1
                    else:
                        h-=1
                       
        return (result)
        
