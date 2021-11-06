# Table of Contents
<!-- no toc -->
- [1. Introduction](#1-introduction)
- [2. Preparing to run the sample codes](#2-preparing-to-run-the-sample-codes)
  - [2.1. Create virtual environment with Conda](#21-create-virtual-environment-with-conda)
  - [2.2. Create virtual environment with Python venv](#22-create-virtual-environment-with-python-venv)
  - [2.3. Install only the required Python modules and packages](#23-install-only-the-required-python-modules-and-packages)
- [3. Description of Python scripts](#3-description-of-python-scripts)


# 1. Introduction
This repository contains the Python script that demonstrates the implementation of a machine learning webapp using Streamlit.

# 2. Preparing to run the sample codes
1. Clone this repository or download the repository as a zip file.
2. If the repository is downloaded as a zip file, extract the zip file into its own folder.
3. Follow one of the methods below to create a virtual environment.

## 2.1. Create virtual environment with Conda
1. Follow this method if you have installed Anaconda.
2. Launch Anaconda Prompt.
3. Create a cirtual environment called py4iot with Python 3.9:
   - conda create -n streamlit_app python=3.9
4. After the virtual environment is created, activate it:
   - conda activate streamlit_app
5. Change to the folder with the extracted repository.
6. Install the required Python modules and packages:
   - python -m pip install -r requirements.txt
7. To deactivate the virtual environment:
   - conda deactivate

## 2.2. Create virtual environment with Python venv
1. Launch a terminal/command prompt.
2. Change to the folder with the extracted repository.
3. Create a virtual environment:
    - python -m venv env
4. Once the virtual environment has been created, there will be a folder called "env" in the current folder.
5. To activate the virtual environment in Windows:
   - cd env\Scripts
   - activate
   - cd ..\\..
6. To active the virtual environment in Linux:
   - souce env/bin/activate
7. Install the required Python modules and packages:
   - python -m pip install -r requirements.txt
8. To deactive the virtual environment in Windows or Linux:
   - deactivate

## 2.3. Install only the required Python modules and packages
1. Follow this method if you do not wish to create a virtual environment.
2. Launch a terminal/command prompt.
3. Install the required Python modules and packages:
   - python -m pip install numpy scipy scikit-learn streamlit

# 3. Description of Python scripts
1. The following table lists the Python scripts in this repository and describes their roles.
   | Filename       | Description                                               |
   | :------------- | :-------------------------------------------------------- |
   | train_model.py | Train a logistic regression model and save it             |
   | webapp.py      | Launch a webapp for classiciation using the trained model |
2. To train the model, download the dataset from the following link and save in the same folder as the Python scripts.
   https://raw.githubusercontent.com/wooihaw/datasets/main/heights_weights_genders.csv
3. To launch the webapp:
   - streamlit run webapp.py