#include <bits/stdc++.h>
class Solution {
public:
    vector<int> divisibilityArray(string word, int m) {
        vector<int> div;
        long long int s = 0;
        for (int i=0;i<word.length();i++){
            s = s*10 + word[i] - 48;
            if (s%m == 0){
                div.push_back(1);
            }else{
                div.push_back(0);
            }
        }
        return div;
    }
};