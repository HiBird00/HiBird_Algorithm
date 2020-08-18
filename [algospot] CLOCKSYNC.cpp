#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;


int numSwitch[10][5] = {
	{0,1,2,-1,-1},
	{3,7,9,11,-1},
	{4,10,14,15,-1},
	{0,4,5,6,7},
	{6,7,8,10,12},
	{0,2,14,15,-1},
	{3,14,15,-1,-1},
	{4,5,7,14,15},
	{1,2,3,4,5},
	{3,4,5,9,13}
};

const int INF = 9999;

int setClock(int start, vector<int>& clock);
void onSwitch(int start, vector<int>& clock);
int isFinished(vector<int>& clock);

int main() {
	int c;
	cin >> c;
	
	for (int i = 0; i < c; i++) {
		vector<int> clock(16, 0);
		for (int j = 0; j < 16; j++) {
			cin >> clock[j];
		}
		int result = INF;
		for (int start = 0; start < 10; start++) {
			result = min(result, setClock(start, clock));
		}
		if (result == INF) {
			cout << -1 << endl;
		}
		else {
			cout << result << endl;
		}
	}
	return 0;
}

int isFinished(vector<int>& clock) {
	int i;
	for (i = 0; i < 16; i++) {
		if (clock[i] != 12)
			return INF;
	}
	if (i == 16) {
		return 0;
	}
}

int setClock(int start, vector<int>& clock) {
	// 기저사실
	// 다 12시로 되었다
	if (start == 10) {
		if (!isFinished(clock)) {
			return 0;
		}
		else {
			return INF;
		}
	}

	//탐색 시작
	int ret = INF;
	for (int cnt = 0; cnt < 4; cnt++) {
		ret = min(ret, cnt + setClock(start + 1, clock));
		onSwitch(start, clock);
	}
	return ret;
}

void onSwitch(int start, vector<int>& clock) {
	for (int conn = 0; conn < 5; conn++) {
		// 연결된 시계가 없다면
		if (numSwitch[start][conn] == -1) {
			break;
		}
		int clockNumber = numSwitch[start][conn];
		if (clock[clockNumber] == 12) {
			clock[clockNumber] = 3;
		}
		else {
			clock[clockNumber] += 3;
		}
	}
}


// 스위치를 4번 누르면 원상복귀 -> 4번 이상 누르지 않는다
// 이 부분이 무한루푸를 막았다.
// 스위치와 같은 문제, 즉 모양이 규칙적으로 순환되어 바뀌는 문제에서는 원상복귀되는 부분을 체크하면 좋다!!!

// 그리고 c++이 파이썬보다 알고리즘엔 좋은 것 같다.

// 아주 큰 숫자를 작성할 때에는 define으로 미리 지정해놓으면 편하다!
