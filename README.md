
# Sui Smart Contract Chatbot API

This project is an AI-powered chatbot that helps generate **Sui Move smart contracts** using **GPT API**. Users can provide prompts, and the chatbot will generate, validate, and refine smart contract code.

## 🚀 Features
- **AI-Powered Chatbot**: Uses GPT API to interpret user prompts.
- **Smart Contract Generation**: Generates **Sui Move** smart contracts based on user requests.
- **Validation**: Ensures that generated contracts follow correct syntax and structure.
- **REST API**: Built with **FastAPI** for easy integration with any frontend.

---

## 🏗️ Project Structure
```
sui-smart-contract-chatbot-api/
│
├── src/                      # Source code for the API
│   ├── main.py               # FastAPI entry point
│   ├── api.py                # API routes
│   ├── chatbot.py            # GPT chatbot logic
│   ├── contract_generator.py # Smart contract generation logic
│   └── validation.py         # Contract validation logic
│
├── templates/                # Smart contract templates
│   └── sui_template.move     # Example Move contract template
│
├── tests/                    # Test cases
│   ├── test_api.py           # Tests API endpoints
│   ├── test_chatbot.py       # Tests chatbot functions
│   └── test_validation.py    # Tests contract validation
│
├── docs/                     # Documentation
│   └── README.md             # Project documentation
│
├── requirements.txt          # Python dependencies
├── Dockerfile                # Docker configuration
├── .env                      # Environment variables
└── .gitignore                # Git ignore file
```

---

## ⚙️ Installation and Setup
### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/sui-smart-contract-chatbot-api.git
cd sui-smart-contract-chatbot-api
```

### **2. Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scriptsctivate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Set Up Environment Variables**
Create a `.env` file and add:
```
GPT_API_KEY=your_openai_api_key
```

### **5. Run the API**
```bash
uvicorn src.main:app --reload
```
The API will be available at: **http://127.0.0.1:8000**

---

## 📌 API Endpoints

| Method | Endpoint       | Description |
|--------|--------------|-------------|
| POST   | `/api/chat`  | Send a message to the chatbot |
| POST   | `/api/generate` | Generate a Sui Move smart contract |
| POST   | `/api/validate` | Validate a generated contract |

---

## 🧪 Running Tests
```bash
pytest tests/
```

---

## 🐳 Docker Deployment
To build and run the project in Docker:
```bash
docker build -t sui-chatbot .
docker run -p 8000:8000 sui-chatbot
```

---

## 🛠️ Technologies Used
- **FastAPI** (Python) - API Framework
- **GPT API** - Chatbot & Smart Contract Generation
- **Sui Move** - Smart Contract Language
- **Pytest** - Testing Framework

---

## 📜 License
This project is **open-source** under the **MIT License**.
