#include<iostream>
using namespace std;

class Solution
{
public:
  void merge(int A[], int m, int B[], int n) {
    if (n == 0)
    {
      printf("The size of A or B is 0!\n");
      return;
    }

    int i = m-1, j = n-1, k = m+n-1;
    for (; k >= 0; --k)
    {
      if ( i < 0 || j < 0)
      {
        break;
      }
      if (B[j] >= A[i])
      {
        A[k] = B[j];
        --j;
      }
      else
      {
        A[k] = A[i];
        --i;
      }
    }

    if (j < 0)
    {
      return;
    }
    else{
      for(; k >= 0 && j >= 0; --k, --j)
        A[k] = B[j];
    }
    return;
  }
};

void printArray(int A[], int m){
  if (m <= 0)
  {
    printf("The size of the array is less than 0\n");
    return;
  }

  for (int i = 0; i < m; ++i)
  {
    printf("%d ", A[i]);
  }
  printf("\n");
  return;
}

int main(){
  int A[] = {0, 0, 0, 0};
  int B[] = {1, 4, 8, 9};
  Solution sol;
  sol.merge(A, 0, B, 4);
  printArray(A, 4);
  return 0;
}