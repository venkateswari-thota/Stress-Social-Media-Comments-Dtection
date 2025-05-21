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



Project Structure 📂
The project is divided into the following components:

Dataset (dataset.csv):
Contains sample social media comments labeled as 0 (No Stress) or 1 (Stress).
Used for training and evaluation of the machine learning model.

Model Training (model.py):
Cleans and processes the text data using TF-IDF Vectorization.
Trains a Logistic Regression model to classify the comments into stressed or not stressed.
Saves the trained model using joblib.

Flask Web App (app.py):
Loads the trained model.
Takes user input through a web form.
Predicts whether the comment indicates stress and displays the result in real-time.

Templates (templates/index.html):
Provides the user interface for input and result display.
