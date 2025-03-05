from langchain_core.prompts import ChatPromptTemplate


chat_template = ChatPromptTemplate([
    ('system', 'You have an experties in {domain}'),
    ('human', 'Explain me about {topic}')
])

prompt = chat_template.invoke({
    'domain': 'Machine Learning',
    'topic': 'Gradient Descent'
})

print(prompt)


from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI( model="gemini-1.5-flash")

result = model.invoke(prompt)

print(result.content)