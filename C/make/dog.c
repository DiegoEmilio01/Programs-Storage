#include <stdio.h>
#include <stdlib.h>
#include "dog.h"


Dog* dog_init(char* name, int age)
{
  Dog* dog = malloc(sizeof(Dog));
  dog -> name = name;
  dog -> age = age;
  printf("Dog initialized!\n");
  return dog;
}

void dog_print(Dog* dog)
{
  printf("Dog's name: %s.\nDog's age: %i\n", dog -> name, dog -> age);
}

void dog_destroy(Dog* dog)
{
  free(dog);
  printf("Dog destroyed!\n");
}