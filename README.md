# AI Competitive Research Tool

The AI Competitive Research Tool is an agent-based application designed to perform in-depth research on the AI offerings, case studies, and technological innovations of various companies. It leverages advanced language models and web search tools to provide structured, actionable insights into the competitive landscape of artificial intelligence.

## Features
- **Web Search Integration**: Conduct targeted web searches for AI offerings, case studies, and client implementations.
- **AI-Powered Analysis**: Use a single advanced language model (Llama-3.3-70b-versatile) to extract, analyze, and document detailed insights.
- **Structured Reporting**: Generate comprehensive Markdown reports summarizing research findings and comparative analyses.
- **Customizable Research Workflow**: Add tools and customize prompts to refine research output.

---

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Key Components](#key-components)
4. [Output Format](#output-format)
5. [API Integration](#api-integration)
6. [Example Workflow](#example-workflow)

---

## Installation

1. **Clone the Repository**:

2. **Install Dependencies**:
   Ensure you have Python 3.11 or later installed. Install the required packages

3. **Set Up API Keys**:
   Obtain the following API keys:
   - **Serper API Key**: For conducting web searches.
   - **Groq API Key**: For using the advanced LLM.

   Add these keys to the script:
   ```python
   SERPER_API_KEY = 'your-serper-api-key'
   GROQ_API_KEY = 'your-groq-api-key'
   ```

---

## Usage

1. **Initialize the Tool**:
   Create an instance of the `AICompetitiveResearch` class with your API keys.

2. **Conduct Research**:
   Provide a list of companies and a parent company to perform detailed research.

3. **Export Results**:
   Generate and export the research findings to a Markdown file for easy sharing.

---

## Key Components

### 1. **Web Search Tool**
   - Uses the Serper API to perform targeted searches for AI-related offerings and case studies.
   - Extracts unique sources and organizes results into a structured format.

### 2. **LLM-Powered Analysis**
   - A single LLM (Llama-3.3-70b-versatile) performs detailed analysis and comparative studies.
   - The model operates with low temperature for consistent and fact-based outputs.

### 3. **Markdown Report Generator**
   - Summarizes findings into a human-readable Markdown file.
   - Includes:
     - AI offerings and innovations for each company.
     - Sources of information.
     - Comparative analysis.

---

## Output Format

The tool generates a Markdown report with the following structure:
```markdown
# AI Offerings and Case Studies Competitive Research Report

## CompanyA AI Offerings
- Detailed insights into AI capabilities.

### Research Sources:
- **Title**: [Link](URL)
...

## Comparative Analysis
- Overview of strengths, weaknesses, and opportunities across companies.
```

---

## API Integration

### 1. **Serper API**
- **Endpoint**: `https://google.serper.dev/search`
- **Purpose**: Targeted web searches.
- **Payload**:
  ```json
  {
    "q": "query string",
    "num": 7
  }
  ```

### 2. **Groq API**
- **Purpose**: Leverages Llama-3.3-70b-versatile for in-depth research and analysis.

---

## Example Workflow

1. Replace placeholders for API keys in the `main()` function.
2. Run the script:
   ```bash
   python tool.py
   ```
3. View the generated Markdown report (`ai_competitive_research.md`).

---
