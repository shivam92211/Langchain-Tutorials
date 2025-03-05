from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash"
)

st.header("Research Tools")

paper_input = st.selectbox("Select Research Paper",[
    "Select Paper ....",
    "Attention is All You Need",
    "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
    "GPT-3: Language Models are Few-Shot Learners",
    "The Annotated GPT-2",
    "Diffusion Models Beat GANs on Image Synthesis",
    "DALL-E: Creating Images from Text",
])

style_input = st.selectbox("Select Explanation Style",[
    "Beginner-Friendly",
    "Technical",
    "Code-Oriented",
    "Mathematical",
])

length_input = st.selectbox("Select Explanation Length",[
    "Short(1-2 paragraphs)",
    "Medium(3-5 paragraphs)",
    "Long(detailed explanation)",
])

template = load_prompt("template.json")

prompt = template.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'length_input': length_input
})


if st.button("Generate"):
    result = model.invoke(prompt)
    st.write(result.content)
    print(result.content)
