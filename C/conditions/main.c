#include <stdio.h>

int main(int argc, char** argv)
{
	int a = 2;

  if (a > 1)
  {
    // printf("Entró if\n");
  }
  else if (a > 0)
  {
    printf("Entró else if\n");
  }
  else
  {
    printf("Entró else\n");
  }

  int i = 0;

  while (i < 5)
  {
    // printf("Número iteración: %i\n", i);
    i += 1;
  }

  for (int j = 0; j < 5; j++)
  {
    printf("Número iteración: %i\n", j);
  }

  int k = 0;
  switch (k)
  {
  case 1:
    printf("0\n");
    break;
  default:
    printf("default\n");
    break;
  }

  return 0;
}