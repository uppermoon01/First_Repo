#include <bits/stdc++.h>
using namespace std;
typedef long long int ll ;
#define mp make_pair
#define pb push_back
#define f(i,a,b) for(int i=a;i<b;i++)
#define fr(j,a,b) for(int j=a;j>b;j--)
#define vi vector<int>
#define vvi vector<vi>
#define pi pair<int,int>


#define trav(a,x) for (auto& a : x)
#define all(x) x.begin(), x.end()

class Solution{
public:
    void solve(){
        int a,b;cin>>a>>b;
        int best_ans=INT_MAX;
        int carry = 0;
        if(b==1){
            b++;
            carry = 1;
        }
        for(int i=0;i<1000;i++){
            int x = a,y = b+i;
            int ans = i;
            while(x>0){
                if(x==y){
                    y++;
                }else{
                    x = x/y;
                }
                ans++;
            }
            best_ans = min(best_ans,ans);
        }
        cout<<best_ans+carry<<endl;
    }
};


int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    ll t=1;
    cin>>t;
    Solution ob;
    while(t--){
        ob.solve();
    }
    return 0;
}