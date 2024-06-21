#include "flutter/encodable_value.h"
#include <iostream>
#include <string>
#include <vector>


// Function to dynamically add pairs of string key and EncodableList into EncodableMap
flutter::EncodableMap CreateEncodableMapWithStringKeyAndEncodableList(
    const std::vector<std::pair<std::string, flutter::EncodableList>>& data) {

  flutter::EncodableMap encodableMap;

  for (const auto& pair : data) {
    encodableMap[flutter::EncodableValue(pair.first)] =
        flutter::EncodableValue(pair.second);
  }

  return encodableMap;
}

int main() {
std::vector<std::pair<std::string, flutter::EncodableList>> data = {
    {"key1", flutter::EncodableList{1, 2, 3}},
    {"key2", flutter::EncodableList{"a", "b", "c"}},
};

flutter::EncodableMap encodableMap =
    CreateEncodableMapWithStringKeyAndEncodableList(data);
    

  // Print the map to demonstrate
  for (const auto& pair : encodableMap) {
    std::cout << "Key: " << std::get<std::string>(pair.first) << ", Values: [";
    const flutter::EncodableList& list = std::get<flutter::EncodableList>(pair.second);
    for (const auto& value : list) {
      if (std::holds_alternative<int>(value)) {
        std::cout << std::get<int>(value) << ", ";
      } else if (std::holds_alternative<std::string>(value)) {
        std::cout << std::get<std::string>(value) << ", ";
      }
    }
    std::cout << "]" << std::endl;
  }
return 0;
}