#include<bits/stdc++.h>
using namespace std;

int main(){
    vector<int> nums = {10, 4, 8, 3};
    vector<int> answer;
    for (int i=0;i<nums.size();i++){
        int leftsum=0;
        int rightsum=0;
        cout << "i=" << i << endl;
        for (int j=0;j<i;j++){
            leftsum += nums[j];
            cout << "\t leftsum += " << nums[j] << endl;
        }
        for (int j=i+1;j<nums.size();j++){
            rightsum += nums[j];
            cout << "\t\t rightsum += " << nums[j] << endl;
        }
        cout << "=>" << leftsum << " " << rightsum << endl;
        answer.push_back(abs(leftsum-rightsum));
    }
    cout << answer[0] << " " << answer[1] << " " << answer[2] << " " << answer[3];
    // return answer;
}