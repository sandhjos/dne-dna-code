#!/usr/bin/env python
"""Working with nested data hands-on exercise / coding challenge."""

import json
import os

# Get the absolute path for the directory where this file is located "here"
from pprint import pprint

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "interfaces.json")) as file:
    # TODO: Parse the contents of the JSON file into a variable
    outputStr = file.read(0)

# TODO: Loop through the interfaces in the JSON data and print out each
outputData = json.loads(outputStr)
# interface's name, ip, and netmask.
pprint(outputData)
