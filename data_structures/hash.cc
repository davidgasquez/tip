// Copyright 2015 David Gasquez

#include <cstdio>
#include <unordered_map>

int main(int argc, char const *argv[]) {
  // Map creation
  std::unordered_map<int, int> count_map = {
    {1, 1},
    {2, 11},
    {3, 111},
    {4, 1111}
  };

  // Map size
  printf("The map size is %lu\n", count_map.size());

  // Access keys and values
  for (auto &element : count_map) {
    printf("%i -> %i\n", element.first, element.second);
  }

  // Insert new elements
  count_map.insert({5, 11111});

  std::pair<int, int> new_element(9, 111111111);
  count_map.insert(new_element);

  // Find by key
  auto key_position = count_map.find(3);
  if (key_position == count_map.end()) {
    printf("Key not found\n");
  } else {
    printf("Found: %i -> %i\n", key_position->first, key_position->second);
  }

  // Modify a pair
  count_map[key_position->first] = 101;
  printf("New value: %i -> %i\n", key_position->first, key_position->second);

  // Remove pair
  count_map.erase(3);

  // Print map
  printf("Final map: \n");
  for (auto &element : count_map) {
    printf("%i -> %i\n", element.first, element.second);
  }

  return 0;
}
