#include <bits/stdc++.h>
using namespace std;
#define ll long long

// Just inputs for this thing are really annoying
// This solution is just finding the gcd of all the numbers
// And then finding how many factors that gcd has.

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    fstream f;
    f.open("1input.txt");

    ll t;
    f >> t;
    for (ll c = 1; c <= t; ++c) {
        ll n;
        f >> n;
        ll out = 0;
        for (ll i = 0,a; i < n; i++) {
            f >> a;
            if (!out) {
                out = a;
                continue;
            }
            out = __gcd(out,a);
        }

        ll factors = 1;
        while (out % 2 == 0) {
            factors++;
            out /= 2;
        }
        ll start = out;
        for (ll i = 3, current; i <= start && out != 1; i+=2) {
            current = 1;
            while (out % i == 0) {
                current++;
                out /= i;
            }
            factors *= current;
        }

        cout << "Case #" << c << ": " << factors << "\n";
    }
    f.close();
}
 