#include<iostream>
#include<cstring>

using namespace std;

int cache[40];

int main() {
	int T;
	cin >> T;
	while (T--) {
		int num;
		cin >> num;
		memset(cache, 0, 40);
		cache[0] = 0; cache[1] = 1;
		if (num == 0) {
			cout << 1 << " " << 0 << endl;
		}
		else if (num == 1) {
			cout << 0 << " " << 1 << endl;
		}
		else {
			for (int i = 2; i <= num; i++) {
				cache[i] = cache[i - 1] + cache[i - 2];
			}
			cout << cache[num - 1] << " " << cache[num] << endl;
		}

	}
		
	return 0;
}
