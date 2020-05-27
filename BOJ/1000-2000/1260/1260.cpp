#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>

using namespace std;

int N, M, V;
vector<vector<int>> children;

void dfs(vector<bool> &visited, int num)
{
    if (visited[num])
        return;
    visited[num] = true;
    cout << num << " ";

    for (int i = 0; i < children[num].size(); i++)
        dfs(visited, children[num][i]);
}
void bfs(vector<bool> &visited, int num)
{
    queue<int> q;

    q.push(num);
    visited[num] = true;
    while (!q.empty())
    {
        num = q.front();
        cout << num << " ";

        q.pop();

        for (int i = 0; i < children[num].size(); i++)
        {
            int N = children[num][i];
            if (!visited[N])
            {
                visited[N] = true;
                q.push(N);
            }
        }
    }
}
int main()
{
    cin >> N >> M >> V;
    int a, b;
    vector<bool> visited(N + 1, false);

    children.resize(N + 1);

    for (int i = 0; i < M; i++)
    {
        cin >> a >> b;
        children[a].push_back(b);
        children[b].push_back(a);
    }

    for (int i = 1; i <= N; i++)
        sort(children[i].begin(), children[i].end());

    dfs(visited, V);
    cout << "\n";

    for (int i = 0; i < N + 1; i++)
        visited[i] = false;

    bfs(visited, V);
    cout << "\n";

    return 0;
}