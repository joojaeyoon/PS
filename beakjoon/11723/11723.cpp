#include <iostream>
#include <string>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;

    string command;
    int num;
    int s = 0;

    cin >> n;

    for (int i = 0; i < n; ++i)
    {
        command.clear();
        cin >> command;

        if (command == "all" || command == "empty")
        {
            if (command == "all")
                s = (1 << 21) - 1;
            else
                s = 0;
        }
        else
        {
            cin >> num;

            char ch = command[0];

            if (ch == 'a')
                s |= 1 << num;
            else if (ch == 'c')
                if (s & (1 << num))
                    cout << 1 << "\n";
                else
                    cout << 0 << "\n";
            else if (ch == 'r')
                s &= ~(1 << num);
            else if (ch == 't')
                s ^= 1 << num;
        }
    }
}