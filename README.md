# Edtech LLM - A Q&A Based Chatbot to Help an Ed-tech Website Using Gemini API and Langchain

This is an end-to-end LLM project based on Google Palm and Langchain. I have built a Q&A system for an e-learning company. This system will provide a Streamlit-based user interface for students where they can ask questions and receive answers.

## Tools and Technologies Used

- Langchain + Google Palm: LLM-based Q&A
- Streamlit: User Interface
- Google Generative AI Embeddings: Text embeddings
- FAISS: Vector Database

## Installation

1. Clone this repository to your local machine using:

   ```bash
   git clone https://github.com/Marriam-Naeem/Ed-Tech-LLM-using-GeminiAPI.git
   ```

2. Navigate to the project directory:
   ```bash
      cd Ed-Tech-LLM-using-GeminiAPI
   ```

3. Install the required dependencies using pip:

   ```bash
      pip install -r requirements.txt

4. Acquire an API key through makersuite.google.com and put it in the .env file:

   ```bash
      GOOGLE_API_KEY="your_api_key_here"
   
## Usage

1. Run the Streamlit app by executing:

   ```bash
   streamlit run main.py
2. The web app will open in your browser.

#

To create a knowledge base of FAQs, click on the Create Knowledge Base button. It will take some time before the knowledge base is created, so please wait. 
Once the knowledge base is created, you will see a directory called ```faiss_index``` in your current folder. Now you are ready to ask questions. Type your question in the question box and hit Enter.
## Sample Questions

- **I have never done programming in my life. Can I take this bootcamp?**
- **What datasets are used in this bootcamp? Is it some toy datasets or something that mimics a real-world business problem?**
- **Do we have an EMI option?**
- **Do you have a JavaScript course?**

# Project Structure

- ```main.py```: The main Streamlit application script.
- ```LLMhelper.py```: This file contains all the Langchain code.
- ```requirements.txt```: A list of required Python packages for the project.
- ```.env```: Configuration file for storing your Google API key.


   
