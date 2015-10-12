// Copyright 2015 David Gasquez

#include <cstdio>

struct Node {
  int data;
  Node *left;
  Node *right;
  Node(int data): data(data), left(nullptr), right(nullptr) {}
};

void print_tree_post_order(Node *tree) {
  if (tree->left != nullptr) {
    print_tree_post_order(tree->left);
  }
  if (tree->right != nullptr) {
    print_tree_post_order(tree->right);
  }
  printf("%i ", tree->data);
  printf("\n");
}

int main(int argc, char const *argv[]) {
  Node *node = new Node(3);

  Node *node_left = new Node(2);
  node->left = node_left;
  Node *node_right = new Node(9);
  node->right = node_right;

  print_tree_post_order(node);

  return 0;
}
