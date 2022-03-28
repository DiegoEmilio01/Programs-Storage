#include <stdio.h>

// & gives the pointer
// * gives the value stored in the pointer
// %p is the pointer type

void update(int *a,int *b) {
  int at = *a;
  int bt = *b;
  *a = at + bt;
  *b = (at - bt > bt - at) ? at - bt : bt - at;
}

int main() {
  int a, b;
  int *pa = &a, *pb = &b;
  
  scanf("%d %d", &a, &b);

  //printf("%d %d\n", a, *pa);
  update(pa, pb);
  printf("%d\n%d\n", a, b);

  return 0;
}