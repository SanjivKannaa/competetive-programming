#include <bits/stdc++.h>

using namespace std;

int main()
{
    int T, n , c;
    cin >> T;
    while (T--)
    {
        cin >> n >> c;
        vector<int> Tel;

        for(int i=0;i<n;i++){
            int temp;
            cin>>temp;
            Tel.push_back(temp+i+1);
        }
        sort(Tel.begin(), Tel.end());

        int ans=0;

        for(int num : Tel){
           c = c - num;
           if(c<0) break;
           ans++;
        }
        cout<<ans<<endl;
    }
}