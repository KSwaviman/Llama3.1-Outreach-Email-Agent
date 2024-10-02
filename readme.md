
# Outreach Email Agent 📬

This project is designed to assist Business Development Officers by generating personalized outreach emails based on job descriptions scraped from websites. It utilizes LangChain for web scraping and document loading, a vector database for storing and retrieving relevant portfolios, and LLaMA 3.1 on Groq for identifying necessary elements from extrcated data and generating emails. This tool makes the task of reaching potential clients more efficient and streamlined.

## 🚀 Project Overview

This app scrapes job descriptions from a given URL, cleans the extracted text, and uses LLaMA 3.1 to extract relevant information such as job roles and required skills. The app then queries a vector database to find matching projects in the company's portfolio and generates a personalized outreach email that highlights the company's expertise in those areas.

## 🛠️ Technologies Used

Here’s a breakdown of the technologies and tools used in this project:

![LangChain](https://img.shields.io/badge/Web%20Scraping-LangChain-yellow) 
![Groq](https://img.shields.io/badge/Inference-Groq-red) 
![LLaMA](https://img.shields.io/badge/LLM-LLaMA%203.1-orange) 
![ChromaDB](https://img.shields.io/badge/Vector%20Database-ChromaDB-purple)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-brightgreen) 
![Python](https://img.shields.io/badge/Programming-Python-blue)

## 📑 Index

- [Outreach Email Agent 📬](#outreach-email-agent-)
  - [🚀 Project Overview](#-project-overview)
  - [🛠️ Technologies Used](#️-technologies-used)
  - [📑 Index](#-index)
  - [📥 Installation](#-installation)
  - [💡 How It Works](#-how-it-works)
  - [📂 Project Structure](#-project-structure)
  - [🚀 Usage](#-usage)
  - [📜 License](#-license)

---

## 📥 Installation

1. Clone this repository.
   ```
   git clone https://github.com/username/outreach-email-agent.git
   ```
2. Navigate to the project directory.
   ```
   cd outreach-email-agent
   ```
3. Set up a virtual environment and activate it.
   ```
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
4. Install the required packages.
   ```
   pip install -r requirements.txt
   ```

5. Set up your `.env` file with your Groq API key:
   ```
   GROQ_API_KEY=<your-api-key>
   USER_AGENT=OutreachEmailAgent/1.0
   ```

## 💡 How It Works

1. **Scraping**: Using LangChain, the app scrapes job descriptions from the input URL and cleans the extracted text.
2. **Inference**: The cleaned text is processed by LLaMA 3.1 running on Groq to extract job roles, skills, and other relevant information.
3. **Vector Database Query**: A ChromaDB vector database is used to store and retrieve project portfolios based on the extracted job requirements.
4. **Email Generation**: The extracted data and matching portfolios are used to generate a personalized outreach email that the Business Development Officer can send to potential clients.

## 📂 Project Structure

```bash
|-- app/
|   |-- main.py           # Main Streamlit app
|   |-- chains.py         # Logic for using LLaMA for inference
|   |-- ChromaVectorDB.py # Vector database for project portfolios
|   |-- utils.py          # Utility functions for cleaning text
|-- venv/                 # Virtual environment
|-- .env                  # Environment variables
|-- README.md             # Project documentation
|-- requirements.txt      # Python dependencies
```

## 🚀 Usage

1. Run the Streamlit app.
   ```
   streamlit run app/main.py
   ```

2. Enter a job description URL, and the app will generate a tailored outreach email for business development purposes.



https://github.com/user-attachments/assets/4c5d7c7b-0b0e-45d1-9318-805908e2e812



---

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for more details.

