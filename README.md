# Disease-Outbreak-Prediction Using ML
📌 Project Overview
This project aims to predict disease outbreaks using machine learning techniques based on various health and environmental factors. The model analyzes historical outbreak data to provide early warnings, helping healthcare professionals take preventive measures.

🚀 Features
✔ Predicts the likelihood of disease outbreaks based on input data
✔ Uses machine learning algorithms such as Logistic Regression/SVM/Random Forest
✔ Provides insights through a Streamlit web application
✔ Saves trained models for future use
✔ User-friendly interface for easy predictions

📊 Model Training
The machine learning model is trained using Logistic Regression / Support Vector Machine (SVM).
Steps followed:

Load and preprocess the dataset (heart.csv / diabetes.csv)
Split the dataset into training and testing sets
Train the model using LogisticRegression() or SVC(kernel='linear')
Evaluate model performance using accuracy, precision, recall, and confusion matrix
Save the trained model using pickle

📈 Evaluation Metrics
To assess model performance, the following metrics are used:

Accuracy: Measures overall correctness
Precision: Measures true positive predictions
Recall: Measures the model's ability to detect all actual positives
Confusion Matrix: Provides a breakdown of predictions

