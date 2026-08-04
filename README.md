# 🚗 Car Price Prediction System

> An end-to-end Machine Learning application that predicts the resale price of a used car based on its specifications and provides the prediction through a FastAPI backend and an interactive Streamlit frontend.

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?logo=render&logoColor=white)](https://render.com/)

---

## 🌐 Live Demo

### Frontend

👉 **[Open Car Price Prediction App](https://car-price-frontend-twv4.onrender.com/)**

### Backend API

👉 **[Open FastAPI Backend](https://car-price-backend-89ir.onrender.com/)**

### API Documentation

👉 **[Open Swagger UI](https://car-price-backend-89ir.onrender.com/docs)**

---

## 📌 Project Overview

The **Car Price Prediction System** is a complete end-to-end Machine Learning project designed to estimate the resale price of a used car.

The project takes important car information such as:

- Company
- Car Model
- Manufacturing Year
- Kilometers Driven
- Fuel Type

and uses a trained Machine Learning pipeline to predict the estimated resale price.

The application is divided into two major services:

1. **FastAPI Backend** — responsible for loading the trained ML model and serving prediction APIs.
2. **Streamlit Frontend** — provides a user-friendly interface through which users can enter car details and receive predictions.

The complete application is containerized using **Docker** and **Docker Compose**, version-controlled using **Git/GitHub**, and deployed publicly using **Render**.

---

## 🎯 Project Goal

The main goal of this project is to demonstrate how a Machine Learning model can be transformed from a notebook experiment into a complete production-style application.

The project covers the complete workflow:

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Feature Engineering
     ↓
Machine Learning Pipeline
     ↓
Model Evaluation
     ↓
Model Serialization
     ↓
FastAPI REST API
     ↓
Streamlit Frontend
     ↓
Docker
     ↓
Docker Compose
     ↓
GitHub
     ↓
Render Deployment
     ↓
Live ML Application
```

---

## ✨ Key Features

- 🚗 Used-car resale price prediction
- 🤖 Machine Learning prediction pipeline
- 🧹 Data cleaning and preprocessing
- 📊 Exploratory Data Analysis
- 🔤 Categorical feature encoding
- 🔢 Numerical feature processing
- 🔗 Scikit-learn preprocessing pipeline
- ⚡ FastAPI REST API
- 📚 Automatic Swagger API documentation
- 🎨 Interactive Streamlit frontend
- 🐳 Dockerized backend
- 🐳 Dockerized frontend
- 🔗 Docker Compose service communication
- 🌐 Public Render deployment
- 📦 Serialized ML model using Joblib
- 🔄 Frontend-to-backend API communication
- 🧪 API testing through Swagger
- 🗂️ Git/GitHub version control

---

# 🛠️ Technology Stack

## Programming Language

- **Python 3.11**

## Machine Learning

- **Pandas** — Data manipulation and analysis
- **NumPy** — Numerical operations
- **Scikit-learn** — Machine Learning and preprocessing
- **Joblib** — Model serialization

## Backend

- **FastAPI** — REST API development
- **Uvicorn** — ASGI server
- **Pydantic** — Request validation

## Frontend

- **Streamlit** — Interactive web application

## DevOps / Deployment

- **Docker**
- **Docker Compose**
- **Git**
- **GitHub**
- **Render**

---

# 🏗️ System Architecture

```text
                         ┌───────────────────────┐
                         │        User           │
                         │   Web Browser         │
                         └───────────┬───────────┘
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │   Streamlit Frontend  │
                         │                       │
                         │  User Input Form      │
                         │  Prediction Result    │
                         └───────────┬───────────┘
                                     │
                              HTTP POST /predict
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │    FastAPI Backend    │
                         │                       │
                         │  Request Validation   │
                         │  Prediction Endpoint  │
                         └───────────┬───────────┘
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │  ML Prediction        │
                         │      Pipeline         │
                         │                       │
                         │ Preprocessing         │
                         │ Encoding              │
                         │ Regression Model      │
                         └───────────┬───────────┘
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │   Predicted Price     │
                         │       in INR          │
                         └───────────────────────┘
```

---

# 🐳 Docker Architecture

The application contains two independent Docker services.

```text
                 Docker Compose
                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
 ┌─────────────────┐       ┌─────────────────┐
 │     Backend     │       │    Frontend     │
 │                 │       │                 │
 │    FastAPI      │◄──────│   Streamlit     │
 │     :8000       │ HTTP  │     :8501       │
 └─────────────────┘       └─────────────────┘
```

Inside Docker Compose, the frontend communicates with the backend using the Docker service name:

```text
http://backend:8000
```

This is important because `localhost` inside a container refers to that same container, not another service.

---

# ☁️ Production Deployment Architecture

The project is deployed as two separate Render web services:

```text
                        Internet
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
     ┌──────────────────┐       ┌──────────────────┐
     │ Streamlit        │       │ FastAPI          │
     │ Frontend         │──────►│ Backend          │
     │                  │ HTTP  │                  │
     │ Render           │       │ Render           │
     └──────────────────┘       └────────┬─────────┘
                                         │
                                         ▼
                                ┌──────────────────┐
                                │ Trained ML Model │
                                │     .joblib      │
                                └──────────────────┘
```

### Render Services

**Frontend**

```text
https://car-price-frontend-twv4.onrender.com/
```

**Backend**

```text
https://car-price-backend-89ir.onrender.com/
```

**Swagger Documentation**

```text
https://car-price-backend-89ir.onrender.com/docs
```

---

# 🔄 Prediction Workflow

When a user wants to predict a car's price:

```text
1. User opens Streamlit application
              ↓
2. User enters car details
              ↓
3. Streamlit validates/collects input
              ↓
4. Frontend sends HTTP POST request
              ↓
5. FastAPI receives request
              ↓
6. Pydantic validates request data
              ↓
7. ML pipeline preprocesses input
              ↓
8. Trained regression model predicts price
              ↓
9. FastAPI returns JSON response
              ↓
10. Streamlit displays predicted price
```


---

# 📊 Dataset

The project uses a used-car dataset containing information about previously owned vehicles.

The dataset was cleaned and transformed before training the Machine Learning model.

## Input Features

The final prediction system uses the following features:

| Feature | Description | Type |
|---|---|---|
| `company` | Car manufacturer/company | Categorical |
| `model` | Car model | Categorical |
| `year` | Manufacturing year | Numerical |
| `kms_driven` | Kilometers driven | Numerical |
| `fuel_type` | Fuel type such as Petrol/Diesel/LPG | Categorical |

## Target Variable

```text
Price
```

The target represents the estimated resale price of the vehicle in Indian Rupees (INR).

---

# 🧹 Data Preprocessing

Before training the model, the dataset went through several preprocessing steps.

### 1. Missing Value Handling

Missing values were identified in important columns such as:

- `kms_driven`
- `fuel_type`

Rows containing unusable missing values were removed during cleaning.

### 2. Price Cleaning

The original price values contained formatting such as:

```text
4,50,000
```

These values were converted into numerical values suitable for Machine Learning.

Example:

```text
"4,50,000"
      ↓
450000
```

### 3. Year Cleaning

Invalid or unusable year values were identified and cleaned before model training.

### 4. Categorical Data

Categorical columns such as:

```text
company
model
fuel_type
```

were transformed into numerical representations using the Scikit-learn preprocessing pipeline.

### 5. Numerical Features

Numerical features such as:

```text
year
kms_driven
```

were processed as numerical inputs.

---

# 🤖 Machine Learning Pipeline

The project uses a Scikit-learn pipeline to combine preprocessing and model prediction.

Conceptually:

```text
Raw Input
   │
   ▼
Column Selection
   │
   ├───────────────┐
   │               │
   ▼               ▼
Numerical        Categorical
Features         Features
   │               │
   │               ▼
   │        One-Hot Encoding
   │               │
   └───────┬───────┘
           ▼
     Feature Matrix
           │
           ▼
   Regression Model
           │
           ▼
    Predicted Price
```

The trained pipeline is saved using Joblib:

```text
model/car_price_prediction_pipeline.joblib
```

---

# 📈 Model Training

The dataset was divided into training and testing sets.

The project used:

```text
Training samples: 652
Testing samples: 163
```

The Machine Learning model used for the final pipeline is:

```text
Linear Regression
```

The preprocessing and model are stored together inside the serialized pipeline.

This makes deployment easier because the backend can load the complete prediction pipeline and directly provide raw feature values.

---

# 📊 Model Evaluation

The model was evaluated using standard regression metrics.

The reported evaluation results include:

| Metric | Score |
|---|---:|
| MAE | 133,302.35 |
| RMSE | 307,953.29 |
| R² Score | 0.5343 |

### Mean Absolute Error — MAE

MAE represents the average absolute difference between the actual and predicted prices.

```text
MAE = 133,302.35
```

### Root Mean Squared Error — RMSE

RMSE gives more weight to larger prediction errors.

```text
RMSE = 307,953.29
```

### R² Score

The R² score indicates how much variance in the target variable is explained by the model.

```text
R² = 0.5343
```

These metrics represent the current trained model and should be treated as baseline project results rather than a guarantee of real-world pricing accuracy.


---

# 📁 Project Structure

```text
Car-Price-Prediction-System/
│
├── Backend/
│   ├── __init__.py
│   ├── app.py
│   ├── predictor.py
│   └── ...
│
├── Frontend/
│   ├── app.py
│   ├── services/
│   │   └── api.py
│   └── ...
│
├── Data/
│   └── ...
│
├── Images/
│   └── ...
│
├── Model/
│   └── ...
│
├── Notebook/
│   └── ...
│
├── model/
│   └── car_price_prediction_pipeline.joblib
│
├── EDA.ipynb
│
├── requirements.txt
│
├── Dockerfile.backend
├── Dockerfile.frontend
├── docker-compose.yml
├── .dockerignore
├── .gitignore
└── README.md
```

---

# 🧩 Main Components

## Backend

The backend contains the FastAPI application responsible for:

- Loading the trained ML pipeline
- Validating input data
- Processing prediction requests
- Returning prediction responses
- Providing API documentation

Main application:

```text
Backend/app.py
```

---

## Frontend

The frontend is built using Streamlit.

It provides:

- User input form
- Car feature selection
- Prediction button
- Prediction result
- Error handling
- User-friendly presentation

Main application:

```text
Frontend/app.py
```

---

## API Service

The frontend communicates with FastAPI through the API service layer:

```text
Frontend/services/api.py
```

This keeps API communication separate from the Streamlit UI code.

---

## Trained Model

The trained Machine Learning pipeline is stored at:

```text
model/car_price_prediction_pipeline.joblib
```

---

# 🔌 API Endpoints

## GET `/`

Used to check whether the API is running.

### Request

```http
GET /
```

### Example Response

```json
{
  "message": "API Running 🚗"
}
```

---

## POST `/predict`

Predicts the resale price of a car.

### Request

```http
POST /predict
```

### Request Body

```json
{
  "company": "Hyundai",
  "year": 2019,
  "kms_driven": 45000,
  "fuel_type": "Petrol",
  "model": "i20"
}
```

### Example Response

```json
{
  "success": true,
  "predicted_price": 450000,
  "currency": "INR",
  "message": "Prediction Successful"
}
```

> The predicted value shown above is only an example response format. Actual predictions depend on the trained model and input values.

---

# 📚 API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
https://car-price-backend-89ir.onrender.com/docs
```

### OpenAPI JSON

```text
https://car-price-backend-89ir.onrender.com/openapi.json
```

Swagger can be used to:

- Explore available endpoints
- View request schemas
- Enter test data
- Execute API requests
- Inspect JSON responses
- Test validation errors


---

# 💻 Local Installation

Follow the steps below to run the project locally.

## 1. Clone the Repository

```bash
git clone https://github.com/vikrantjadhav09/Car-Price-Prediction-System.git
```

Move into the project:

```bash
cd Car-Price-Prediction-System
```

---

# 🐍 2. Create Virtual Environment

Create a Python virtual environment:

```bash
python -m venv venv
```

### Windows

Activate the environment:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

# 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ⚡ 4. Run FastAPI Backend

From the project root:

```bash
uvicorn Backend.app:app --reload
```

The backend should be available at:

```text
http://127.0.0.1:8000
```

Open Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# 🎨 5. Run Streamlit Frontend

Open another terminal.

Activate the virtual environment again if necessary:

```bash
venv\Scripts\activate
```

Run:

```bash
streamlit run Frontend/app.py
```

The frontend should be available at:

```text
http://localhost:8501
```

---

# 🐳 Run Using Docker

Docker is the recommended way to run the complete application because the project contains separate backend and frontend services.

---

## 1. Verify Docker

Check Docker installation:

```bash
docker --version
```

Check Docker Engine:

```bash
docker info
```

Test Docker:

```bash
docker run hello-world
```

---

## 2. Build and Start Services

From the project root:

```bash
docker compose up -d --build
```

This starts:

```text
Backend  → http://localhost:8000
Frontend → http://localhost:8501
```

---

## 3. Check Running Containers

```bash
docker compose ps
```

Expected services:

```text
car-price-backend
car-price-frontend
```

---

## 4. Test Backend

Open:

```text
http://localhost:8000/
```

Expected response:

```json
{
  "message": "API Running 🚗"
}
```

Swagger:

```text
http://localhost:8000/docs
```

---

## 5. Test Frontend

Open:

```text
http://localhost:8501
```

---

# 🔗 Docker Service Communication

Inside Docker Compose, the frontend should communicate with the backend using:

```text
http://backend:8000
```

Not:

```text
http://127.0.0.1:8000
```

and not:

```text
http://localhost:8000
```

because `localhost` inside the frontend container refers to the frontend container itself.

Docker Compose creates an internal network where the service name:

```text
backend
```

resolves to the FastAPI container.

---

# 🛑 Stop Docker Services

```bash
docker compose down
```

---

# 🔄 Restart Docker Services

```bash
docker compose restart
```

---

# 📋 View Logs

All services:

```bash
docker compose logs
```

Follow logs:

```bash
docker compose logs -f
```

Backend only:

```bash
docker compose logs backend
```

Frontend only:

```bash
docker compose logs frontend
```


---

# ☁️ Deployment

The application is deployed using **Render**.

The deployment uses two separate web services.

## Backend Deployment

The FastAPI backend is deployed as a Docker-based web service.

Live URL:

```text
https://car-price-backend-89ir.onrender.com/
```

Swagger:

```text
https://car-price-backend-89ir.onrender.com/docs
```

---

## Frontend Deployment

The Streamlit frontend is deployed as a separate Docker-based web service.

Live URL:

```text
https://car-price-frontend-twv4.onrender.com/
```

---

# 🐳 Render Docker Configuration

The backend uses:

```text
Dockerfile.backend
```

The frontend uses:

```text
Dockerfile.frontend
```

Docker containers use Render's dynamically assigned `PORT` environment variable.

The backend starts using:

```bash
uvicorn Backend.app:app --host 0.0.0.0 --port ${PORT}
```

The frontend starts using:

```bash
streamlit run Frontend/app.py --server.address=0.0.0.0 --server.port=${PORT}
```

This allows the application to work correctly with Render's networking environment.

---

# 🔐 Environment Variables

The project can use environment variables for configuration and secrets.

Do not commit sensitive credentials such as:

```text
API keys
passwords
tokens
secret keys
.env files
```

The project `.gitignore` excludes `.env` files.

---

# 🐙 Git & GitHub Workflow

The project uses Git for version control.

Current development branch:

```text
docker-setup
```

Example workflow:

```bash
git status
```

Add changes:

```bash
git add .
```

Commit:

```bash
git commit -m "Your commit message"
```

Push:

```bash
git push origin docker-setup
```

---

# 📦 Important Model File

The trained model file is:

```text
model/car_price_prediction_pipeline.joblib
```

The project originally ignored `.joblib` files using:

```text
*.joblib
```

For deployment, the required trained model was explicitly added to Git using:

```bash
git add -f model/car_price_prediction_pipeline.joblib
```

This is necessary because the deployed backend must have access to the trained model.

---

# 🚀 Deployment Flow

```text
Developer
    │
    ▼
Local Development
    │
    ▼
Git Commit
    │
    ▼
GitHub
    │
    ▼
Render
    │
    ├───────────────┐
    ▼               ▼
Backend          Frontend
    │               │
    ▼               ▼
FastAPI          Streamlit
    │               │
    └───────┬───────┘
            ▼
       Live Application
```


---

# 🧪 Testing

The application can be tested at multiple levels.

## 1. Backend Health Check

Open:

```text
http://localhost:8000/
```

Expected:

```json
{
  "message": "API Running 🚗"
}
```

---

## 2. Swagger Testing

Open:

```text
http://localhost:8000/docs
```

Use the `/predict` endpoint to send test input.

Example:

```json
{
  "company": "Hyundai",
  "year": 2019,
  "kms_driven": 45000,
  "fuel_type": "Petrol",
  "model": "i20"
}
```

---

## 3. Docker Network Testing

To verify that the frontend container can communicate with the backend:

```bash
docker compose exec frontend python -c "import requests; print(requests.get('http://backend:8000/').json())"
```

Expected:

```text
{'message': 'API Running 🚗'}
```

This confirms that Docker service-to-service communication is working.

---

# 🛠️ Common Issues

## Port 8501 Already in Use

If Docker reports:

```text
bind: Only one usage of each socket address
```

another application is already using port `8501`.

Check:

```bash
netstat -ano | findstr :8501
```

Stop the process if necessary or change the host port in `docker-compose.yml`.

---

## Frontend Cannot Reach Backend

If the frontend shows:

```text
Connection refused
```

check the Docker backend service:

```bash
docker compose ps
```

Then test:

```bash
docker compose exec frontend python -c "import requests; print(requests.get('http://backend:8000/').json())"
```

Inside Docker, use:

```text
http://backend:8000
```

instead of:

```text
http://127.0.0.1:8000
```

---

## Model File Not Found

If deployment reports:

```text
FileNotFoundError:
model/car_price_prediction_pipeline.joblib
```

verify that the model exists in Git:

```bash
git ls-tree -r --name-only HEAD | findstr /I "car_price_prediction_pipeline.joblib"
```

Expected:

```text
model/car_price_prediction_pipeline.joblib
```

---

## Check Docker Logs

Backend:

```bash
docker compose logs backend
```

Frontend:

```bash
docker compose logs frontend
```

All services:

```bash
docker compose logs -f
```

---

# ⚠️ Model Compatibility

The serialized Scikit-learn model may produce an `InconsistentVersionWarning` when loaded using a different Scikit-learn version from the version used during training.

For example:

```text
Trying to unpickle estimator ... from version X
when using version Y
```

The current project deployment is functioning with the configured environment.

For production ML systems, keeping the training and inference Scikit-learn versions aligned is recommended.



---

# ⚠️ Current Limitations

This project is a practical end-to-end Machine Learning deployment project, but there are several areas that can be improved.

### Machine Learning

- The current model is based on Linear Regression.
- Prediction accuracy can be improved with stronger regression algorithms.
- More data could improve generalization.
- Additional vehicle features could improve predictions.
- Hyperparameter optimization can be explored.
- Cross-validation can be added to model evaluation.

### Dataset

The model's prediction quality depends heavily on the quality and distribution of the training dataset.

Real-world used-car prices can vary because of factors such as:

- Vehicle condition
- Location
- Number of previous owners
- Insurance status
- Accident history
- Service history
- Variant
- Engine specifications
- Market demand

These factors are not fully represented in the current feature set.

### Deployment

The application currently uses separate Render services for frontend and backend.

The project can be further improved with:

- Better production logging
- Monitoring
- Automated testing
- CI/CD
- API rate limiting
- Better error tracking
- Health checks
- Model versioning

---

# 🚀 Future Improvements

Planned improvements include:

## Machine Learning Improvements

- [ ] Try Random Forest Regression
- [ ] Try Gradient Boosting
- [ ] Try XGBoost
- [ ] Compare multiple regression algorithms
- [ ] Hyperparameter tuning
- [ ] Cross-validation
- [ ] Feature importance analysis
- [ ] Error analysis
- [ ] Model versioning

## Backend Improvements

- [ ] Add `/health` endpoint
- [ ] Add structured logging
- [ ] Add automated API tests
- [ ] Add better exception handling
- [ ] Add request rate limiting
- [ ] Add API versioning
- [ ] Add batch prediction endpoint

## Frontend Improvements

- [ ] Improve prediction visualization
- [ ] Add prediction history
- [ ] Add charts
- [ ] Add downloadable prediction reports
- [ ] Improve mobile responsiveness
- [ ] Add better validation messages

## DevOps Improvements

- [ ] Add CI/CD pipeline
- [ ] Add GitHub Actions
- [ ] Add automated testing before deployment
- [ ] Add Docker image optimization
- [ ] Add production monitoring
- [ ] Add deployment health checks

## AI / MCP Integration

A future version can explore AI-assisted functionality such as:

- Natural-language explanation of predictions
- AI-generated car price summaries
- Prediction analysis
- Interactive AI assistant
- MCP-based tools for interacting with the prediction system

These are future enhancements and are not part of the current deployed implementation.



---

# 🎓 What This Project Demonstrates

This project demonstrates the complete journey from a Machine Learning experiment to a deployed application.

### Machine Learning

```text
Dataset
   ↓
Cleaning
   ↓
EDA
   ↓
Feature Engineering
   ↓
Preprocessing
   ↓
Model Training
   ↓
Evaluation
   ↓
Model Serialization
```

### Software Engineering

```text
ML Model
   ↓
FastAPI
   ↓
REST API
   ↓
Streamlit
   ↓
Docker
   ↓
Docker Compose
   ↓
Git/GitHub
   ↓
Cloud Deployment
```

The project therefore combines:

- Data Science
- Machine Learning
- Python
- Backend Development
- Frontend Development
- REST APIs
- Docker
- Git/GitHub
- Cloud Deployment

---

# 💡 Why This Project Matters

A Machine Learning model inside a Jupyter Notebook is only one part of a real-world ML system.

This project demonstrates how to take the model further:

```text
Notebook
   ↓
Reusable ML Pipeline
   ↓
API
   ↓
Application
   ↓
Container
   ↓
Cloud Deployment
```

This makes the project closer to a real **Machine Learning application / ML engineering workflow** rather than only a model-training exercise.

---

# 📸 Application Screenshots

Add screenshots of the application inside the `Images/` directory and reference them here.

Example:

```markdown
![Home Page](Images/home.png)

![Prediction Page](Images/prediction.png)

![Prediction Result](Images/result.png)

![Swagger API](Images/swagger.png)
```

Recommended screenshots:

1. Home page
2. Prediction form
3. Prediction result
4. Swagger documentation
5. Docker containers
6. Render deployment

---

# 🔗 Project Links

| Resource | Link |
|---|---|
| 🌐 Live Frontend | [Car Price Prediction App](https://car-price-frontend-twv4.onrender.com/) |
| ⚡ Live Backend | [FastAPI Backend](https://car-price-backend-89ir.onrender.com/) |
| 📚 Swagger API | [API Documentation](https://car-price-backend-89ir.onrender.com/docs) |
| 🐙 GitHub Repository | [Car Price Prediction System](https://github.com/vikrantjadhav09/Car-Price-Prediction-System) |

---

# 👨‍💻 Author

## Vikrant Jadhav

Python Full Stack Developer | AI / ML Engineer

Interested in:

- Python
- Machine Learning
- FastAPI
- Data Science
- Generative AI
- Backend Development
- AI Engineering
- Cloud Deployment

---

# ⭐ Support

If you found this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

# 📄 License

This project is intended for educational and portfolio purposes.

Add an appropriate open-source license to the repository if you plan to distribute or reuse the project publicly.

---

# 🙌 Acknowledgements

Thanks to the open-source Python ecosystem and the tools used throughout this project:

- Python
- Pandas
- NumPy
- Scikit-learn
- FastAPI
- Uvicorn
- Streamlit
- Docker
- GitHub
- Render

---

## 🚗 Car Price Prediction System

**From Machine Learning Model → REST API → Docker → Cloud Deployment → Live Application.**

⭐ **Built with Python, Machine Learning, FastAPI, Streamlit and Docker.**

