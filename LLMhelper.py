import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import CSVLoader  # Updated import
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS  # Updated import

load_dotenv()  

# Create Google Palm LLM model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0.1,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

instructor_embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vectordb_file_path = "faiss_index"

def create_vector_db():
    loader = CSVLoader(file_path='data.csv', source_column="prompt", encoding='ISO-8859-1')
    data = loader.load()
    vectordb = FAISS.from_documents(documents=data, embedding=instructor_embeddings)
    vectordb.save_local(vectordb_file_path)

def get_relevant_docs(user_query):
    # Set allow_dangerous_deserialization=True to load the FAISS index
    vectordb = FAISS.load_local(vectordb_file_path, instructor_embeddings, allow_dangerous_deserialization=True)
    retriever = vectordb.as_retriever(score_threshold=0.7)
    relevant_docs = retriever.get_relevant_documents(user_query)
    return relevant_docs

def make_rag_prompt(query, relevant_passage):
    relevant_passage = ''.join(relevant_passage)
    prompt = (
        f"You are a helpful and informative chatbot that answers questions using text from the reference passage included below. "
        f"Give a detailed response answering the user query but make sure you provide as much information from the context response part as possible and relevant. "
        f"Maintain a friendly and conversational tone. "
        f"If you don't know the answer or you cannot find the relevant information in the provided context passage, just say 'I don't know'. No extra detail. "
        f"Don't make things up. Don't give any extra information that is not there in the provided context passage.\n\n"
        f"QUESTION: '{query}'\n"
        f"PASSAGE: '{relevant_passage}'\n\n"
        f"ANSWER:"
    )
    return prompt

def generate_response(user_prompt):
    answer = llm.invoke(user_prompt)
    return answer.content

def generate_answer(query):
    relevant_text = get_relevant_docs(query)
    
    # Extract text using the correct attribute 'page_content'
    text = " \n".join([doc.page_content for doc in relevant_text])
    prompt = make_rag_prompt(query, relevant_passage=text)
    answer = generate_response(prompt)
    return answer

if __name__ == "__main__":
    answer = generate_answer(query="I dont know if i should spend money on this bootcamp or not?")
    print("\nAnswer:")
    print(answer)
