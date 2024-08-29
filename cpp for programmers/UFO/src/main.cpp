#include <iostream>
#include "../include/ufo_functions.h"

int main() {

  // Task 2
  greet();

  // Task 3
  std::string codeword = "codecademy";
  std::string answer = "__________";
  
  // Task 10
  std::vector<char> incorrect;
  bool guess = false;

  // Task 4
  int misses = 0;

  // Task 5
  while((answer != codeword) && (misses < 7)) {

    // Task 9
    display_misses(misses);

    // Task 11
    std::cout << "Incorrect guesses:\n";
    for (auto iter: incorrect) {
      std::cout << iter << " ";
    }
    
    misses++;
  }

  // Task 7
  end_game(answer, codeword);

}
