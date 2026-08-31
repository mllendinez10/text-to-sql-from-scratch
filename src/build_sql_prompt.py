"""
Build the prompt used to generate SQL from a natural language question.

The script will:
- Load the database schema from schema.json
- Format tables, columns, and relationships for the LLM
- Add the question from the user
- Add rules for generating valid SQLite.
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
# Format schema from JSON to plain text for the LLM
# ---------------------------------------------------------------------------

def format_schema(schema):

    schema_text = ""

    for table_name, table_info in schema["tables"].items():

        schema_text += f"\nTable: {table_name}\n"

        for column_name, column_info in table_info["columns"].items():

            sql_type = column_info["sql_type"]
            description = column_info["description"]

            schema_text += (
                f"- {column_name}: {sql_type}"
                f" | {description}\n"
            )

    schema_text += "\nRelationships:\n"

    for relationship in schema["relationships"]:

        schema_text += (
            f"- {relationship['child_table']}."
            f"{relationship['child_column']} "
            f"references "
            f"{relationship['parent_table']}."
            f"{relationship['parent_column']}\n"
        )

    return schema_text


# ---------------------------------------------------------------------------
# Build SQL generation prompt
# ---------------------------------------------------------------------------

def build_sql_prompt(query):

    schema = load_schema()
    schema_text = format_schema(schema)

    prompt = f"""
You are a SQL assistant.

Use the database schema below to generate a valid SQLite query.

Rules:
- Use only tables and columns defined in the schema.
- Generate only SELECT queries.
- Do not use DELETE, UPDATE, INSERT, DROP, or ALTER.
- Return only the SQL query.
- Do not explain the query.

Database schema:
{schema_text}

User question:
{query}

"""

    return prompt