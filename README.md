# Streamlit LLM App

This Streamlit application allows users to interact with various Large Language Model (LLM) APIs, such as OpenAI, Gemini, and Ollama. The app fetches the description of a JIRA ticket, generates test cases using the selected LLM model, and provides options to export the test cases to Excel or create new JIRA issues with the generated test cases.

## Table of Contents
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/streamlit-llm-app.git
   cd streamlit-llm-app
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Configuration

1. **Create a `.env` file** in the root directory and add your API keys and JIRA instance URL. The `.env` file should look like this:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   GEMINI_API_KEY=your_gemini_api_key
   OLLAMA_API_KEY=your_ollama_api_key
   JIRA_API_TOKEN=your_jira_api_token
   JIRA_BASE_URL=https://your_jira_instance.atlassian.net
   ```

## Usage

1. **Run the Streamlit application:**
   ```sh
   streamlit run main.py
   ```

2. **Use the UI:**
   - **Left Sidebar:** Select the LLM model (OpenAI, Gemini, or Ollama).
   - **Center:** Enter the JIRA ID and any additional context, then click the "Generate" button to generate test cases.
   - **Below the Generate Button:** View the generated test cases in a table.
   - **Export to Excel:** Click to export the test cases to an Excel file.
   - **Generate test cases in JIRA:** Click to create new JIRA issues with the generated test cases.

## Project Structure

```
streamlit_llm_app/
├── main.py                   # Entry point for the Streamlit application
├── requirements.txt          # List of dependencies
├── README.md                 # Project documentation
├── .env                      # Configuration file for API keys and URLs
├── config/
│   └── config.py             # Configuration settings
├── strategies/               # Folder containing strategy implementations
│   ├── __init__.py
│   ├── base_strategy.py      # Base strategy interface
│   ├── openai_strategy.py    # OpenAI strategy implementation
│   ├── gemini_strategy.py    # Gemini strategy implementation
│   └── ollama_strategy.py    # Ollama strategy implementation
├── ui/                       # Folder containing UI-related files
│   ├── __init__.py
│   ├── home.py               # Main UI page
│   └── utils.py              # Utility functions for the UI
└── services/                 # Folder containing service files
    ├── __init__.py
    ├── jira_service.py       # JIRA API interaction functions
    └── excel_service.py      # Excel export functions
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

This `README.md` file provides a comprehensive overview of your project, including instructions for installation, configuration, usage, project structure, and contributing. Adjust the repository URL and any other specific details as needed.