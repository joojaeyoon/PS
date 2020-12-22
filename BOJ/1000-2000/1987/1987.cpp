#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int dx[]={1,-1,0,0};
int dy[]={0,0,1,-1};

int R,C;
int visited[26]={0};
int answer=0;
void dfs(vector<vector<int>> &board,int x,int y,int cnt){
    if(answer < cnt)
        answer=cnt;

    
    for(int i=0;i<4;i++){
        int nx=x+dx[i];
        int ny=y+dy[i];

        if(0<=nx && nx < C && 0<= ny && ny <R){
            int idx=board[ny][nx]-'A';
            
            if(!visited[idx]){
                visited[idx]=1;
                dfs(board,nx,ny,cnt+1);
                visited[idx]=0;
            }

        }
    }

}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin>>R>>C;
    vector<vector<int>> board(20,vector<int>(20,0));

    for(int i=0;i<R;i++){
        string tmp;
        cin>>tmp;
        for(int j=0;j<C;j++){
            board[i][j]=tmp[j];
        }
    }
    visited[board[0][0]-'A']=1;
    dfs(board,0,0,1);

    cout<<answer<<endl;

    return 0;
}