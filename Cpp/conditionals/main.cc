#include <cstdio>
#include <iostream>
using namespace std;

// (a > b) ? true : false;

int main() {
  int a = 12;
  if(a > 5) {
    cout << "1\n";
  }
  else if(a > 6) {
    cout << "2\n";
  }
  else {
    cout << "3\n";
  }
  return 0;
}

