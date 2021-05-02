

![](https://github.com/napoles-uach/Nanostring/blob/main/variationred.png?raw=true)
 # Project for the Nanostring Hackaton
 
 ## How to run this?
 Try the badge 
 [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/napoles-uach/nanostring/main/kidney_app.py)

or 

 download the files:
 * [kidney_app.py](https://raw.githubusercontent.com/napoles-uach/Nanostring/main/kidney_app.py)
 * [utils.py](https://raw.githubusercontent.com/napoles-uach/Nanostring/main/utils.py)
 * [requirements.txt](https://raw.githubusercontent.com/napoles-uach/Nanostring/main/requirements.txt)
 * [variationred.png](https://github.com/napoles-uach/Nanostring/blob/main/variationred.png?raw=true)
 * [variation.png](https://github.com/napoles-uach/Nanostring/blob/main/variation.png?raw=true)

You must also have on the same folde where the above files are stored the following files which are part of the dataset provided:

* [Kidney_Sample_Annotations.csv](https://raw.githubusercontent.com/napoles-uach/Nanostring/main/Kidney_Sample_Annotations.csv)
* [Kidney_Q3Norm_TargetCountMatrix.csv](https://raw.githubusercontent.com/napoles-uach/Nanostring/main/Kidney_Q3Norm_TargetCountMatrix.csv)




 ```
pipenv three
pipenv shell
pip3 install -r requirements.txt
streamlit run kidney_app.py
 ```
 
 
 
 
