class SelectSort():
    def select_sort(self,nums):
       for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]<nums[i]:
                    nums[i], nums[j] = nums[j],nums[i]
class BubbleSort():
    def bubble_sort(self,nums):
        n = len(nums)
        for i in range(n-1):
            isSwap = False         # 判断是否发生交换，如果没有说明已经有序可提前退出
            for j in range(0,n-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
                    isSwap = True
            if isSwap == False:
                break


def main():
    nums = [7,1,5,3,2,4]
    select_obj = SelectSort()
    select_obj.select_sort(nums)

    print("-------选择排序：",nums)


    nums = [1,2,3,4,5,6]
    bubble_obj = BubbleSort()
    bubble_obj.bubble_sort(nums)

    print("-------冒泡排序：",nums)
main()