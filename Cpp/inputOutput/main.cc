#include <cstdio>
#include <iostream>
using namespace std;

// gcpp main.cc
// ./main then hello then 1

int main() {
  string s; 
  int n;
  cin >> s >> n;
  //scanf("%s %d", &s, &n); this function doesnt work over string datatype 
  cout << s << " " << n << endl;
  return 0;
}