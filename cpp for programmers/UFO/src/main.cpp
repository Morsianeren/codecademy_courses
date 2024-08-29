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

  // Task 7
  end_game(answer, codeword);

}
