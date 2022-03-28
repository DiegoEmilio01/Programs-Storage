/*
Int ("%d"): 32 Bit integer
Long ("%ld"): 64 bit integer
Char ("%c"): Character type
Float ("%f"): 32 bit real value
Double ("%lf"): 64 bit real value
*/

#include <iostream>
#include <cstdio>
using namespace std;

int main() {
  char ch = 'x';
  double d = 12;
  printf("%c %lf\n", ch, d);
  return 0;
}

