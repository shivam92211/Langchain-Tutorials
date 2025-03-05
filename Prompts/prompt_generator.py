from langchain_core.prompts import PromptTemplate

# Prompt template for summarizing research papers
template = PromptTemplate(
    template="""
    Please provide a {length_input} summary of the research paper "{paper_input}". 
    Use a {style_input} explanation style to ensure the content is tailored appropriately. 
    Highlight the key concepts, methodologies, and findings, while keeping the tone consistent with the selected style.
    """,
    input_variables=['paper_input', 'style_input', 'length_input']
)


template.save("template.json")