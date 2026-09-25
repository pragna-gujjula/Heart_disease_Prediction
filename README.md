# Heart_disease_Prediction
# ❤️ Heart Disease Prediction Using Logistic Regression

## 📌 Project Overview

Heart Disease Prediction is a Machine Learning project that predicts whether a person is likely to have heart disease based on various medical attributes.

This project uses **Logistic Regression**, a supervised machine learning classification algorithm, to analyze patient data and predict the presence or absence of heart disease.

The model is trained using the Heart Disease Dataset obtained from Kaggle. The project includes data preprocessing, exploratory data analysis, model training, evaluation, and deployment using Flask and Render.

## 🎯 Objectives

* To develop a machine learning model for heart disease prediction.
* To preprocess and analyze the dataset.
* To visualize important patterns and relationships in the data.
* To train a Logistic Regression classification model.
* To evaluate the model's performance using suitable metrics.
* To deploy the trained model as a web application.
* To provide a user-friendly interface for making predictions.

## 🛠️ Technologies Used

| Technology          | Purpose                   |
| ------------------- | ------------------------- |
| Python              | Programming Language      |
| Pandas              | Data Manipulation         |
| NumPy               | Numerical Computation     |
| Matplotlib          | Data Visualization        |
| Seaborn             | Statistical Visualization |
| Scikit-learn        | Machine Learning          |
| Logistic Regression | Classification Algorithm  |
| Flask               | Web Application Framework |
| HTML                | Frontend Structure        |
| CSS                 | Frontend Styling          |
| Render              | Cloud Deployment          |
| GitHub              | Version Control           |


### Input Features

* Age
* Sex
* Chest Pain Type (cp)
* Resting Blood Pressure (trestbps)
* Cholesterol (chol)
* Fasting Blood Sugar (fbs)
* Resting Electrocardiographic Results (restecg)
* Maximum Heart Rate Achieved (thalach)
* Exercise-Induced Angina (exang)
* ST Depression (oldpeak)
* Slope
* Number of Major Vessels (ca)
* Thalassemia (thal)

### Target Variable

* **Target = 0:** No heart disease
* **Target = 1:** Heart disease present

*The target interpretation should be verified against the dataset and preprocessing code.*

## 🔍 Exploratory Data Analysis (EDA)

Exploratory Data Analysis is performed to understand the dataset, identify patterns, and analyze relationships between medical attributes and the target variable.

### Data Analysis Includes

* Checking dataset shape and structure.
* Identifying missing values.
* Analyzing statistical information.
* Checking the distribution of heart disease cases.
* Understanding relationships between numerical features.
* Identifying patterns in medical attributes.

### 📊 Data Visualization

The following graphs can be used to understand the dataset:

**1. Heart Disease Distribution**

A count plot showing the number of patients with and without heart disease.

**2. Age Distribution**

A histogram showing the age distribution of patients in the dataset.

**3. Correlation Heatmap**

A heatmap showing the correlation between different medical features.

**4. Cholesterol Distribution**

A graph showing cholesterol levels among patients.

**5. Maximum Heart Rate Analysis**

A visualization of the relationship between maximum heart rate and heart disease outcomes.

**6. Confusion Matrix**

A heatmap showing the actual and predicted classification results of the model.

> 📌 Add your actual graph screenshots to the README if you generated them in your Jupyter Notebook or Python code.

## 🧠 Machine Learning Algorithm

### Logistic Regression

Logistic Regression is a supervised machine learning algorithm used for binary classification problems.

In this project, Logistic Regression predicts whether a patient has heart disease or not based on medical input features.

The algorithm estimates the probability of a particular class and uses a classification threshold to generate the final prediction.

### Logistic Regression Workflow

1. Load the dataset.
2. Separate independent and dependent variables.
3. Split the dataset into training and testing sets.
4. Train the Logistic Regression model.
5. Predict outcomes for test data.
6. Evaluate the model using classification metrics.
7. Save the trained model for deployment.

## ⚙️ Project Workflow

```text
Dataset Collection
       ↓
Data Preprocessing
       ↓
Exploratory Data Analysis
       ↓
Feature Selection
       ↓
Train-Test Split
       ↓
Logistic Regression Model
       ↓
Model Evaluation
       ↓
Save Trained Model
       ↓
Flask Web Application
       ↓
Render Deployment
       ↓
Heart Disease Prediction
```

## 📊 Model Evaluation

The model performance can be evaluated using the following metrics:

### Accuracy

Measures the proportion of correct predictions out of all predictions.

### Precision

Measures how many predicted positive cases are actually positive.

### Recall

Measures how many actual positive cases are correctly identified.

### F1-Score

Combines precision and recall into a single metric.

### Confusion Matrix

Displays the number of true positives, true negatives, false positives, and false negatives.

> **Note:** Add your actual model accuracy and evaluation results after training. Do not assume a performance value without measuring it.

## 💻 Web Application

The project includes a Flask-based web application that allows users to enter medical information and receive a model-generated prediction.

### Application Features

* User-friendly input form.
* Patient medical feature collection.
* Trained Logistic Regression model integration.
* Prediction result display.
* HTML and CSS-based interface.
* Web deployment using Render.

## 🚀 How to Run the Project Locally

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Folder

```bash
cd heart-disease-prediction
```

### 3. Create a Virtual Environment (Optional)

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 5. Install Required Libraries

```bash
pip install pandas numpy scikit-learn flask matplotlib seaborn
```

### 6. Run the Application

```bash
python app.py
```

Open the local application URL in your browser:

```text
http://127.0.0.1:5000/
```

## ☁️ Deployment Using Render

The Flask application is deployed using **Render**, a cloud platform for hosting web applications.

### Deployment Steps

1. Push the project code to GitHub.
2. Create a new Web Service on Render.
3. Connect the GitHub repository.
4. Configure the build and start commands.
5. Deploy the application.
6. Access the live application using the Render URL.

### Deployment Configuration

**Build Command:**

```bash
pip install -r requirements.txt
```

**Start Command (Example):**

```bash
gunicorn app:app
```

> Ensure that Gunicorn is included in `requirements.txt` and that your Flask application uses the correct entry point.

## 🔮 Project Output

The application accepts patient medical information and provides a model-based prediction of whether heart disease is present or absent.

The deployed application allows users to access the prediction system through a web browser.


### 🔗 Connect With Me

* **LinkedIn:** [Your LinkedIn Profile](YOUR_LINKEDIN_PROFILE_URL)
* **GitHub:** [Your GitHub Profile](YOUR_GITHUB_PROFILE_URL)



## 🔗 Project Links

### 📊 Dataset

[Heart Disease Dataset – Kaggle](https://www.kaggle.com/datasets/yasserh/heart-disease-dataset)

### 💻 GitHub Repository

[View Source Code on GitHub](YOUR_GITHUB_REPOSITORY_URL)

### 🌐 Live Deployment

[Click Here to Use the Heart Disease Prediction App](YOUR_RENDER_DEPLOYMENT_URL)

### 🔗 LinkedIn

[Connect With Me on LinkedIn](YOUR_LINKEDIN_PROFILE_URL)
