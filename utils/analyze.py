import time
import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
# from langchain.chains import LLMChain
# from langchain.prompts import PromptTemplate
from langchain.callbacks import get_openai_callback


def analyze_text(context, question):
    response = None

    response_status = st.status("Working on it. Hang on...")

    if context is not None:
        # extract text in file
        text = ""
        for page in context.pages:
            text += page.extract_text()
        # split into chunks
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text)
        # create embeddings and knowledge base
        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(chunks, embeddings)

        if question:
            formatted_question = f"The question is after the colon. (Be as precise as possible in your response. Your response should ideally be a sentence long, unless where it makes sense to have more than a sentence): {question}"
            docs = knowledge_base.similarity_search(formatted_question)
            llm = OpenAI(model_name="gpt-3.5-turbo")
            chain = load_qa_chain(llm, chain_type="stuff", verbose=True)
            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs,
                                     question=formatted_question)
                response_status.update(
                    label="Your answer is ready!", state="complete")
                print(cb)

            st.divider()
            st.subheader('Answer')
            st.divider()
            st.text(f"Question: {question}")
            st.write(f"Answer: {response if response else 'Thinking...'}")
            st.divider()
            st.caption(
                'Disclaimer: AI Q&A (BETA) can may be wrong. For enquiries, please reach us at notoristechnologies@gmail.com.')
            st.divider()
            st.write("Download Response")
            st.download_button(
                type="secondary",
                mime="text/plain",
                file_name="aiqa-answer",
                label="Download",
                data=response,
            )
