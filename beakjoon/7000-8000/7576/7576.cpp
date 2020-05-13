#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int M, N;
    int tmp, result = 0;

    cin >> M >> N;

    vector<int> map[N];
    vector<int> visited[N];
    queue<pair<int, int>> q;

    int dx[] = {0, 0, 1, -1};
    int dy[] = {1, -1, 0, 0};
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> tmp;
            map[i].push_back(tmp);
            visited[i].push_back(-1);
            if (tmp == 1)
            {
                q.push({j, i});
                visited[i][j] = 0;
            }
        }
    }

    while (!q.empty())
    {
        pair<int, int> pos = q.front();
        int x = pos.first;
        int y = pos.second;
        q.pop();

        for (int i = 0; i < 4; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (0 <= nx && nx < M && 0 <= ny && ny < N &&
                visited[ny][nx] == -1 && map[ny][nx] == 0)
            {
                visited[ny][nx] = visited[y][x] + 1;
                q.push({nx, ny});
            }
        }
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if (map[i][j] == 0 && visited[i][j] == -1)
            {
                result = -1;
                break;
            }
            result = max(result, visited[i][j]);
        }
        if (result == -1)
            break;
    }

    cout << result << "\n";

    return 0;
}