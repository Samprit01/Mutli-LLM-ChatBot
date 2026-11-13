# LLM Dashboard & Multi-Model Chat

A dual-interface application (Command-Line and Streamlit Web UI) that allows users to interact with multiple Large Language Models (LLMs) using LangChain. The project routes user queries to OpenAI, Google Gemini, or a locally hosted Ollama model and tracks the response time for each interaction.

## Features
* **Multi-Provider Support:** Seamlessly switch between OpenAI (GPT-4o), Google Gemini, and local Ollama models.
* **Dual Interfaces:** 
  * A lightweight Command-Line Interface (CLI) for quick terminal access.
  * A Streamlit web application with a clean, two-column UI layout.
* **Performance Tracking:** Calculates and returns the exact execution time for every LLM response.
* **Environment-Based Security:** Relies on system environment variables for API key management, keeping credentials out of the codebase.

## Prerequisites
Before running the application, ensure you have the following installed:
* Python 3.8+
* [Ollama](https://ollama.com/) (Installed and running locally for local model execution)

## Installation

1. **Clone or Download the Repository:**
   Place the project files (`app.py`, `dashboard.py`, `utility.py`, and `requirements.txt`) into a single directory.

2. **Install Dependencies:**
   Run the following command to install the required Python packages from your `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Environment Variables:**
   The application requires API keys for OpenAI and Google Gemini. Set them in your environment:
   * **Windows (Command Prompt):**
     ```cmd
     set OPENAI_API_KEY=your_openai_api_key
     set GOOGLE_API_KEY=your_google_api_key
     ```
   * **macOS/Linux:**
     ```bash
     export OPENAI_API_KEY="your_openai_api_key"
     export GOOGLE_API_KEY="your_google_api_key"
     ```

4. **Prepare Local Ollama:**
   Ensure Ollama is running on your machine and you have pulled the required model (matching the name in `utility.py`):
   ```bash
   ollama run gemma4
   ```

## Usage

### 1. Web Application (Streamlit)
To launch the graphical user interface, open your terminal in the project directory and run:
```bash
streamlit run app.py
```
This will open a local web server (usually at `http://localhost:8501`). Select your preferred model from the right-hand settings panel, type your query, and view the response and execution time.

### 2. Command-Line Interface (CLI)
To use the terminal-based dashboard, run:
```bash
python dashboard.py
```
Follow the on-screen numeric menu to select your model and input your question.

## Project Structure
* `utility.py`: The core backend module containing the LangChain integration logic (`openai_call`, `ollama_call`, `gemini_call`). It handles model instantiation, invoking the query, and calculating the response duration.
* `dashboard.py`: The CLI script providing a continuous terminal loop for model selection and querying.
* `app.py`: The Streamlit web application script providing a browser-based UI for the project.
* `requirements.txt`: The file containing all project dependencies.