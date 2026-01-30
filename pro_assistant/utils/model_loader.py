import os
import sys
import json
from dotenv import load_dotenv

from utils.config_loader import load_config
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

from logger import GLOBAL_LOGGER as log
from exception.custom_exception import ProductAssistantException
import asyncio

class ApiKeyManager:
    def __init__(self):
        self.api_keys = {
            "GOOGLE_API_KEY": os.getenv("GOOGLE_API_KEY"),
            "GROQ_API_KEY": os.getenv("GROQ_API_KEY"),
            "HUGGINGFACEHUB_API_TOKEN": os.getenv("HUGGINGFACEHUB_API_TOKEN"),
            "ASTRA_DB_API_ENDPOINT": os.getenv("ASTRA_DB_API_ENDPOINT"),
            "ASTRA_DB_APPLICATION_TOKEN": os.getenv("ASTRA_DB_APPLICATION_TOKEN"),
            "ASTRA_DB_KEYSPACE": os.getenv("ASTRA_DB_KEYSPACE"),
        }

        # Just log loaded keys (don't print actual values)
        for key, val in self.api_keys.items():
            if val:
                log.info(f"{key} loaded from environment")
            else:
                log.warning(f"{key} is missing from environment")

    def get(self, key: str):
        return self.api_keys.get(key)