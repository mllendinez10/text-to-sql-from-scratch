"""
Generate natural language answer.

The script will:

- Receive the user question
- Receive the SQL query
- Receive the answer prompt
- Return the natural language answer

"""

import ollama

# Local LLM model
LLM_MODEL = "qwen3:4b"

def generate_answer(answer_prompt):

    
    response = ollama.chat(
        model=LLM_MODEL,
        messages=[
            {
                "role": "user",
                "content": answer_prompt
            }
        ],
        # Disable Qwen3 thinking mode for faster answers
        think=False,
        # Keep the model loaded in memory for faster follow up questions. It consumes RAM
        keep_alive="10m",
        options={"temperature": 0}
    )
    
    answer = response["message"]["content"].strip()

    # Remove Qwen thinking output if it appears
    if "</think>" in answer:
        answer = answer.split("</think>")[-1].strip()

    return answer