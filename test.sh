#!/bin/bash

# i want a seperate dir for tests
# i do the stupid cd stuff so test can import modules in src
cd src
python3 -m unittest discover -s ../tests
cd ..