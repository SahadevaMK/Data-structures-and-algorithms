#include<iostream>
using namespace std;
int main(){
  char s[] = "how rre you";
  int i,words;
  int c = 1;
  int v = 2;
  for (int i=0;s[i]!='\0';i++){
      if (!(s[i]>=65 && s[i] <=90) && !(s[i]>=97 && s[i] <=122) && !(s[i]>=48 && s[i] <=57)){
          cout << "invalid STRING";
      }
  }
  cout << "valid string";
}
validate a string means a string should have only upper and lower case alphabets and numbers in it no special characters
