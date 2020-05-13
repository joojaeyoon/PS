#include <iostream>
#include <vector>

using namespace std;

int max_value = -1000000000;
int min_value = 1000000000;

void select(vector<int> &nums, vector<int> &op_count, int toPick, int length, int N);
void input(int N, vector<int> &nums, vector<int> &op);
int oper(int a, int b, int i);

int main()
{
    int N, sum = 0;
    vector<int> nums;
    vector<int> op;
    input(N, nums, op);

    select(nums, op, nums.size() - 1, nums.size() - 1, nums[0]);

    cout << max_value << endl
         << min_value << endl;

    return 0;
}
int oper(int a, int b, int i)
{
    int ret = 0;

    if (i == 0)
        ret = a + b;
    else if (i == 1)
        ret = a - b;
    else if (i == 2)
        ret = a * b;
    else
        ret = a / b;

    return ret;
}
void select(vector<int> &nums, vector<int> &op_count, int toPick, int length, int N)
{
    if (toPick == 0)
    {
        max_value = max(max_value, N);
        min_value = min(min_value, N);
        return;
    }

    for (int i = 0; i < 4; i++)
    {
        if (op_count[i] != 0)
        {
            op_count[i] -= 1;
            select(nums, op_count, toPick - 1, length, oper(N, nums[length - toPick + 1], i));
            op_count[i] += 1;
        }
    }
}
void input(int N, vector<int> &nums, vector<int> &op)
{
    int tmp;

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> tmp;
        nums.push_back(tmp);
    }

    for (int i = 0; i < 4; i++)
    {
        cin >> tmp;
        op.push_back(tmp);
    }
}