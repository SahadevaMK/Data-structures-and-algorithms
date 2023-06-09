#include<iostream>
using namespace std;
int main(){
    int arr[] = {1,2,2,3,5,6,6};
    int i,lastduplicate = 0;
    for (i=0;i<7;i++){
        if (arr[i] == arr[i+1] && arr[i]!=lastduplicate ){
            cout << arr[i] << endl;
            lastduplicate = arr[i];
        }
    }
}
