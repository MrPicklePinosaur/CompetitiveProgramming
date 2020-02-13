#include <bits/stdc++.h>

using namespace std;

int main() {
	freopen("input.txt","r",stdin);

	//get input
	int n, m, g;
	cin >> n >> m >> g;

	vector<int> rain_time;
	for (int i = 0; i < n; i++) {
		int t;
		cin >> t;
		rain_time.push_back(t);
	}

	vector<int> dry_times;
	for (int i = 0; i < m; i++) {
		int d;
		cin >> d;
		dry_times.push_back(d);
	}

	int count = 0; //amount of clothes we can remove
	for (int s = 0; s < rain_time.size()-1; s++) {
		int time_before_rain = rain_time.at(s+1)-rain_time.at(s);
		for (int c = 0; c < dry_times.size(); c++) {
			if (dry_times.at(c) != 0 && dry_times.at(c) <= time_before_rain) {
				dry_times.at(c) = 0;
				count++;
			}
	 	}
	}

	cout << count << endl;

}