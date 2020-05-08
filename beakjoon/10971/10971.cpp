#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{

    int N;
    int costs[10][10] = {0};
    int cost = 10000000;
    vector<int> v;

    cin >> N;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            cin >> costs[i][j];

    for (int i = 0; i < N; i++)
        v.push_back(i);

    while (true)
    {

        int total = 0;
        bool flag = true;

        for (int i = 0; i < N - 1; i++)
        {
            if (costs[v[i]][v[i + 1]] == 0)
            {
                flag = false;
                break;
            }
            total += costs[v[i]][v[i + 1]];
        }
        if (costs[v[v.size() - 1]][v[0]] == 0)
            flag = false;
        total += costs[v[v.size() - 1]][v[0]];

        if (flag)
        {
            cost = min(cost, total);
        }

        if (!next_permutation(v.begin(), v.end()))
        {
            break;
        }
    }

    cout << cost << endl;

    return 0;
}