#include<iostream>
using namespace std;
int main(){
    int arr[] = {1,2,2,3,5,6,6};
    int hs[7];
    int i;
    for (i=0;i<7;i++){
        hs[arr[i]]++;
    }
    for (i=0;i<7;i++){
        cout << hs[i]<< " " << i<< endl;
    }
}
