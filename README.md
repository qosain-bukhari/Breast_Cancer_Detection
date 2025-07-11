 🧠 Breast Cancer Detection with SVM

This project builds a machine learning model to detect breast cancer using the **Support Vector Machine (SVM)** algorithm.
It includes data preprocessing, model training with GridSearchCV, evaluation, and deployment using Docker and Streamlit.

---

## 📂 Project Structure

📦 Breast_Cancer_Detection/
├── app.py # Streamlit web app
├── data/ # Dataset folder (CSV or raw files)
├── models/ # Trained models (.pkl)
├── requirements.txt # Python packages
├── Dockerfile # Docker container instructions
└── README.md # Project documentation


## ✅ Features

- Cleaned & Preprocessed Real-World Dataset
- Feature Engineering
- SVM Model with Hyperparameter Tuning
- Evaluation (Accuracy, ROC-AUC, Confusion Matrix)
- Streamlit Web App Interface
- Dockerized Deployment for Portability


## 🚀 How to Run (Locally)

### 1. Clone this repository


git clone https://github.com/qosain-bukhari/Breast_Cancer_Detection.git
cd Breast_Cancer_Detection
2. Install dependencies
pip install -r requirements.txt
3. Run the app
streamlit run app.py
Then open in browser:

http://localhost:8501
🐳 Docker Deployment Guide
Step 1: Build the Docker image
docker build -t breast-cancer-app .
Step 2: Run the Docker container
docker run -p 8501:8501 breast-cancer-app
Then open:

http://localhost:8501
🧱 Dockerfile (Already included in this repo)
dockerfile
Copy
Edit
# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy all files into container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
📊 Model Performance
Metric	Value
Accuracy	96.4%
ROC AUC Score	0.981
F1 Score	0.95

These may vary based on dataset & preprocessing.

📦 Requirements
Here’s an example of what your requirements.txt might look like:


streamlit
pandas
numpy
scikit-learn
matplotlib
seaborn
joblib
👨‍💻 Author
Name: Qosain Bukhari
GitHub: @qosain-bukhari
Email: bukhariqosain824@gmail.com (update this if needed)

📜 License
This project is licensed under the MIT License.
Feel free to use, share, and improve it.

🙌 Contributions
Pull requests are welcome. For major changes, open an issue first to discuss what you would like to change.

---

If you want, I can generate this as a downloadable file (`README.md`). Would you like that?
