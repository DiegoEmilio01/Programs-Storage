#include <stdio.h>

int sumArrayOfArrays(int* array, int rows, int cols)
{
  int sum = 0;
  for (int i = 0; i < rows * cols; i += 1)
  {
    sum += array[i];
  }
  return sum;
}

int main(int argc, char** argv)
{
  int A[6] = {0, 5, 3, 4, 7, 8};
  float B[4];
  B[0] = 1;
  printf("%p %p\n", A, &A);
  printf("%i %i %i\n", A[1], *(A+1), 1[A]);
  printf("%f\n", B[0]);
  printf("%f\n", B[1]);

  int C[3][2] = {{8, 2}, {1, 3}, {9, 4}};
  printf("%p\n", C);
  void* D = C;
  // printf("%p\n", D);
  printf("%i\n", sumArrayOfArrays(C, 3, 2));
  return 0;
}