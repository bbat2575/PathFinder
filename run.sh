#! /usr/bin/env bash

echo "Select graph:"
echo "- graph8"
echo "- graph250"
echo "- graph1000"

read option

if [ $option -eq 1 ]; then
    python3 pathfinder.py < graphs/graph8.in
elif [ $option -eq 2 ]; then
    python3 pathfinder.py < graphs/graph250.in
elif [ $option -eq 3 ]; then
    python3 pathfinder.py < graphs/graph1000.in
fi

