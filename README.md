# AI Agents Kaggle Bootcamp

A comprehensive 5-day bootcamp focused on building AI agents using modern tools and APIs including OpenAI, Google Gemini, and Kaggle.

## 📚 Project Overview

This repository contains materials, notebooks, and assignments for Kaggle's 5-Day AI Agents Bootcamp. Each day focuses on different aspects of AI agent development, from fundamentals to advanced implementations.

## 🗂️ Project Structure

```
Ai-Agents-Kaggle-Bootcamp/
├── day-1/          # Day 1: Foundational Models & Prompt Engineering
├── day-2/          # Day 2: Embeddings & Vector Databases
├── day-3/          # Day 3: AI Agents
├── day-4/          # Day 4: Domain-Specific Models
├── day-5/          # Day 5: MLOps for Generative AI
├── pyproject.toml  # Poetry project configuration
├── README.md       # This file
└── .gitignore      # Git ignore rules
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- Poetry (for dependency management)
- API Keys:
  - OpenAI API key
  - Google Gemini API key
  - Kaggle API credentials

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/HamzaBendemra/Ai-Agents-Kaggle-Bootcamp.git
   cd Ai-Agents-Kaggle-Bootcamp
   ```

2. **Install dependencies using Poetry**
   ```bash
   poetry install
   ```

3. **Activate the virtual environment**
   ```bash
   poetry shell
   ```

4. **Set up API keys**
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   GOOGLE_API_KEY=your_google_api_key_here
   KAGGLE_USERNAME=your_kaggle_username
   KAGGLE_KEY=your_kaggle_key
   ```

5. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

## 📦 Installed Libraries

- **Jupyter & Notebooks**: `jupyter`, `notebook`, `ipykernel`
- **AI/ML APIs**: `openai`, `google-generativeai`
- **Data Science**: `pandas`, `numpy`, `matplotlib`, `plotly`
- **Utilities**: `python-dotenv`, `requests`, `aiohttp`
- **Kaggle Integration**: `kaggle`
- **Development Tools**: `black`, `pylint`, `ipywidgets`

## 📅 Bootcamp Schedule

### Day 1: Foundational Models & Prompt Engineering
- Understanding large language models and their capabilities
- Setting up development environment
- Prompt engineering techniques and best practices
- Working with OpenAI and Google Gemini APIs

### Day 2: Embeddings & Vector Databases
- Understanding embeddings and their applications
- Working with text embeddings
- Vector similarity and search
- Introduction to vector databases

### Day 3: AI Agents
- Understanding AI agents and their architectures
- Agent design patterns and frameworks
- Tool integration and function calling
- Building autonomous agents

### Day 4: Domain-Specific Models
- Fine-tuning models for specific domains
- Transfer learning techniques
- Model evaluation and optimization
- Domain adaptation strategies

### Day 5: MLOps for Generative AI
- Production deployment strategies
- Monitoring and logging best practices
- Security and safety considerations
- Scalability and performance optimization

## 🛠️ Usage

Each day's folder contains Jupyter notebooks with assignments and exercises. Navigate to the respective day's folder and open the notebook:

```bash
cd day-1
jupyter notebook assignment.ipynb
```

## 📝 Notes

- Make sure to activate the Poetry virtual environment before running any notebooks
- Keep your API keys secure and never commit them to version control
- Each day builds upon the previous day's concepts

## 🤝 Contributing

Feel free to open issues or submit pull requests for improvements and corrections.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Kaggle for providing the bootcamp structure
- OpenAI and Google for their AI APIs
- The AI/ML community for continuous inspiration

---

Happy Learning! 🚀
