#include <vector>

using namespace std;

vector<vector<int>> multiplication_table(int n){
  std::vector<std::vector<int>> matrix;
  for (int i  = 1; i <= n; i++){
    std::vector<int> v;
    for (int j = 1; j <= n; j++) {
      v.push_back((i) * (j));
    }
    matrix.push_back(v);
  }
  return matrix;
}
