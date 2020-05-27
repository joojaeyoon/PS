#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>

using namespace std;

int bfs(int n, int k)
{
    queue<int> q;
    vector<int> visited(100001, 0);

    int pos, time, N;
    int next[3] = {0};

    q.push(n);
    visited[n] = 1;

    while (!q.empty())
    {
        pos = q.front();
        q.pop();

        if (pos == k)
            return visited[pos] - 1;

        next[0] = pos * 2;
        next[1] = pos - 1;
        next[2] = pos + 1;

        for (int i = 0; i < 3; i++)
        {
            N = next[i];
            if (0 <= N && N <= 100000 && visited[N] == 0)
            {
                visited[N] = visited[pos] + 1;
                q.push(N);
            }
        }
    }
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, K;
    cin >> N >> K;

    if (N >= K)
        cout << N - K << "\n";
    else
        cout << bfs(N, K) << "\n";

    return 0;
}