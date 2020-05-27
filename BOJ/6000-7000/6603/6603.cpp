#include <iostream>
#include <vector>

using namespace std;

int N;

int nums[13] = {0};

void select(vector<int> &selected, int last, int toPick)
{
    if (toPick == 0)
    {
        for (int i = 0; i < 6; i++)
            cout << selected[i] << " ";
        cout << endl;
        return;
    }

    for (int i = last + 1; i < N; i++)
    {
        selected.push_back(nums[i]);
        select(selected, i, toPick - 1);
        selected.pop_back();
    }
}
int main()
{

    vector<int> v;

    while (true)
    {

        cin >> N;

        if (N == 0)
            break;

        for (int i = 0; i < N; i++)
            cin >> nums[i];

        select(v, -1, 6);

        cout << endl;
    }

    return 0;
}