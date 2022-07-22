#include <bits/stdc++.h>
#include <fstream>
using namespace std;
#define ll long long

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    fstream in;
    in.open("");
    ofstream out;
    out.open("");

    ll t, r = 0;
    in >> t;
    while (t - r++) {
        out << "Case #" << r << ": ";
    }

    in.close();
    out.close();
}
