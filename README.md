# Autonomous CSV Data Analyst

This project uses LangChain's Pandas DataFrame Agent to perform natural language analysis on CSV data, integrated into a Django web application.

## Features
- LangChain Pandas Agent setup.
- Web-based dashboard for data analysis.
- Automatic manual verification against standard Pandas operations.
- Sample CSV processing and visualization.

## Setup
1. **Install Ollama**:
   - Download and install from [ollama.com](https://ollama.com/).
   - Open your terminal and pull the LLM model:
     ```bash
     ollama pull llama3
     ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment**:
   - Create or update your `.env` file:
     ```bash
     AI_PROVIDER=OLLAMA
     OLLAMA_MODEL=llama3
     ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

## Files
- `sample.csv`: The target data file.
- `agent_logic.py`: initialization of the LangChain agent.
- `manage.py`: Django management script.
- `analyst/`: Django app containing views and templates.
