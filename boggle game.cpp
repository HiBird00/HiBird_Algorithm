#include<iostream>
#include<vector>
#include<string>
using namespace std;

string map[5][5];	//맵에 써있는 알파벳
string word; //찾을 단어
int dx[8] = { -1,-1,-1,1,1,1,0,0 };
int dy[8] = { -1,0,1,-1,0,1,-1,1 };

bool isRange(int x, int y) {
	//맵 범위 밖
	if (x < 0 || y < 0 || x>4 || y>4)
		return false;
	return true;
}

bool isHavingWord(int x, int y, const string& word) {
	//기저사례
	//1. 범위 밖
	if (!isRange(x, y)) return false;
	
	//2. 첫 글자 틀림
	if (map[y][x] != word.substr(0,1)) return false;

	//3. word가 한글자
	if (word.size() == 1) return true;
	
	//첫 글자 맞으면 다음 글자 보기
	for (int move = 0; move < 8; ++move) {
		int nextX = x + dx[move];
		int nextY = y + dy[move];
		if (isHavingWord(nextX, nextY, word.substr(1)))
			return true;
	}
	return false;
}

int main() {
	cin >> word;
	for (int i = 0; i < 5; i++)
		for (int j = 0; j < 5; j++)
			cin >> map[i][j];
	bool answer = false;
	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 5; j++) {
			if (answer = isHavingWord(i, j, word)) break;
		}
		if (answer)	break;
	}

	if(answer) cout << word << " IS IN!!" << endl;
	else cout << word << " IS NOT IN!!" << endl;

	return 0;
}
