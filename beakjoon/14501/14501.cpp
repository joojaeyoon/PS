#include <iostream>

using namespace std;

int N = 0;
int T[15] = {0};
int P[15] = {0};
int max_value = 0;
void find(int day, int cost)
{
    bool flag = true;

    for (int i = day; i < N; i++)
        if (day + T[i] + i - day <= N)
            find(day + T[i] + i - day, cost + P[i]);

    if (flag)
    {
        max_value = max(max_value, cost);
        return;
    }
}

int main()
{

    cin >> N;

    for (int i = 0; i < N; i++)
        cin >> T[i] >> P[i];

    find(0, 0);

    cout << max_value << endl;

    return 0;
}