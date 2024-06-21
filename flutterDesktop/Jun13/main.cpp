#include "flutter/encodable_value.h"
#include <iostream>
#include <string>
#include <variant>

using flutter::EncodableMap;
using flutter::EncodableValue;
using flutter::EncodableList;

int main() {
    EncodableMap my_map;

    EncodableList my_list1;
    my_list1.push_back(EncodableValue("item1"));
    my_list1.push_back(EncodableValue("item2"));

    EncodableList my_list2;
    my_list2.push_back(EncodableValue(100));
    my_list2.push_back(EncodableValue(200));

    my_map[EncodableValue("key1")] = EncodableValue(my_list1);
    my_map[EncodableValue("key2")] = EncodableValue(my_list2);

    for (const auto& pair : my_map) {
        // Assuming the keys are strings
        std::cout << "Key: " << std::get<std::string>(pair.first) << ", Values: [";

        // Assuming the values are EncodableLists
        const EncodableList& list = std::get<EncodableList>(pair.second);
        for (const auto& value : list) {
            if (std::holds_alternative<std::string>(value)) {
                std::cout << std::get<std::string>(value) << ", ";
            } else if (std::holds_alternative<int>(value)) {
                std::cout << std::get<int>(value) << ", ";
            }
        }
        std::cout << "]" << std::endl;
    }

    return 0;
}
