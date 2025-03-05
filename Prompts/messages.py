from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash"
)


# System messages
messages = [
    SystemMessage(content="You are a helpful assistant that provides summaries of research papers."),
    HumanMessage(content="Tell me about langchain"),
]


result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)