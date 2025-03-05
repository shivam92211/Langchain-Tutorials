from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


# Create chat template
chat_template = ChatPromptTemplate([
    ('system', 'You are a help full customer service agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])

# Load chat history
chat_history = []
with open("chat_history.txt") as f:
    chat_history.extend(f.readlines())


# Create prompt
prompt = chat_template.invoke({
    'chat_history': chat_history,
    'query': "When will i get my refund back?"
})

print(prompt)
