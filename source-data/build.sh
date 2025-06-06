#!/usr/bin/env bash
set -euxo pipefail

for n in 6
do
    for p in 1.5 2.0 2.5
    do
        python processWordlist.py $n $p --safe > ../lists/words-$n-$p.txt
    done
done
