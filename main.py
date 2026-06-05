from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
# from vector import retriever

# Load model
model = OllamaLLM(model="llama3")

# Prompt template
template = """
You are expert in hotel parking management.

Here are some relevant reviews:
{reviews}

Here is the question to answer:
{question}
"""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

while True:
    print("\n\n---------------------------")
    question = input("Ask your question(q to quit): ")
    print("\n\n")
    if question =="q":
        break

    # reviews = retriever.invoke(question)
    result = chain.invoke({"reviews": [], "question": question})
    print(result)