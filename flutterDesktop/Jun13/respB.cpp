                      
#include "flutter/encodable_value.h"
#include "flutter/method_channel.h"
#include <iostream>
#include <string>

// Using namespaces to simplify the code
using flutter::EncodableMap;
using flutter::EncodableValue;
using flutter::EncodableList;

int main() {
    // Step 2: Declare an EncodableMap
    EncodableMap my_map;

    // Step 3: Create and populate EncodableList 1
    EncodableList my_list1;
    my_list1.push_back(EncodableValue("item1"));
    my_list1.push_back(EncodableValue("item2"));
    
    // Create and populate EncodableList 2
    EncodableList my_list2;
    my_list2.push_back(EncodableValue(100));
    my_list2.push_back(EncodableValue(200));

    // Step 4: Add key-value pairs to EncodableMap
    my_map[EncodableValue("key1")] = EncodableValue(my_list1);
    my_map[EncodableValue("key2")] = EncodableValue(my_list2);

    // Printing the map to demonstrate
    for (const auto& pair : my_map) {
        // Assuming the keys are strings
        std::cout << "Key: " << std::get<std::string>(pair.first) << ", Values: [";
        
        // Assuming the values are EncodableLists
        for (const auto& value : std::get<EncodableList>(pair.second)) {
            if (value.IsString()) {
                std::cout << std::get<std::string>(value) << ", ";
            } else if (value.IsInt()) {
                std::cout << std::get<int>(value) << ", ";
            }
        }
        std::cout << "]" << std::endl;
    }

    return 0;
}