import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.callbacks import get_openai_callback


def analyze_text(context, question):
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
            formatted_question = f"The question is after the colon symbol. Be as verbose as possible in your response. Your response should include a 'Interpretation of Question' subheading under which you'll write your interpretation of the user's question, a 'Recommendation' subheading under which you'll write the role you're recommending to the user. Each subheading and its content should be its own paragraph: {question}"
            docs = knowledge_base.similarity_search(formatted_question)
            template = """Question: {question}
            Answer: Let's think step by step."""
            prompt = PromptTemplate(
                template=template, input_variables=["question"])
            llm = OpenAI()
            chain = load_qa_chain(llm, chain_type="stuff", verbose=True)
            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs,
                                     question=formatted_question)
                print(cb)

            # if response is not None:
            #     reason_chain = LLMChain(prompt=prompt, llm=llm)
            #     reason_question = f"Tell me the reason why I should do the action in the quoted text: '{response}'"
            #     with get_openai_callback() as cb:
            #         reason_response = reason_chain.run(reason_question)
            #         print(cb)
            #     with get_openai_callback() as cb:
            #         further_consideration_response = reason_chain.run(question)
            #         print(cb)

            st.subheader('Recommendation Report')
            st.caption("This recommendation report has been created with Adele AI. If you have any questions or feedback, please reach out to the Customer Supoort team at example@adeleai.com")
            st.divider()
            st.write("Question: ", question)
            st.divider()
            st.write(response)

            # if reason_response:
            #     st.write("Reason for Recommending: ", reason_response)
            # if further_consideration_response:
            #     st.write("Further Considerations: ", further_consideration_response)

            st.divider()
            st.write("Download Recommendation Report")
            st.download_button(
                type="primary",
                mime="text/plain",
                file_name="adeleai_recommendation_report",
                label="Download",
                data=response,
            )
