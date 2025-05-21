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

## Project Structure 📂
The project is divided into the following components:

𝗗𝗮𝘁𝗮𝘀𝗲𝘁 (𝗱𝗮𝘁𝗮𝘀𝗲𝘁.𝗰𝘀𝘃):
Contains sample social media comments labeled as 0 (No Stress) or 1 (Stress).
   
Used for training and evaluation of the machine learning model.
   
   𝗠𝗼𝗱𝗲𝗹 𝗧𝗿𝗮𝗶𝗻𝗶𝗻𝗴 (𝘁𝗿𝗮𝗶𝗻_𝗺𝗼𝗱𝗲𝗹.𝗽𝘆):
   Loads the dataset.
   
   Uses TF-IDF Vectorizer to convert text to numeric features.
   
   Trains a Logistic Regression model.
   
   Saves the model as stress_model.pkl using joblib.
   
   𝗥𝗲𝗮𝗹-𝘁𝗶𝗺𝗲 𝗗𝗲𝘁𝗲𝗰𝘁𝗶𝗼𝗻 𝗪𝗲𝗯 𝗔𝗽𝗽 (𝗮𝗽𝗽.𝗽𝘆):
   A simple Flask application.
   
   Loads the saved model and takes user input via a web form.
   
   Predicts and displays whether the input comment indicates stress or not.
   
   𝗙𝗿𝗼𝗻𝘁𝗲𝗻𝗱 𝗧𝗲𝗺𝗽𝗹𝗮𝘁𝗲 (𝘁𝗲𝗺𝗽𝗹𝗮𝘁𝗲𝘀/𝗶𝗻𝗱𝗲𝘅.𝗵𝘁𝗺𝗹):
   A minimal HTML page for user input.
   
   Displays the classification result returned by Flask.

## Usage 🚀
1. Train the Model:
   python train_model.py
2. Run the Web Application:
   python app.py
   
## Technologies Used 💻
- **Python**: Programming Language
  
- **Scikit-learn**: Machine Learning Model

- **TF-IDF Vectorizer**: Text Feature Extraction

- **Logistic Regression**: Binary Classification
- **Flask**: Web Framework

## Notes ℹ️
- No use of NLTK or deep NLP libraries — simple and efficient TF-IDF-based approach.

- Make sure to train the model before starting the Flask app.

- The dataset can be extended with more labeled comments for better accuracy.


   








