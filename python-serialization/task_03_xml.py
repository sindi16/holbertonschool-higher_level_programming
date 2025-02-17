#!/usr/bin/env python3
"""
This script provides functions to serialize a Python dictionary to an XML file
and deserialize an XML file back to a Python dictionary.
"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Parameters:
    dictionary (dict): The Python dictionary to serialize.
    filename (str): The filename of the output XML file.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.Element(key)
        child.text = str(value)  # Ensure the value is a string
        root.append(child)
    tree = ET.ElementTree(root)

    with open(filename, 'wb') as f:
        tree.write(f)
    print(f"Data serialized and saved to '{filename}'.")


def deserialize_from_xml(filename):
    """
    Load and deserialize an XML file to a Python dictionary.

    Parameters:
    filename (str): The filename of the input XML file.

    Returns:
    dict: The deserialized Python dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    my_dict = {}

    for child in root:
        my_dict[child.tag] = child.text
    return my_dict
