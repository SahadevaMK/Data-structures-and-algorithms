#include<iostream>
using namespace std;

int main(){
    char a[] = "how are you";
    int i,vcount,consonentCount;
    for(i=0;a[i]!='\0';i++){
        if (a[i] == 'a' || a[i] == 'e' || a[i] == 'i' || a[i] == 'o' || a[i] == 'u' || a[i] == 'A' || a[i] == 'E' ||a[i] == 'I' ||a[i] == 'O' ||a[i] == 'U'){
            vcount++;
        }
        else if((a[i]>=65 && a[i]<=90) || a[i]>=97 && a[i]<=122){
            consonentCount++;
        }
        
    }
    cout << "no of vowels presnet in given string is " << vcount <<endl;
    cout << "no of consonents present in given string is " << consonentCount;
}
