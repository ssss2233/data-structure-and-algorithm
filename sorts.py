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
class InsertSort():
    def insert_sort(self,nums):
        n = len(nums)
        for i in range(1,n):
            base = nums[i]
            insert_point = 0   #插入点位置
            for j in range(i-1,-2,-1):
                insert_point = j+1
                if nums[j] > base and j >= 0:
                    nums[j+1] = nums[j]
                else:
                    break              
            nums[insert_point] = base
class QuickSort():
    def partion(self,nums,left,right):
        i, j = left+1, right
        while(i<j):
            while(i<j and nums[j]>nums[left]): j-=1
            while(i<j and nums[i]<nums[left]): i+=1
            if(i<j):
                nums[i],nums[j] = nums[j], nums[i]
        nums[left],nums[i] = nums[i],nums[left]   
        return i  
    def quick_sort(self,nums,left,right):
        if(left >= right):
            return
        pivot = self.partion(nums,left,right)
        self.quick_sort(nums,left,pivot-1)
        self.quick_sort(nums,pivot+1,right)

class MergeSort():
    def merge(self,nums,left,mid,right):
        tmp = list(nums[left:right+1])  # 索引是[0:right-left]
        left_start = 0
        left_end = mid - left
        right_start = mid+1-left
        right_end = right - left
        i = left_start
        j = right_start
        for k in range(left,right+1):
            if i > left_end:
                nums[k] = tmp[j]
                j+=1
            elif j > right_end or tmp[j]>=tmp[i]:
                nums[k] = tmp[i]
                i+=1
            else:
                nums[k] = tmp[j]
                j += 1
    def merge_sort(self,nums,left,right):
        if(left >= right):
            return
        mid = (left+right)//2
        self.merge_sort(nums,left,mid)
        
        self.merge_sort(nums,mid+1,right)
        
        self.merge(nums,left,mid,right)


class HeapSort():
    def sift_down(self,nums,n,i):
        while True:
            tmp = i  
            l = 2*i+1      
            r = 2*i+2
            # 找i及其子节点中最大的
            if l<n and nums[l] > nums[tmp]:
                tmp = l
            if r<n and nums[r] > nums[tmp]:
                tmp = r
            if tmp == i:
                break
            nums[i],nums[tmp] = nums[tmp],nums[i]
            i = tmp
    def heap_sort(self,nums):
        for i in range(len(nums)//2-1,-1,-1):
            self.sift_down(nums,len(nums),i)
            # print(nums)
        for i in range(len(nums)):
            nums[0],nums[len(nums)-i-1] = nums[len(nums)-i-1], nums[0]
            self.sift_down(nums,len(nums)-i-1,0)

        
        


def main():
    nums = [7,1,5,3,2,4]
    select_obj = SelectSort()
    select_obj.select_sort(nums)

    print("-------选择排序：",nums)


    nums = [1,2,3,4,5,6]
    bubble_obj = BubbleSort()
    bubble_obj.bubble_sort(nums)

    print("-------冒泡排序：",nums)


    nums = [7,1,5,3,2,4]
    insert_obj = InsertSort()
    insert_obj.insert_sort(nums)

    print("-------插入排序：",nums)

    nums = [7,1,5,3,2,4]
    quick_obj = QuickSort()
    quick_obj.quick_sort(nums,0,len(nums)-1)

    print("-------快速排序：",nums)

    nums = [7,1,5,3,2,4]
    merge_obj = MergeSort()
    merge_obj.merge_sort(nums,0,len(nums)-1)

    print("-------归并排序：",nums)

    nums = [7,1,5,3,2,4]
    heap_obj = HeapSort()
    heap_obj.heap_sort(nums)

    print("-------堆排序：",nums)
main()