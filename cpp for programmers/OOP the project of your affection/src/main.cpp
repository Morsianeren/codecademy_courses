#include "iostream"

#include "../include/profile.hpp"

/// @brief Main function for running the application
/// @return 0 on success
int main(int argc, char **argv)
{
    Profile sam;
    sam.SetName("Same Drakilla");

    sam.SetAge(21);
    sam.SetCity("New York");
    sam.SetCountry("USA");
    sam.SetPronouns("He/Him");
    sam.AddHobby("Windsurfing");
    sam.AddHobby("Mountain biking");

    std::cout << sam.ViewProfile() << "\n";

    return 0;
}