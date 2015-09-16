// Copyright 2015 David Gasquez

#include <random>
#include <cstdio>
#include <vector>
#include <algorithm>

template<class TYPE>
std::vector<TYPE> insertion_sort(std::vector<TYPE> data) {
  unsigned data_size = data.size();

  for (unsigned i = 1; i < data_size; ++i) {
    TYPE value = data[i];
    unsigned hole = i;

    // Put the value in the sorted sub-array. While it founds a number grater
    // than value it moves the "hole" one place to the right.
    while (hole > 0 && data[hole - 1] > value) {
      data[hole] = data[hole - 1];
      hole = hole - 1;
    }
    data[hole] = value;
  }

  return data;
}

int main(int argc, char const *argv[]) {
  // Initialize vector
  std::vector<int> data = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};

  // Shuffle vector
  auto engine = std::default_random_engine {};
  std::shuffle(std::begin(data), std::end(data), engine);

  printf("Unsorted Array: ");
  for (auto element : data) {
    printf("%d ", element);
  } printf("\n");

  // Sort
  std::vector<int> sorted = insertion_sort(data);

  printf("Sorted Array: ");
  for (auto element : sorted) {
    printf("%d ", element);
  } printf("\n");

  return 0;
}
