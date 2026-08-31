## text-to-sql-from-scratch

This project focuses on learning how Text-to-SQL works by building the complete pipeline from scratch in Python.

It intentionally avoids higher-level frameworks at the beginning, so each step can be implemented and understood independently.

As a practical use case, the project uses structured Hilti product data stored in a SQLite database and allows users to ask questions in natural language, which are translated into SQL queries and used to retrieve the relevant information from the database.

## Project Goal

The goal is to gain hands-on experience with the main components of a Text-to-SQL system:

- Structured data and schema preparation
- SQLite database creation
- Prompt construction using the database schema and user question
- SQL query generation with an LLM
- SQL validation and safety checks
- Query execution against SQLite
- SQL result processing
- LLM answer generation
- Text-to-SQL evaluation using a golden set
- UI development with Streamlit

## Technology Stack

| Area                   | Technology           |
| ---------------------- | -------------------- |
| Programming language   | Python               |
| Structured data source | Excel                |
| Database schema        | JSON                 |
| Excel processing       | Pandas with openpyxl |
| Relational database    | SQLite               |
| LLM                    | Qwen3 4B via Ollama  |
| UI                     | Streamlit            |
