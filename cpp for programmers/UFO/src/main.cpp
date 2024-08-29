#include <iostream>
#include "../include/ufo_functions.h"

int main() {

  // Task 2
  greet();

  // Task 3
  std::string codeword = "codecademy";
  std::string answer = "__________";

  // Task 4
  int misses = 0;

  // Task 5
  while((answer != codeword) && (misses < 7)) {


    misses++;
  }

  // Task 6
  if (answer == codeword) {
    std::cout << "Hooray! You saved the person and earned a medal of honor!\n";
  } else {
    std::cout << "Oh no! The UFO just flew away with another person!\n";
  }

}
