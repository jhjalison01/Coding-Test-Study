class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #k: val이 아닌 정수의 개수
        k=0
        #temp: val이 아닌 정수 저장
        temp=[]
        for i in range(len(nums)):
            if nums[i]!=val:
                k+=1
                temp.append(nums[i])
        nums[:]=temp.copy()
        
        return k