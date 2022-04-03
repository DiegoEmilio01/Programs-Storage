#include <iostream>
using namespace std;


int main() {
  cout << (2 << 2) << endl;
  cout << (65536 >> 16) << endl;
  unsigned short id = ((2 << 17) + 300) % (2 << 16);
  unsigned short id2 = (unsigned short)((2 << 17) + 300);
  cout << id << endl;
  cout << id2 << endl;
  return 0;
}