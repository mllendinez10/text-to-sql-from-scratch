"""
Run the Text-to-SQL pipeline by connecting the individual processing steps.
"""

from build_sql_prompt import build_sql_prompt
from generate_sql import generate_sql
from execute_sql import execute_sql
from build_answer_prompt import build_answer_prompt
from generate_answer import generate_answer

def run_pipeline(question):

    sql_prompt = build_sql_prompt(question)

    sql_query = generate_sql(sql_prompt)

    query_result = execute_sql(sql_query)

    answer_prompt = build_answer_prompt(question, sql_query, query_result)

    answer = generate_answer(answer_prompt)

    return answer
