#include<iostream>
using namespace std;

int main(){

    string arr="geeeks";
    int n=arr.length();
        int temp[26]={0};
        for(int i=0;i<n;i++){
            temp[arr[i]-97]++;
        }
        for(int i=0;i<26;i++){
            while(temp[i]>0){
                char c='a'+i;
                cout<<c;
                temp[i]--;
            }
        }

    return 0;
}