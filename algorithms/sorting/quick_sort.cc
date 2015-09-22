// Copyright 2015 David Gasquez

#include <cstdio>
#include <vector>
#include <algorithm>


template<typename T>
void swap(std::vector<T> *data, int a, int b) {
  T aux = data->at(a);
  data->at(a) = data->at(b);
  data->at(b) = aux;
}

template<typename T>
int partition(std::vector<T> *data, int start, int end) {
  // Classic pivot
  int pivot_value = data->at(end);
  int partition_index = start;
  for (int i = start; i < end; ++i) {
    if (data->at(i) < pivot_value) {
      swap(data, i, partition_index);
      partition_index++;
    }
  }
  swap(data, partition_index, end);
  return partition_index;
}

template<typename T>
void quick_sort(std::vector<T> *data, int start, int end) {
  if (start < end) {
    int partition_index = partition(data, start, end);
    quick_sort(data, start, partition_index - 1);
    quick_sort(data, partition_index + 1, end);
  }
}

int main(int argc, char const *argv[]) {
  // Initialize vector
  std::vector<int> data = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};

  // Shuffle vector
  std::random_shuffle(data.begin(), data.end());

  printf("Unsorted Array: ");
  for (const auto &element : data) {
    printf("%d ", element);
  }
  printf("\n");

  // Sort
  quick_sort(&data, 0, data.size() - 1);

  printf("Sorted Array: ");
  for (const auto &element : data) {
    printf("%d ", element);
  }
  printf("\n");

  return 0;
}
