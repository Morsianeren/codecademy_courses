#include "../include/profile.hpp" // Ensure this is the correct path to your profile.hpp

// Constructor
Profile::Profile() : age(0) {
    // Initialize members if needed
}

// Destructor
Profile::~Profile() {
    // Clean up if necessary (not needed here since we're not using dynamic memory)
}

// Setters
void Profile::SetName(std::string name) {
    _name = name;
}

std::string Profile::GetName(void) const {
    return _name;
}

void Profile::SetAge(int age) {
    this->age = age;
}

int Profile::GetAge(void) const {
    return age;
}

void Profile::SetCity(std::string city) {
    _city = city;
}

std::string Profile::GetCity(void) const {
    return _city;
}

void Profile::SetCountry(std::string country) {
    _country = country;
}

std::string Profile::GetCountry(void) const {
    return _country;
}

void Profile::SetPronouns(std::string pronouns) {
    _pronouns = pronouns;
}

std::string Profile::GetPronouns(void) const {
    return _pronouns;
}

// Hobby management
void Profile::AddHobby(std::string hobby) {
    // Add hobby to the list if it's not already present
    if (std::find(_hobbies.begin(), _hobbies.end(), hobby) == _hobbies.end()) {
        _hobbies.push_back(hobby);
    }
}

void Profile::RemoveHobby(std::string hobby) {
    // Remove the hobby if it exists in the list
    _hobbies.remove(hobby);
}

std::list<std::string> Profile::GetHobbies(void) const {
    return _hobbies;
}

std::string Profile::ViewProfile(void) {
    std::string profile = "Name: " + _name + "\n";
    profile += "Age: " + std::to_string(age) + "\n";
    profile += "City: " + _city + "\n";
    profile += "Country: " + _country + "\n";
    profile += "Pronouns: " + _pronouns + "\n";
    profile += "Hobbies:\n";
    for (const auto& hobby : _hobbies) {
        profile += " - " + hobby + "\n";
    }
    return profile;
}