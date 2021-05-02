

![](https://github.com/napoles-uach/Nanostring/blob/main/variationred.png?raw=true)
 # Project for the Nanostring Hackaton
 
 ## How to run this?
 Try the badge 
 
 [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/napoles-uach/nanostring/main/kidney_app.py)

or 

If you are not familiar with github, just download as a Zip file the whole project in the green button (with the leyend "Code") at the top of this page. As the code works with a large set of images, this would be a large file (about 1.7 Gb), so be patient.  

Once you have downloaded and uncompressed the ZIP file, go to your terminal and type
```
pipenv three
pipenv shell
pip3 install -r requirements.txt
streamlit run kidney_app.py
 ```


Besides this, the code is in the following two files:

 * [kidney_app.py](https://raw.githubusercontent.com/napoles-uach/Nanostring/main/kidney_app.py)
 * [utils.py](https://raw.githubusercontent.com/napoles-uach/Nanostring/main/utils.py)

and uses python libraries in the requirements file:

* [requirements.txt](https://raw.githubusercontent.com/napoles-uach/Nanostring/main/requirements.txt)

and also this two images:
 * [variationred.png](https://github.com/napoles-uach/Nanostring/blob/main/variationred.png?raw=true)
 * [variation.png](https://github.com/napoles-uach/Nanostring/blob/main/variation.png?raw=true)

You will find in the same folder where the above files are stored the following files which are part of the dataset provided:

* [Kidney_Sample_Annotations.csv](https://raw.githubusercontent.com/napoles-uach/Nanostring/main/Kidney_Sample_Annotations.csv)
* [Kidney_Q3Norm_TargetCountMatrix.csv](https://raw.githubusercontent.com/napoles-uach/Nanostring/main/Kidney_Q3Norm_TargetCountMatrix.csv)

and the ROI folder. Be careful. The order of the files in the ROI folder is important so please don't modify it!!



 
 
 
 
 
