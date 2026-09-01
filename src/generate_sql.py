"""
This file generates a SQL query from a natural language question.

The script will:
- Receive the prompt
- Send the prompt to the LLM
- Return the generated SQL query
"""

import ollama

LLM_MODEL = "qwen3:4b"


def generate_sql(prompt: str) -> str:

    response = ollama.chat(
        model=LLM_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            # temperature=0 is more deterministic (no creativity)
            "temperature": 0
        }
    )

    sql_query = response.message.content.strip()

    return sql_query
