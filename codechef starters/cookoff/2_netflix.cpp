#include<iostream>

using namespace std;

int main(){
    int n;
    cin >> n;
    for (int i=0;i<n;i++){
        int arr[4];
        for(int i=0;i<4;i++){
            cin >> arr[i];
        }
        int sum = arr[0] + arr[1] + arr[2];
        if ((arr[0] + arr[1])>arr[3] || (arr[0] + arr[2])>arr[3] || (arr[1] + arr[2])>arr[3]){
            cout << "YES" << endl;
        }else{
            cout << "NO" << endl;
        }
    }
    return 0;
}