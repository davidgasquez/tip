// Copyright 2015 David Gasquez

#include <cstdio>
#include <vector>
#include <algorithm>

template<typename T>
void merge(const std::vector<T> &left, const std::vector<T> &right,
           std::vector<T> *data) {
  // Calculate sizes
  unsigned size_left = left.size();
  unsigned size_right = right.size();

  unsigned left_iterator = 0, right_iterator = 0, data_iterator = 0;

  // Compare the values and merge
  while (left_iterator < size_left && right_iterator < size_right) {
    if (left[left_iterator] <= right[right_iterator]) {
      data->at(data_iterator) = left[left_iterator];
      left_iterator++;
    } else {
      data->at(data_iterator) = right[right_iterator];
      right_iterator++;
    }
    data_iterator++;
  }

  // Add the remaining data
  while (left_iterator < size_left) {
    data->at(data_iterator) = left[left_iterator];
    left_iterator++;
    data_iterator++;
  }

  // Add the remaining data
  while (right_iterator < size_right) {
    data->at(data_iterator) = right[right_iterator];
    right_iterator++;
    data_iterator++;
  }
}

template<typename T>
void merge_sort(std::vector<T> *data) {
  unsigned data_size = data->size();

  if (data_size < 2) {
    return;
  }

  // Determine the location of the middle element in the vector
  auto middle = data->begin() + (data_size / 2);

  std::vector<T> left(data->begin(), middle);
  std::vector<T> right(middle, data->end());

  // Sort recursively and merge into data
  merge_sort(&left);
  merge_sort(&right);
  merge(left, right, data);
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
  merge_sort(&data);

  printf("Sorted Array: ");
  for (const auto &element : data) {
    printf("%d ", element);
  }
  printf("\n");

  return 0;
}
