#include<bits/stdc++.h>
using namespace std;

int main(){
    int times;
    cin >> times;
    while (times--){
        int arr[2];
        cin >> arr[0];
        cin >> arr[1];
        string t1, t2;
        cin >> t1;
        cin >> t2;
        int count1=0;
        int count2=0;
        string repeat;
        for(int i=1;i<arr[0];i++){
            if (t1[i-1] == t1[i]){
                count1++;
                repeat = t1[i];
            }
        }
        for(int i=1;i<arr[1];i++){
            if (t2[i-1] == t2[i]){
                count2++;
                repeat = t2[i];
            }
        }
        // cout << "t1=" << count1 << endl;
        // cout << "t2=" << count2 << endl;
        if(count1+count2==0){
            cout << "YES" << endl;
        }else if (count1+count2>1){
            cout << "NO" << endl;
        }else if (count1==0){
            if(t1[arr[0]-1]!=t2[arr[1]-1]){
                cout << "YES" << endl;
            }else{
                cout << "NO" << endl;
            }
        }else if (count2==0){
            if(t1[arr[0]-1]!=t2[arr[1]-1]){
                cout << "YES" << endl;
            }else{
                cout << "NO" << endl;
            }
        }
    }
}