#include<stdio.h>
#include<stdlib.h>

void main(){
    // int* nums1; int nums1Size, int m, int* nums2, int nums2Size, int n;
    int* nums1 = {1,2,3,0,0,0};
    int* nums2 = {2,5,6};
    int m = 3;
    int n = 3;
    int nums1Size = 6;
    int nums2Size = 3;
    
    int *shit                                                                                                                                   ;
    shit = (int*)malloc(sizeof(int)*nums1Size);
    int arr1=0, arr2=0, i = 0;
    while(arr1<m || arr2<n){
        if (nums1[arr1] <= nums2[arr2]){
            shit[i] = nums1[arr1];
            arr1++;
        }else if(nums2[arr2] <= nums1[arr1]){
            shit[i] = nums2[arr2];
            arr2++;
        }
    }
    nums1 = shit;
}