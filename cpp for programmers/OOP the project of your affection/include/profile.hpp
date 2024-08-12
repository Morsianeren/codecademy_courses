#ifndef PROFILE_HPP
#define PROFILE_HPP

#include <string>
#include <list>
#include <algorithm> // std::find

class Profile
{
public:
    Profile();
    ~Profile();	

    // Getters and setters
    void SetName(std::string name);
    std::string GetName(void) const;

    void SetAge(int age);
    int GetAge(void) const;
    
    void SetCity(std::string city);
    std::string GetCity(void) const;
    
    void SetCountry(std::string country);
    std::string GetCountry(void) const;
    
    void SetPronouns(std::string pronouns);
    std::string GetPronouns(void) const;
    
    // Hobby management
    void AddHobby(std::string hobby);
    void RemoveHobby(std::string hobby);
    std::list<std::string> GetHobbies(void) const;

    // Class information
    std::string ViewProfile(void);


private:
    std::string _name;
    int age;
    std::string _city;
    std::string _country;
    std::string _pronouns;
    std::list<std::string> _hobbies;

};

#endif //PROFILE_HPP