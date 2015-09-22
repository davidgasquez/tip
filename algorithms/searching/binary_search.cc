// Copyright 2015 David Gasquez

#include <cstdio>
#include <vector>
#include <algorithm>

template<typename T>
int binary_search(const std::vector<T> &data, T value) {
  unsigned start = 0, end = data.size() - 1;

  while (start <= end) {
    unsigned middle = (start + end) / 2;
    if (value == data[middle]) {
      return middle;
    } else if (value < data[middle]) {
      end = middle - 1;
    } else {
      start = middle + 1;
    }
    return -1;
  }
}

int main(int argc, char const *argv[]) {
  // Initialize vector
  std::vector<int> data = {1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};

  int position = binary_search(data, 4);
  printf("The number %d it's at position %d.\n", 4, position);

  position = binary_search(data, 3);
  if (position < 0) {
    printf("Number %d not found.\n", 3);
  }

  return 0;
}
