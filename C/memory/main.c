#include <stdio.h>
#include <stdlib.h>

// int* badArray()
// {
//   int A[3] = {5, 6, 7};
//   return A;
// }

int* goodArray()
{
  int* A = calloc(3, sizeof(int));
  A[0] = 5;
  A[1] = 6;
  A[2] = 7;
  return A;
}

int main(int argc, char** argv)
{

  int a = 10;
  int* b = malloc(sizeof(int));
  *b = 5;
  printf("%i %i\n", a, *b);
  printf("%p %p\n", &a, b);
  free(b);

  // int* A = badArray();
  // printf("%i\n", A[1]);

  int* A = goodArray();
  printf("%i\n", A[1]);
  free(A);

  return 0;
}