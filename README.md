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

## Project Structure

```text
text-to-sql-from-scratch/
│
├── data/
│   ├── schema.json
│   └── Tables.xlsx
│
├── database/
│   └── products.db
│
├── evaluation/
│   └── golden_set.json
│
├── src/
│   ├── app.py
│   ├── build_answer_prompt.py
│   ├── build_sql_prompt.py
│   ├── create_database.py
│   ├── evaluation.py
│   ├── execute_sql.py
│   ├── generate_answer.py
│   ├── generate_sql.py
│   └── main.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## File Purpose

| File                   | Purpose                                                                                               |
| ---------------------- | ----------------------------------------------------------------------------------------------------- |
| create_database.py     | Creates the SQLite database and loads the Excel data into the tables                                  |
| build_sql_prompt.py    | Builds the SQL generation prompt using the schema and user question                                   |
| generate_sql.py        | Sends the prompt to Qwen3 via Ollama and generates the SQL query                                      |
| execute_sql.py         | Executes the generated SQL query against the SQLite database                                          |
| build_answer_prompt.py | Builds the answer prompt using the question, SQL query, query result, and relevant schema information |
| generate_answer.py     | Sends the answer prompt to Qwen3 via Ollama and generates the final natural language answer           |
| evaluation.py          | Evaluates Text-to-SQL accuracy using the golden set                                                   |
| main.py                | Connects and runs the individual steps of the Text-to-SQL pipeline                                    |
| app.py                 | Provides the Streamlit user interface                                                                 |

## Evaluation Results

The Text-to-SQL pipeline is evaluated using the questions in the file golden_set.json

Each golden set entry contains:

* A natural language question
* A difficulty level: easy, medium, or hard
* The expected answer content

The evaluation script runs every question through the complete pipeline and checks whether all expected answer content is present in the generated answer. A question is counted as correct only if all expected answer content is present in the answer.

The evaluation results are:

* Easy: 5/6 correct
* Medium: 5/6 correct
* Hard: 0/2 correct

## Project Takeaways

The main insights gained from building and evaluating the Text-to-SQL pipeline from scratch are:

* Text-to-SQL performance depends heavily on how clearly the database schema and relationships are described to the LLM.
* Prompt instructions can guide SQL generation, but they do not guarantee correct queries.
* Answer accuracy is more meaningful than comparing generated SQL strings because different SQL queries can return the same correct result.
* Providing only relevant schema information to the answer generation step reduces unnecessary context and improves efficiency.
* Local LLM inference is the main performance bottleneck, while SQLite query execution is typically very fast.
* A golden set is essential for identifying the strengths and weaknesses of the system.
* The pipeline performs well on easy and medium questions but struggles with hard questions involving multiple filters and joins.
