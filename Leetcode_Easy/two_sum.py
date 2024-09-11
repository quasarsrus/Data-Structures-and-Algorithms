# Two Sum

class Solution:
    def twosum(self, nums: list[int], target: int) -> list[int]:
        
        a = {}
        for i in range(len(nums)):
            if target - int(nums[i]) not in a.values():
                a[i] = int(nums[i])
            else:
                return [i, list(a.keys())[list(a.values()).index(target - int(nums[i]))]]
        return [-1,-1]
        


if __name__ == "__main__":
    
    
    input_list = []
    while True:
        input_list.append(input())
        if input_list[-1] == '':
            del input_list[-1]
            break
    target = int(input())
    
    s = Solution()
    
    print(s.twosum(input_list, target))
