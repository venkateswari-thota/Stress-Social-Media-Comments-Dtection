# Stress Detection from Social Media Comments 💬🧠  
This project leverages machine learning to detect **stress-related content** in social media comments. It classifies user-written text into two categories: **Stress** or **No Stress** using a trained Logistic Regression model built on TF-IDF features. It also includes a simple web interface built with Flask for real-time prediction.

---

## Prerequisites 🛠️  
Before running this project, make sure the following tools and libraries are installed:

- Python (version 3.6 or higher) 🐍  
- Pandas (pandas) 📊  
- Scikit-learn (scikit-learn) 📚  
- Flask (flask) 🌐  
- Joblib (joblib) 💾  

You can install all dependencies using pip:

```bash
pip install pandas scikit-learn flask joblib
```

Project Structure 📂
The project is divided into the following components:

Dataset (dataset.csv):
Contains sample social media comments labeled as 0 (No Stress) or 1 (Stress).

Used for training and evaluation of the machine learning model.

Model Training (train_model.py):
Loads the dataset.

Uses TF-IDF Vectorizer to convert text to numeric features.

Trains a Logistic Regression model.

Saves the model as stress_model.pkl using joblib.

Real-time Detection Web App (app.py):
A simple Flask application.

Loads the saved model and takes user input via a web form.

Predicts and displays whether the input comment indicates stress or not.

Frontend Template (templates/index.html):
A minimal HTML page for user input.

Displays the classification result returned by Flask.
