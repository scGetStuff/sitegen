#!/bin/bash

# i want a seperate dir for tests
# cd to src so test can import modules
cd src && python3 -m unittest discover -s ../tests
