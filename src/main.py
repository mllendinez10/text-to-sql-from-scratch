"""
Run the Text-to-SQL pipeline by connecting the individual processing steps.
"""

from build_sql_prompt import build_sql_prompt
from generate_sql import generate_sql
from execute_sql import execute_sql
from build_answer_prompt import build_answer_prompt
from generate_answer import generate_answer

question = "What is the length for MT-30?"

sql_prompt = build_sql_prompt(question)

sql_query = generate_sql(sql_prompt)

query_result = execute_sql(sql_query)

answer_prompt = build_answer_prompt(question, sql_query, query_result)

answer = generate_answer(answer_prompt)

print(f"the user question is: {question}")
print(f" The sql query is: \n {sql_query} \n")
print(f"the query result is: \n {query_result} \n")
print(f"the answer is: {answer}")

