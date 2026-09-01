"""
Run the Text-to-SQL pipeline by connecting the individual processing steps.
"""

from build_sql_prompt import build_sql_prompt
from generate_sql import generate_sql
from execute_sql import execute_sql

question = "What is the maximum yield strength?"

prompt = build_sql_prompt(question)

sql_query = generate_sql(prompt)

query_result = execute_sql(sql_query)

print(f" The sql query is: \n {sql_query} \n")
print(f"the query result is: \n {query_result} \n")

