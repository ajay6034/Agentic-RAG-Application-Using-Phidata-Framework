from phi.agent import Agent
from phi.model.groq import Groq
from phi.embedder.openai import OpenAIEmbedder
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.lancedb import LanceDb, SearchType
import os
import openai

from dotenv import load_dotenv
load_dotenv()


openai.api_key=os.getenv("OPENAI_API_KEY")
Groq.api_key=os.getenv("GROQ_API_KEY")

# Create a Knowledge Base from A PDF

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],

    vector_db=LanceDb(
        table_name="Recipes",
        uri="tmp/lancedb",
        search_type=SearchType.vector,
        embedder=OpenAIEmbedder(model="text-embedding-3-small")
    )
)

# Comment out after first run as the knowledge base is loaded
knowledge_base.load()

## Creating agent to communicate with vector db

agent= Agent(
    model=Groq(id='llama-3.2-1b-preview'),
    # Add the knowledge base to the agent
    knowledge=knowledge_base,
    show_tool_calls=True,
    markdown=True,

)

agent.print_response("How do I make chicken?", stream=True)