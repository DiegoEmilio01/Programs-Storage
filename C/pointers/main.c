#include <stdio.h>

int main(int argc, char** argv)
{
  int c = 12;
  int* d = &c;
  int* e = NULL;
  printf("%i\n", c);
  printf("%i\n", *d);
  printf("%li\n", sizeof(d));
  printf("%p\n", d);
  printf("%p\n", d + 1);
  // printf("%i\n", *(d + 1));
  // printf("%p\n", e);
  // printf("%p\n", NULL);
  return 0;
}