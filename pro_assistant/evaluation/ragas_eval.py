import asyncio
from utils.model_loader import ModelLoader
from ragas import SingleTurnSample
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from ragas.metrics import LLMContextPrecisionWithoutReference, ResponseRelevancy
import grpc.experimental.aio as grpc_aio