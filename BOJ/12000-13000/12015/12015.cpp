#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    int N;
    vector<int> li;
    vector<int> arr;
    vector<int>::iterator iter;
    cin>>N;
    
    for(int i=0;i<N;i++){
        int tmp;
        cin>>tmp;
        arr.push_back(tmp);
    }

    for(int i=0;i<N;i++){
        if(li.empty() || li[li.size()-1] < arr[i])
            li.push_back(arr[i]);
        else{
            iter=lower_bound(li.begin(),li.end(),arr[i]);
            *iter=arr[i];
        }
    }

    cout<<li.size()<<endl;

    return 0;
}