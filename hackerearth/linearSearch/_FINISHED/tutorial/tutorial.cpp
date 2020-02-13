#include <bits/stdc++.h>

using namespace std;

int main() {
	freopen("input.txt","r",stdin);

	int N, M;
	cin >> N >> M;

	int last_ind;
	for (int i = 1; i < N+1; i++) {
		int e;
		cin >> e;
		
		if (e == M) {
			last_ind = i;
		}
	}

	cout << last_ind << endl;


}