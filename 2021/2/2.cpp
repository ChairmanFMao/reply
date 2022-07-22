#include <bits/stdc++.h>
#include <fstream>
using namespace std;
#define ll long long

// I think that this brute force solution will work for smaller inputs
// For larger ones I need to identify cycles in the successor graph and
// determine the length fo the cycle and do k mod it to reduce operations.
// The brute force solution works for every input except the last
// Need to determine cycle length quickly and efficiently for all items.
// The evaluation is silly and wants no \n at the end of the last line

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    fstream in;
    in.open("2input.txt");
    ofstream out;
    out.open("2out.txt");

    ll t, r = 1;
    in >> t;
    while (r <= t) {
        ll n, k;
        in >> n >> k;
        vector<ll> numbers(n), output(n), cycle(n);
        for (ll& i : numbers)
            in >> i;
        
        for (ll i = 0; i < n; i++) {
            ll start = i, moving = numbers[i], moves = 1;
            while (moving != start) {
                moving = numbers[moving];
                moves++;
            }
            cycle[i] = k % moves;
        }
        
        for (int j = 0; j < n; j++) {
            ll pos = j;
            for (int i = 0; i < cycle[j]; i++)
                pos = numbers[pos];
            output[pos] = j;
        }

        out << "Case #" << r << ": ";
        for (ll i : output)
            out << i << " ";
        if (r != t) 
            out << "\n";
        r++;
    }

    in.close();
    out.close();
}
