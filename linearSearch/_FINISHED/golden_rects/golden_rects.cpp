#include <bits/stdc++.h>

using namespace std;

int main() {
	freopen("input.txt","r",stdin);
	int n;
	cin >> n;

	int count = 0;
	for (int i = 0; i < n; i++) {
		double w, h;
		cin >> w >> h;

		double ratio = w >= h ? w/h : h/w;
		
		if (1.6 <= ratio && ratio <= 1.7) {
			count++;
		}
	}

	cout << count << endl;

}