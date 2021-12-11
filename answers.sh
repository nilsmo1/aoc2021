#!/bin/sh
TODAY=$(date | awk '{print $3}')
echo "Answers for Advent of Code, Days: 1 - $TODAY!"
for day in `seq 1 $TODAY`;
do
    if [ $day -lt 10 ]; 
    then
        D="0$day"
    else
        D=$day
    fi

    cd "day$D" > /dev/null 2>&1 || exit 1
    echo "DAY $day"
    ANSWERS=$(python3 $D.py)
    echo $(echo $ANSWERS | awk '{print $1, $2}') 
    echo $(echo $ANSWERS | awk '{print $3, $4}')
    echo 
    cd ..
done
