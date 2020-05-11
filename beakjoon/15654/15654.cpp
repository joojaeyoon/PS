#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int N, M;
int arr[8] = {};
bool visited[8] = {false};
void print_set(vector<int> &selected, int toPick)
{
    if (toPick == 0)
    {
        for (int i = 0; i < selected.size(); i++)
            cout << selected[i] << " ";
        cout << "\n";
        return;
    }

    for (int i = 0; i < N; i++)
    {
        if (!visited[i])
        {
            visited[i] = true;
            selected.push_back(arr[i]);

            print_set(selected, toPick - 1);

            visited[i] = false;
            selected.pop_back();
        }
    }
}
int main()
{
    cin >> N >> M;
    int tmp;
    vector<int> v;

    for (int i = 0; i < N; i++)
    {
        cin >> tmp;
        arr[i] = tmp;
    }

    sort(arr, arr + N);

    print_set(v, M);

    return 0;
}