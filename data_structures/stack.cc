// Copyright 2015 David Gasquez

#include <cstdio>
#include <stack>

int main(int argc, char const *argv[]) {
  std::stack<int> int_stack;

  // Fill the stack
  for (int i = 1; i < 6; ++i) {
    int_stack.push(i);
  }

  // Stack size
  printf("Stack size: %lu \n", int_stack.size());

  // Acess top element and pop it out
  printf("Elements: ");
  for (int i = 0; i < 5; ++i) {
    printf("%d ", int_stack.top());
    int_stack.pop();
  }
  printf("\n");

  return 0;
}
