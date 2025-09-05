import os
from typing import Type
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import BaseMessage
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
import logging
from dotenv import load_dotenv

load_dotenv()
class LLM:
    def __init__(self, model: str, api_key: str = os.getenv('GOOGLE_API_KEY')):
        self._model = ChatGoogleGenerativeAI(
            model=model,
            api_key=api_key,
        )

    def singleChat(self, user_input: str) -> str:
        return self._model.invoke(user_input).content

    def hisChat(self, history: list[BaseMessage]) -> str:
        return self._model.invoke(history).content

    def structuredOutputChat(self, user_input: str, schema: Type[BaseModel]):
        runnable_object = self._model.with_structured_output(schema)
        class_output = runnable_object.invoke(user_input)
        return class_output