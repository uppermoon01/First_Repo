#include <bits/stdc++.h>
using namespace std;
typedef long long int ll ;
#define mp make_pair
#define pb push_back
#define f(i,a,b) for(int i=a;i<b;i++)
#define fr(j,a,b) for(int j=a;j>b;j--)
#define vi vector<int>
#define vvi vector<vi>

#define trav(a,x) for (auto& a : x)
#define all(x) x.begin(), x.end()

void solve(){
    int n;cin>>n;
    ll a[n],b[n];f(i,0,n)cin>>a[i];
    f(i,0,n)cin>>b[i];
    ll cnt =0;
    for(int i=1;i<n;i++){
        ll real = abs(a[i]-a[i-1]) + abs(b[i]-b[i-1]);
        ll img = abs(a[i]-b[i-1]) + abs(b[i]-a[i-1]);
        cnt += min(real,img);
    }
    cout<<cnt<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    ll t=1;
    cin>>t;
    while(t--){
        solve();
    }
    return 0;
}