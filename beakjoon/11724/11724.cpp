#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int N, M;
bool visited[1001] = {false};
vector<int> graph[1001];

void dfs(int num)
{
    visited[num] = true;

    for (int i = 0; i < graph[num].size(); i++)
    {
        int N = graph[num][i];
        if (!visited[N])
            dfs(N);
    }
}
int main()
{
    cin >> N >> M;
    int a, b, count = 0;

    for (int i = 0; i < M; i++)
    {
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    for (int i = 1; i < N + 1; i++)
    {
        if (!visited[i])
        {
            dfs(i);
            count++;
        }
    }
    cout << count << "\n";

    return 0;
}