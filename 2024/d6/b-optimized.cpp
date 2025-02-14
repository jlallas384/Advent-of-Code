#include <bits/stdc++.h>
using namespace std;
int main() {
    vector<string> g;
    string s;
    while (cin >> s) {
        g.push_back(s);
    }
    int n = g.size(), m = g[0].size();
    vector<vector<vector<pair<int,int>>>> jumps(n, vector(m, vector<pair<int,int>>(4)));

    const vector<pair<int,int>> dirs = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

    auto ok = [n, m](int i, int j) {
        return 0 <= min(i, j) && i < n && j < m;
    };

    auto go = [&g, =](int i, int j) {

    };
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            int 
        }
    }
    
}