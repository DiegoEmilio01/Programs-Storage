#include <stdio.h>

int main(int argc, char** argv)
{
  char s[3] = {'d', 'e', '\0'};
  printf("%s\n", s);
  char r[5] = "Hola";
  printf("%s\n", r);
  return 0;
}