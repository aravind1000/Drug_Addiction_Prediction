# Student Drug Addiction Prediction

This project aims to predict whether a student is likely to develop a drug addiction based on various factors such as age, gender, academic performance, attendance, social influence, behavioral issues, family background, and stress level. The prediction is made using a logistic regression model.

## Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Web Application](#web-application)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

The project consists of two main components:
1. **Model Training**: A logistic regression model is trained using a dataset of student information.
2. **Web Application**: A Flask-based web application that allows users to input student data and receive a prediction about the likelihood of drug addiction.

## Dataset

The dataset used for this project is assumed to be in a CSV file named `students_data.csv` and contains the following columns:
- `age`: Age of the student
- `gender`: Gender of the student (Male/Female)
- `academic_performance`: Academic performance score
- `attendance`: Attendance percentage
- `social_influence`: Score indicating the level of social influence
- `behavioral_issues`: Binary indicator of behavioral issues (0 or 1)
- `family_background`: Binary indicator of family background (0 or 1)
- `stress_level`: Stress level score
- `drug_addiction`: Target variable indicating if the student has developed drug addiction (0 or 1)

## Model Training

The model is trained using the Logistic Regression algorithm. The training script performs the following steps:
1. Loads and preprocesses the data.
2. Scales the features using `StandardScaler`.
3. Splits the data into training and testing sets.
4. Trains a Logistic Regression model.
5. Evaluates the model using accuracy, precision, recall, and F1 score.
6. Saves the trained model and scaler using `joblib`.

## Web Application

The web application is built using Flask. It provides an interface for users to input student data and receive a prediction. The app performs the following steps:
1. Accepts user input from a form.
2. Preprocesses and scales the input data.
3. Uses the trained model to make a prediction.
4. Displays the prediction result to the user.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/aravind1000/Drug_Addiction_Prediction.git
    cd Drug_Addiction_Prediction
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

5. Place the dataset (`students_data.csv`) in the project directory.

6. Run the model training script:
    ```bash
    python model_training.py
    ```

## Usage

To start the web application, run the following command:
```bash
python drug_addiction_prediction.py
