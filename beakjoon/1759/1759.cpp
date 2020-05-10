#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

void select(vector<char> &alpha, string selected, int toPick, int prev, int mo, int ja)
{
    if (toPick == 0 && mo >= 1 && ja >= 2)
    {
        cout << selected << endl;
        return;
    }

    for (int i = prev + 1; i < alpha.size(); i++)
    {
        char ch = alpha[i];

        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
            select(alpha, selected + ch, toPick - 1, i, mo + 1, ja);
        else
            select(alpha, selected + ch, toPick - 1, i, mo, ja + 1);
    }
}
int main()
{
    int L, C;
    char tmp;
    vector<char> alpha;

    cin >> L >> C;

    for (int i = 0; i < C; i++)
    {
        cin >> tmp;
        alpha.push_back(tmp);
    }
    sort(alpha.begin(), alpha.end());

    select(alpha, "", L, -1, 0, 0);

    return 0;
}