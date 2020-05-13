#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;
int dx[] = {0, 1, -1, 0};
int dy[] = {1, 0, 0, -1};

int map[100][100];
int dist[100][100];

int N, M;
int main()
{
    cin >> M >> N;

    queue<pair<int, int>> q;
    pair<int, int> p;

    for (int i = 0; i < N; i++)
    {
        string tmp;
        cin >> tmp;
        for (int j = 0; j < M; j++)
        {
            map[i][j] = tmp[j] - '0';
            dist[i][j] = 10000000;
        }
    }

    q.push(make_pair(0, 0));
    dist[0][0] = 0;

    while (!q.empty())
    {
        p = q.front();

        q.pop();

        for (int i = 0; i < 4; i++)
        {
            int nx = p.first + dx[i];
            int ny = p.second + dy[i];

            if (0 <= nx && nx < M && 0 <= ny && ny < N)
            {
                if (map[ny][nx] == 1)
                {
                    if (dist[ny][nx] > dist[p.second][p.first] + 1)
                    {
                        dist[ny][nx] = dist[p.second][p.first] + 1;
                        q.push(make_pair(nx, ny));
                    }
                }
                else
                {
                    if (dist[ny][nx] > dist[p.second][p.first])
                    {
                        dist[ny][nx] = min(dist[ny][nx], dist[p.second][p.first]);
                        q.push(make_pair(nx, ny));
                    }
                }
            }
        }
    }

    cout << dist[N - 1][M - 1] << "\n";

    return 0;
}