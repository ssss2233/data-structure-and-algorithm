#include<iostream>
using namespace std;

void insert(int *nums, int size,int num , int index){
    for(int i = size - 1; i>index;i--){
        nums[i] = nums[i-1];
    }
    nums[index] = num;
}
void traverse(int *nums, int size){
    for(int i=0;i<size;i++){
        cout<<nums[i];
    }
}
void remove(int *nums,int size, int index){
    for(int i = index;i < size-1;i++){
        nums[i] = nums[i+1];
    }
}
int find(int *nums,int size,int num){
    for(int i=0;i <size ; i++){
        if(nums[i] == num){
            return i;
        }
    }
    return -1;
}

int *extend(int *nums,int size,int enlarge){
    int *res = new int[size + enlarge];
    for(int i= 0;i<size;i++){
        res[i] = nums[i];
    }
    delete []nums;
    return res;
}
int main(){

    int nums[5] {1,2,3,4,0};
    insert(nums,5,5,2);
    for(int i = 0; i<5;i++){
        cout<<nums[i];
    }
    return 0;

}