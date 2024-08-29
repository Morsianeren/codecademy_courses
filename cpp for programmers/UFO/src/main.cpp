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

  // Task 14
  char letter;

  // Task 5
  while((answer != codeword) && (misses < 7)) {

    // Task 9
    display_misses(misses);

    // Task 13
    display_status(&incorrect, &answer);

    // Task 14
    std::cout << "Please enter your guess:\n";
    std::cin >> letter;

    // Task 15 & 16
    char c;
    for (int i = 0; i < codeword.length(); i++) {
      c = codeword[i];
      if (c == letter) {
        guess = true;
        answer[i] = letter;
      }
    }

    // Task 17
    if (guess == true) {
      std::cout << "Correct!\n";
    }
    else {
      std::cout << "Incorrect! The tractor beam pulls the person in further.\n";
      incorrect.push_back(letter);
    }

    misses++;
  }

  // Task 7
  end_game(answer, codeword);

}
