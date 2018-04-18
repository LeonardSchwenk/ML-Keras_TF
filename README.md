#### ML-Keras_TF

folder test_data has one image per categorie, to test a trained model.

## GreenCycle_v2.0_8_categoreis.ipynb 

This notebook used old Keras version code and took really long for training and had also a bad acc

## GreenCycle_v3.0_8_categoreis.ipynb

Code adjustments with new keras version way better, trained 8 categories with ~6600 images for 50 epoches.


## bash_script for renaming files in a folder for training 
#!/bin/bash

counter=0

for file in *; do
    mv -i "$file" $((counter+1))banana.jpg && ((counter++))
done

execute this as a script in a folder --> 

/banana
    /1banana.jpg
    /2banana.jpg
    ...
    /1300banana.jpg
    ...
