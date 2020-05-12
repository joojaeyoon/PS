#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};
int N, idx = 0;
void dfs(vector<int> *map, vector<bool> *visited, vector<int> &counter, int x, int y, int count, int idx)
{
    visited[x][y] = true;
    counter[idx]++;

    for (int i = 0; i < 4; i++)
    {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (nx >= 0 && nx < N && ny >= 0 && ny < N && map[x][y] == map[nx][ny] && !visited[nx][ny])
            dfs(map, visited, counter, nx, ny, count + 1, idx);
    }
}
int main()
{

    cin >> N;

    vector<int> map[N];
    vector<bool> visited[N];
    vector<int> counter(N * N, 0);

    for (int i = 0; i < N; i++)
    {
        string tmp;
        cin >> tmp;
        for (int j = 0; j < N; j++)
        {
            map[i].push_back(tmp[j] - '0');
            visited[i].push_back(false);
        }
    }

    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            if (map[i][j] != 0 && !visited[i][j])
                dfs(map, visited, counter, i, j, 0, idx++);

    sort(counter.begin(), counter.begin() + idx);
    cout << idx << "\n";
    for (int i = 0; i < idx; i++)
        cout << counter[i] << "\n";

    return 0;
}