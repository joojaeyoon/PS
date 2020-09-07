#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int N,M;
    int answer=0;

    vector<long long> trees;

    cin>>N>>M;
    
    for(int i=0;i<N;i++){
        long long tmp;
        cin>>tmp;
        trees.push_back(tmp);
    }

    long long lo=0;
    long long hi=*max_element(trees.begin(),trees.end());

    while(lo<=hi){
        long long mid=(lo+hi)/2;
        long long total=0;

        for(int i=0;i<N;i++)
            if(trees[i] > mid)
                total+=trees[i]-mid;
        
        if (total>=M){
            lo=mid+1;
            if (answer < mid)
                answer = mid;
        }
        else
            hi=mid-1;
    }
    cout<<answer<<endl;

    return 0;
}