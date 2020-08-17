#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

#define MAX 8

int n;
vector<vector<double>> dist;
vector<bool> visited;
vector<int> path;
double tsp(vector<bool> visited, vector<int> path, double currentRet);

int main() {
	int c;
	cin >> c;
	
	for (int i = 0; i < c; i++) {
		cin >> n;
		dist = vector<vector<double>>(n, vector<double>(n, 0));
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < n; k++) {
				cin >> dist[j][k];
			}
		}
		
		double ret = 999999;
		for (int here = 0; here < n; here++) {
			visited = vector<bool>(n, false);
			path = vector<int>(1, here);
			visited[here] = true;

			ret = min(ret, tsp(visited, path, 0));
		}
		cout << fixed;
		cout.precision(10);
		cout << ret << endl;
	}
	return 0;

}

double tsp(vector<bool> visited, vector<int> path, double currentRet) {
	// 다 돌았을 때
	if (path.size() == n) {
		return currentRet;
	}

	double mini = 999999;
	for (int next = 0; next < n; next++) {
		if (visited[next])
			continue;
		int here = path.back();
		visited[next] = true;
		path.push_back(next);
		mini = min(mini, tsp(visited, path, currentRet + dist[here][next]));
		visited[next] = false;
		path.pop_back();
	}
	return mini;
}
