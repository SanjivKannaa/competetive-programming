#include <bits/stdc++.h>

using namespace std;

int main()
{
    int T, n;
    cin >> T;
    while (T--)
    {
        cin >> n;
        string s;
        cin >> s;
        int x = 0, y = 0;
        bool flag = false;
        for (char ch : s)
        {
            if (ch == 'U')
                y++;
            else if (ch == 'D')
                y--;
            else if (ch == 'L')
                x--;
            else if (ch == 'R')
                x++;

            if (y == 1 && x == 1 && !flag)
            {
                cout << "YES" << endl;
                flag = true;
            }
        }
        if (flag == false)
            cout << "NO" << endl;
    }
}