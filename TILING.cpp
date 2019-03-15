#include<iostream>

using namespace std;

int d[1001];

int tiling(int x) {
	if (x == 1) return 1;
	if (x == 2) return 2;
	if (d[x] != 0) return d[x];
	return d[x] = (tiling(x - 1) + tiling(x - 2)) % 10007;
}

int main() {
	int n;
	cin >> n;
	cout << tiling(n)<< endl;
	return 0;
}
