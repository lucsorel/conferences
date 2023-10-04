#!/bin/bash
start=$(date +%s.%N)

exec_times="${EXEC_TIMES:-10}"
# performs multiple times the command passed as an argument
for ((i=1; i<=$exec_times; i++)); do eval "$@"; done

stop=$(date +%s.%N)
duration=$(echo "scale=3; ($stop - $start) / 1" | bc -l)

echo "Command '$@' executed $exec_times times in $duration seconds"
