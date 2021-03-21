#include <stdio.h>

int main(int argc, char** argv)
{
	int a = 2;
  printf("Número: %i\n", a);
  // printf("Tamaño: %zu\n", sizeof(a));

	float b = 2.5;
  printf("Número: %f\n", b);
  // printf("Tamaño: %zu\n", sizeof(b));

	double c = 2.33;
  printf("Número: %lf\n", c);
  // printf("Tamaño: %zu\n", sizeof(c));

	char d = 'e';
  printf("Caracter: %c\n", d);
  // printf("Tamaño: %zu\n", sizeof(d));

	// Casting
	int e = 65;
	char f = e;
	char g = (char) e;
	printf("Valor f: %c\n", f);
	printf("Valor g: %c\n", g);


  return 0;
}