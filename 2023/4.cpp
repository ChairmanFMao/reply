#include <bits/stdc++.h>
#include <fstream>
using namespace std;
#define ll long long
#define sz(c) (int)c.size()
#define all(c) c.begin(),c.end()
#define f first
#define s second

int main(void) {
    ofstream output("4output.txt");
    ifstream input("4input.txt");
	int tests;
	input >> tests;
	for (int test = 1; test <= tests; ++test) {
        cout << "test: " << test << "\n";
        int n, c, q;
        input >> n >> c >> q;
        vector<vector<char> > grid(n,vector<char>(n,' '));
        vector<int> minimum(5,INT_MAX);
        for (int i = 0; i < q; i++) {
            int x, y;
            char character;
            input >> x >> y >> character;
            grid[x][y] = character;
        }
        // This is just the starting position
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                map<char,int> current;
                // This is how far down we go
                for (int k = 0; k < n; k++) {
                    // This is how far over we go
                    for (int l = i; l <= j; l++)
                        if (grid[k][l] != ' ')
                            current[grid[k][l]] = k;
                    if (sz(current) == c) {
                        int smallest = INT_MAX;
                        for (auto ptr = current.begin(); ptr != current.end(); ptr++)
                            smallest = min(smallest,ptr->s);
                        int A = (k-smallest+1)*(j-i+1);
                        if (A < minimum[4])
                            minimum = {smallest,i,k,j,A};
                    }
                }
            }
        }

        string out = "";
        for (int i = 0; i < 5; i++)
            out += to_string(minimum[i]) + (i < 4 ? " " : "");

        output << "Case #" << test << ": " << out << "\n";   
    }

    output.close();
    input.close();
}

