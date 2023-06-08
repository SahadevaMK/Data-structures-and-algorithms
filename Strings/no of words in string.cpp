#include<iostream>
using namespace std;
int main(){
  char a[] = "how are you";
  int i,words;
  for (int i=0;a[i]!='\0';i++){
    if (a[i] == ' '){
      words++;
    }
  }
  cout << words+1;
}
