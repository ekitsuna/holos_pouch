#include <bits/stdc++.h>
using namespace std;
//may need to use long
int main(){
  int N;
  int C;
  cin >> N >> C;
  int c[N];
  for (int n = 0; n < N; n++){ 
    string S;
    cin >> S;
    int cot = count(S.begin(), S.end(), 'M');
    c[n] = cot;
  }
  sort(c, c+N);
  int sum,cot = 0;
  for (int n = N-1; n >= 0; n++){
    sum += c[n];
    cot++;
    if (sum >= C){
      break;
    }
  }
  if (sum < C){
    cout << -1;
    return 0;
  }
  cout << cot;
}
