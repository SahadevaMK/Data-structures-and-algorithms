#include<iostream>
using namespace std;

int main(){
    char s[] = "sahadeva";
    int i;
    for(i=0;s[i]!='\0';i++){
        s[i]=s[i]-32; // form lower case to upper case
        // s[i]=s[i]+32; // from upper case to lower case
    }
    cout << s;
}
