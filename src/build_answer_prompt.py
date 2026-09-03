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
# Get relevant schema information
# ---------------------------------------------------------------------------

def get_relevant_schema_info(schema, sql_query):

    relevant_schema_info = []

    for table_name, table_info in schema["tables"].items():

        for column_name, column_info in table_info["columns"].items():

            if column_name.lower() in sql_query.lower():

                relevant_schema_info.append(
                    {
                        "table": table_name,
                        "column": column_name,
                        "description": column_info.get("description"),
                        "unit": column_info.get("unit")
                    }
                )

    return relevant_schema_info


# ---------------------------------------------------------------------------
# Build SQL generation prompt
# ---------------------------------------------------------------------------

def build_answer_prompt(question, sql_query, query_result):


    schema = load_schema()
    relevant_schema_info = get_relevant_schema_info(schema, sql_query)

    answer_prompt = f"""
/no_think

Use only the query result provided below to answer the question.

Rules:
- Give only the final answer.
- Answer directly and concisely.
- Do not explain your reasoning.
- Do not describe how you searched the data.
- Do not include information that is not available in the query result.
- When the query result contains a numerical value, include the unit if one is defined in the relevant schema information.
- Use the unit defined in the relevant schema information below.

If the query result is empty, respond exactly with:
"The information is not available in the database."

Question:
{question}

SQL query:
{sql_query}

Query result:
{query_result}

Relevant schema information:
{relevant_schema_info}
"""

    return answer_prompt