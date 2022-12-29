#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
int n,i,j;
scanf("%d", &n);//2
int len=2*n-1;//3
int start=0;
int end=len-1;//2
int a[len][len];//a[13][13];//a[3][3]

  while(n!=0)
  {
      for(i=start;i<=end;i++)
      {
          for(j=start;j<=end;j++)
          {
              if(i==start || i==end || j==start || j==end)
              {
                  a[i][j]=n;
              }
          }

      }
        start++;
          end--;
          n--;
  }
  for(i=0;i<len;i++)
  {
      for(j=0;j<len;j++)
      {
          printf("%d ",a[i][j]);
      }
      printf("\n");
  }
  return 0;
}