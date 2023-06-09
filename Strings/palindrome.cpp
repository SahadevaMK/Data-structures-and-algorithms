#include<iostream>
using namespace std;
int main()
{
    char name[]="sahadeva";
    char name1[100];
    int i,j,n;
    
 for(i=0;name[i]!='\0';i++)
    {
        
    }
  i=i-1;
  for(j=0;i>=0;i--,j++)   ///////String Reversal
  {
      name1[j]=name[i];
  }
  name1[j]='\0';
  cout << name1 << endl;
  
  for(i=0,j=0;name[i]!='\0',name1[j]!='\0';i++,j++)
  {
      if(name[i]==name1[j]){
          continue;
      }
      else{
          cout << "the given string is not PALINDROME";
      }
  }
  cout<<" THE GIVEN STRING IS PALINDROME";
 
 return 0;
}
