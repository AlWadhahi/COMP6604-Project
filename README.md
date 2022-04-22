[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/alwadhahi/comp6604-project/main/app/app.py)



# COMP6604-Project

This repository will contain all relevant work for the project.

## Installing Packages
if you would like to run the project locally on your machine, then you need to download the dataset first then follow these steps: 

1. Make sure you have `Poetry` installed in your Environment (run `pip install Poetry`).
2. Once installed, you can now install the dependencies by running `poetry install`. 
3. Once your dependencies are installed, access the project's virtual environment by running `poetry shell`.
4. To run the app `streamlit run .\app\app.py`

## Repository Structure

- `\notebooks`: folder includes notebook that explores the data and builds the model
- `\trained_models`: folder includes the weights for the trained models
- `\app`: folder includes streamlit app that runs the project

## Dataset used

The dataset used for this experiment is [car-damage-dataset](https://github.com/neokt/car-damage-detective)