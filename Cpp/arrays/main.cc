#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
  int n;
  scanf("%d\n", &n);
  int A[n];
  for(int i = 0; i < n; i++) scanf("%d", &A[i]);
  for(int i = n-1; i >= 0; i--) printf("%d ", A[i]);
  /*
  int* B;
  reverse_copy(A, A + n, B);
  printf("%d - %ld\n", n, (sizeof(A) / sizeof(int)));
  for(int i = 0; i < n; i++) printf("%d ", A[i]);
  printf("\n");
  for(int i = 0; i < n; i++) printf("%d ", B[i]);
  printf("\n");
  */
  return 0;
}