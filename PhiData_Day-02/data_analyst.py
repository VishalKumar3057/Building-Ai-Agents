import json
import streamlit as st

from phi.llm.openai import OpenAIChat
from phi.assistant.duckdb import DuckDbAssistant       #DuckDbTools enable an Assistant to run SQL and analyze data using DuckDb.

data_analyst = DuckDbAssistant(
    llm=OpenAIChat(model="gpt-4o",api_key=""),
    semantic_model=json.dumps(
        {
            "tables": [
                {
                    "name": "movies",
                    "description": "Contains information about movies from IMDB.",
                    "path": "imdb-top-1000.csv",
                }
            ]
        }
    ),
)
data_analyst.print_response("Highest rated movie in 2022? Show me the SQL.", markdown=True)
data_analyst.print_response("Different category of movies", markdown=True)