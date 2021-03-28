// gcc main.c -g -o main
// el -g es para que no optimice el codigo para debuguear mejor
// time ./main
// para analizar el tiempo del proceso
// valgrind ./main
// para analizar el proceso utilizando Valgrind
// gcc main.c -g -o main && valgrind --leak-check=full ./main

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char** argv)
{
  char* s = malloc(sizeof("Hello World!"));
  strcpy(s, "Hello World!"); // tambien existe strdup
  printf("%s\n", s);
  free(s);

  return 0;
}