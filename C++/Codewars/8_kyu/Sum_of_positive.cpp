#include <vector>

int positive_sum (const std::vector<int> arr){
  int sum = 0;
  for (int i = 0; i < size(arr); i++){
    if (arr[i] > 0) sum += arr[i];
  }
  return sum;
}
