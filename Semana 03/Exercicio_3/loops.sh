MY_FIRST_LIST=(one two three four five)

for item in ${MY_FIRST_LIST[@]}; do echo -n $item | wc -c; done
