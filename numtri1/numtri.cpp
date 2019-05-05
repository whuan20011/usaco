/*
ID: whuan2001
PROG: numtri
LANG: C++
 */
#include <iostream>
#include <fstream>
using namespace std;

int main() {
  int r;
  int best = 0;
  int triangle[1001][1001];
  ofstream fout("numtri.out");
  ifstream fin("numtri.in");

  fin >> r;

  for (int i = 1; i <= r; i++) {
    for (int j = 1; j <= i; j++) {
      fin >> triangle[i][j];
    }
  }

  for (int i = 2; i <= r; i++) {
    for (int j = 1; j <= i; j++) {
      if (j == 1) {
        triangle[i][j] += triangle[i-1][j];
      } else if (j == i) {
        triangle[i][j] += triangle[i-1][j-1];
      } else {
        triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1]);
      }
    }
  }

  for (int j = 1; j <= r; j++) {
    if (triangle[r][j] > best)
      best = triangle[r][j];
  }

  fout << best << endl;

  return 0;
}
