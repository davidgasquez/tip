// Copyright 2015 David Gasquez

#include <cstdio>
#include <vector>
#include <algorithm>

template<typename T>
void insertion_sort(std::vector<T> *data) {
  unsigned data_size = data->size();

  for (unsigned i = 1; i < data_size; ++i) {
    T value = data->at(i);
    unsigned hole = i;

    // Put the value in the sorted sub-array. While it founds a number grater
    // than value it moves the "hole" one place to the right.
    while (hole > 0 && data->at(hole - 1) > value) {
      data->at(hole) = data->at(hole - 1);
      hole = hole - 1;
    }
    data->at(hole) = value;
  }
}

int main(int argc, char const *argv[]) {
  // Initialize vector
  std::vector<int> data = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};

  // Shuffle vector
  std::random_shuffle(data.begin(), data.end());

  printf("Unsorted Array: ");
  for (auto element : data) {
    printf("%d ", element);
  }
  printf("\n");

  // Sort
  insertion_sort(&data);

  printf("Sorted Array: ");
  for (auto element : data) {
    printf("%d ", element);
  }
  printf("\n");

  return 0;
}
