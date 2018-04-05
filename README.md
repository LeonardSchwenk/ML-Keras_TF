#### ML-Keras_TF

#!/bin/bash

counter=0

for file in *; do
    mv -i "$file" $((counter+1))banana.jpg && ((counter++))
done
