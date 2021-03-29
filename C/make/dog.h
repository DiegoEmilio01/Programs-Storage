#pragma once  // para que solo se incluya una sola vez

typedef struct dog
{
  char* name;
  int age;
} Dog;

Dog* dog_init(char* name, int age);
void dog_print(Dog* dog);
void dog_destroy(Dog* dog);