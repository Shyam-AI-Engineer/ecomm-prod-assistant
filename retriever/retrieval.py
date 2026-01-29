import os
from langchain_astradb import AstraDBVectorStore
from utils.config_loader import load_config
from utils.model_loader import ModelLoader
from dotenv import load_dotenv
from langchain.retrievers.document_compressors import LLMChainFilter
from langchain.retrievers import ContextualCompressionRetriever
from evaluation.ragas_eval import evaluate_context_precision, evaluate_response_relevancy
# Add the project root to the Python path for direct script execution
# project_root = Path(__file__).resolve().parents[2]
# sys.path.insert(0, str(project_root))


class Retriever:
    def __init__(self):
        """_summary_
        """
        self.model_loader=ModelLoader()
        self.config=load_config()
        self._load_env_variables()
        self.vstore = None
        self.retriever_instance = None