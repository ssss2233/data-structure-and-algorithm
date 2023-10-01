#include<iostream>
using namespace std;

int fib(int n){
    if(n == 1 || n == 2)
    {
        return n-1;
    }
    int res = fib(n-1)+fib(n-2);
    return res;
    }
void insert(int *nums, int size,int num , int index){
    for(int i = size - 1; i>index;i--){
        nums[i] = nums[i-1];
    }
    nums[index] = num;
}

int main(){
    int res = fib(1);
    int nums[5] {1,2,3,4,0};
    insert(nums,5,5,2);
    for(int i = 0; i<5;i++){
        cout<<nums[i];
    }
    cout<<res<<std::endl;
    return 0;

}