"""
Run the Text-to-SQL pipeline by connecting the individual processing steps.
"""

from build_sql_prompt import build_sql_prompt

query = "What is the installation torque for MT-TL M10 OC?"

prompt = build_sql_prompt(query)

print(prompt)

