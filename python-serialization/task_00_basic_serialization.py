#!/usr/bin/env python3
import json
def serialize_and_save_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    with open(filename, 'r') as file:
        return json.load(file)

if __name__ == '__main__':
    data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}


serialize_and_save_to_file(data_to_serialize, 'data.json')

print("Data serialized and saved to 'data.json'.")

deserialized_data = load_and_deserialize('data.json')

print("Deserialized Data:")
print(deserialized_data)
