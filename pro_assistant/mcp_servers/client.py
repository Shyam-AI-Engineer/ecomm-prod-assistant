import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

async def main():
    client = MultiServerMCPClient({
        "hybrid_search": {   # server name
            "command": "python",
            "args": [
                r"D:\complete_content_new\llmops-batch\ecomm-prod-assistant\prod_assistant\mcp_servers\product_search_server.py"
            ],  # absolute path
            "transport": "stdio",
        }
    })