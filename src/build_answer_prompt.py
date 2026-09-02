"""
Build the prompt used to generate the natural language answer from the query result.

The script will:

- Receive the user question
- Receive the SQL query
- Receive the query result 
- Receive schema
- Return the prompt for answer generation

"""

from pathlib import Path
import json

# ---------------------------------------------------------------------------
# File path
# ---------------------------------------------------------------------------

SCHEMA_FILE = Path("data/schema.json")


# ---------------------------------------------------------------------------
# Load database schema
# ---------------------------------------------------------------------------

def load_schema():

    with open(SCHEMA_FILE, "r", encoding="utf-8") as file:
        schema = json.load(file)

    return schema

# ---------------------------------------------------------------------------
# Build SQL generation prompt
# ---------------------------------------------------------------------------

def build_answer_prompt(question, sql_query, query_result):


    schema = load_schema()

    answer_prompt = f"""
/no_think

Use only the query result provided below to answer the question.

Rules:
- Give only the final answer.
- Answer directly and concisely.
- Do not explain your reasoning.
- Do not describe how you searched the data.
- Do not include information that is not available in the query result.
- When the query result is a numerical value, provide always the unit.
- Use the unit defined in the schema for the column returned by the SQL query.

If the query result is empty, respond exactly with:
"The information is not available in the database."

Question:
{question}

SQL query:
{sql_query}

Query result:
{query_result}

Schema:
{schema}

"""

    return answer_prompt