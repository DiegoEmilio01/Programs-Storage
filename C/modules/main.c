// gcc modulo.c maim.c -o main
// o
// gcc modulo.c -c -o modulo.o
// gcc main.c -c -o main.o
// gcc modulo.o main.o -o main

#include <stdio.h>
#include "dog.h"

int main(int argc, char** argv)
{
  Dog* pluto = dog_init("Pluto", 10);
  dog_print(pluto);
  dog_destroy(pluto);
  return 0;
}