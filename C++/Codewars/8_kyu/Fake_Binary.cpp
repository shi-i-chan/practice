#include <string>
#include <map>


std::string fakeBin(std::string s){
    char r;
    std::map<char, char> rs = { {'1', '0'}, {'2', '0'}, {'3', '0'}, {'4', '0'}, {'5', '1'}, {'6', '1'}, {'7', '1'}, {'8', '1'}, {'9', '1'} };
    std::replace_if(s.begin(), s.end(), [&](char c){ return r = rs[c]; }, r);
    return s;
}
