#include <bits/stdc++.h>
using namespace std;

int kadane(int arr[], int n){
    
    int csum=0,msum=0;
    for(int i=0;i<n;i++){
        csum=csum+arr[i];
        if(csum<0){
            csum=0;
        }
        msum=max(msum,csum);
    }
    return msum;
}


int main(){

    int arr[10]={-4,1,3,-2,6,2,-1,-4,-7,-5};

    cout<<kadane(arr,10)<<" ";
	return 0;
}