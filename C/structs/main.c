#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv)
{
  struct perro
  {
    char* nombre;
    int edad;
  };
  typedef struct perro Perro; // un alias
  // o
  typedef struct gato
  {
    char* nombre;
    int edad;
  } Gato;

  struct perro cachupin = {"Cachupín", 10};
  Perro pluto = {.edad = 10, .nombre = "Pluto"};
  
  printf("%s\n", cachupin.nombre);
  printf("%s\n", pluto.nombre);
  
  Perro perros[2]; // arreglo de 2 perros 

  Gato* felix = malloc(sizeof(Gato));
  *felix = (Gato){"Feliz", 12};
  printf("%s\n", felix -> nombre);
  return 0;
}