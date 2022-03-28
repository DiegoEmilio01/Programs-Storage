#include <sstream>
#include <iostream>
using namespace std;

// string s; can be added, has index access, can be printed by cout and have a size sting.size()

// use of stringstream class

int main() {
  stringstream ss("23,4,56");
  char ch;
  int a, b, c;
  ss >> a >> ch >> b >> ch >> c;
  cout << c << " " << b << " " << a << endl;
}

/* for variable size
char ch;
int a;
for (;ss >> a;) {
  integers.push_back(a);
  ss >> ch;
}
*/