#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int N, M;
int arr[] = {1, 2, 3, 4, 5, 6, 7, 8};

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
        selected.push_back(arr[i]);
        print_set(selected, toPick - 1);
        selected.pop_back();
    }
}
int main()
{
    cin >> N >> M;
    vector<int> v;

    print_set(v, M);

    return 0;
}