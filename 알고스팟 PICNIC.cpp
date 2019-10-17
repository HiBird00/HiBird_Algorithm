#include<iostream>
#include<vector>
using namespace std;

int sNum;
int pairNum;
vector<vector<bool>> isPair;
vector<bool> hasPartner;
vector<int> ans;

int getPartner() {
	int firstFree = -1;
	for (int i = 0; i < sNum; i++) {
		if (!hasPartner[i]) {
			firstFree = i;
			break;
		}
	}

	if (firstFree == -1) return 1;
	int ret = 0;

	for (int pairWith = firstFree + 1; pairWith < sNum; pairWith++) {
		if (!hasPartner[pairWith] && isPair[firstFree][pairWith]) {
			hasPartner[firstFree] = hasPartner[pairWith] = true;
			ret += getPartner();
			hasPartner[firstFree] = hasPartner[pairWith] = false;
		}
	}
	return ret;
}

int main() {
	int test;
	cin >> test;

	while (test--) {
		cin >> sNum;
		cin >> pairNum;
		hasPartner.assign(sNum, 0);
		isPair.assign(sNum, vector<bool>(sNum, false));
		for (int i = 0; i < pairNum; i++) {
			int first, second;
			cin >> first >> second;
			isPair[first][second] = true;
			isPair[second][first] = true;
		}
		
		ans.push_back(getPartner());
	}
	for (int i = 0; i < ans.size(); i++)
		cout << ans[i] << endl;

	return 0;
}

