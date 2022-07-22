#include <bits/stdc++.h>
#include <fstream>
using namespace std;
#define ll long long

// To deal with the negative numbers we need for:
// min - largest pos * smallest neg, or if both pos just smallest product, or both neg, just smallest product
// max - max(largest neg * second largest neg, largest pos, second largest pos)
// with two pointers for each end of the vector

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    fstream in;
    in.open("3in.txt");
    ofstream out;
    out.open("3out.txt");

    ll t, r = 0;
    in >> t;
    while (t - r++) {
        ll n, k;
        in >> n >> k;
        vector<ll> an, ap, bn, bp;
        for (int i = 0,a; i < n; i++) {
            in >> a;
            if (a >= 0)
                ap.push_back(a);
            else
                an.push_back(a);
        }
        for (int i = 0,b; i < n; i++) {
            in >> b;
            if (b >= 0)
                bp.push_back(b);
            else
                bn.push_back(b);
        }
        
        sort(ap.begin(),ap.end());
        sort(bp.begin(),bp.end());
        sort(an.begin(),an.end());
        sort(bn.begin(),bn.end());
        ll small = 0, app = 0, bpp = 0, anp = 0, bnp = 0, current;
        for (ll i = 0; i < k; i++) {
            current = LLONG_MAX;
            if (app < (ll)ap.size() && )
        }
        
        ll big = 0;
        for (ll i = 0; i < k; i++)
            big += a[i] * b[i];
        
        out << "Case #" << r << ": " << small << " " << big;
        if (t-r)
            out << "\n";
    }

    in.close();
    out.close();
}
