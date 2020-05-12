#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

bool dfs(vector<int> &color, vector<int> *graph, int num, int c)
{
    color[num] = c;

    for (int i = 0; i < graph[num].size(); i++)
    {
        int N = graph[num][i];

        if (color[N] == 0)
        {
            if (!dfs(color, graph, N, 3 - c))
                return false;
        }
        else if (color[N] == color[num])
            return false;
    }

    return true;
}
int main()
{
    int K;

    cin >> K;

    for (int i = 0; i < K; i++)
    {
        int V, E;
        bool check = true;
        cin >> V >> E;

        vector<int> graph[V + 1];
        vector<int> color(V + 1, 0);

        for (int j = 0; j < E; j++)
        {
            int a, b;
            cin >> a >> b;
            graph[a].push_back(b);
            graph[b].push_back(a);
        }

        for (int j = 1; j < V + 1; j++)
            if (color[j] == 0 && !dfs(color, graph, j, 1))
                check = false;

        if (check)
            cout << "YES\n";
        else
            cout << "NO\n";
    }

    return 0;
}