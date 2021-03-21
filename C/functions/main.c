#include <stdio.h>

int function(int num)
{
  printf("Número es: %i\n", num);
  return 0;
}

int main(int argc, char** argv)
{
  function(1);
  return 0;
}