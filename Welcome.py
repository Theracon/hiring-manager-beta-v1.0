# from typing import List
from dotenv import load_dotenv
import streamlit as st
# from PyPDF2 import PdfReader
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.vectorstores import FAISS
# from langchain.chains.question_answering import load_qa_chain
# from langchain.llms import OpenAI
# from langchain.chains import LLMChain
# from langchain.prompts import PromptTemplate
# from langchain.callbacks import get_openai_callback
# from langchain.document_loaders import GoogleDriveLoader
# from google.cloud.speech_v2 import SpeechClient
# from google.cloud.speech_v2.types import cloud_speech


# def transcribe_file_v2(
#     project_id: str,
#     audio_file: str,
#     language_codes: List[str]
# ) -> cloud_speech.RecognizeResponse:
#     """Transcribe an audio file."""
#     # Instantiates a client
#     client = SpeechClient()

#     # Reads a file as bytes
#     with open(audio_file, "rb") as f:
#         content = f.read()

#     config = cloud_speech.RecognitionConfig(
#         auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
#         language_codes=language_codes,
#         model="latest_long",
#         # features=cloud_speech.RecognitionFeatures(
#         #     enable_automatic_punctuation=True
#         # )
#     )

#     request = cloud_speech.RecognizeRequest(
#         recognizer=f"projects/{project_id}/locations/global/recognizers/_",
#         config=config,
#         content=content,
#     )

#     # Transcribes the audio into text
#     response = client.recognize(request=request)
#     text = ""

#     for result in response.results:
#         text += f"{result.alternatives[0].transcript}"

#     return text


# def analyze(context, question):
#     if context is not None:
#         print("Context:", context.metadata)

#         # extract text in file
#         text = ""
#         for page in context.pages:
#             text += page.extract_text()

#         # split into chunks
#         text_splitter = CharacterTextSplitter(
#             separator="\n",
#             chunk_size=1000,
#             chunk_overlap=200,
#             length_function=len
#         )
#         chunks = text_splitter.split_text(text)

#         # create embeddings and knowledge base
#         embeddings = OpenAIEmbeddings()
#         knowledge_base = FAISS.from_texts(chunks, embeddings)

#         if question:
#             formatted_question = f"The question is after the colon symbol. Be as verbose as possible in your response. Your response should include a 'Interpretation of Question' subheading under which you'll write your interpretation of the user's question, a 'Recommendation' subheading under which you'll write the role you're recommending to the user. Each subheading and its content should be its own paragraph: {question}"
#             docs = knowledge_base.similarity_search(formatted_question)

#             template = """Question: {question}
#             Answer: Let's think step by step."""
#             prompt = PromptTemplate(
#                 template=template, input_variables=["question"])
#             llm = OpenAI()
#             chain = load_qa_chain(llm, chain_type="stuff", verbose=True)
#             with get_openai_callback() as cb:
#                 response = chain.run(input_documents=docs,
#                                      question=formatted_question)
#                 print(cb)

#             # if response is not None:
#             #     reason_chain = LLMChain(prompt=prompt, llm=llm)
#             #     reason_question = f"Tell me the reason why I should do the action in the quoted text: '{response}'"
#             #     with get_openai_callback() as cb:
#             #         reason_response = reason_chain.run(reason_question)
#             #         print(cb)
#             #     with get_openai_callback() as cb:
#             #         further_consideration_response = reason_chain.run(question)
#             #         print(cb)

#             st.subheader('Recommendation Report')
#             st.caption("This recommendation report has been created with Adele AI. If you have any questions or feedback, please reach out to the Customer Supoort team at example@adeleai.com")
#             st.divider()
#             st.write("Question: ", question)
#             st.divider()
#             st.write(response)

#             # if reason_response:
#             #     st.write("Reason for Recommending: ", reason_response)
#             # if further_consideration_response:
#             #     st.write("Further Considerations: ", further_consideration_response)

#             st.divider()
#             st.write("Download Recommendation Report")
#             st.download_button(
#                 type="primary",
#                 mime="text/plain",
#                 file_name="adeleai_recommendation_report",
#                 label="Download",
#                 data=response,
#             )


def main():
    load_dotenv()
    # project_name = 'adele-405718'
    # language_codes = ["en-US", "es-ES"]
    # user_question = ""
    st.set_page_config(page_title="Adele AI (beta)",
                       layout="centered", page_icon="🏠")
    st.header("Welcome to ADELE AI (beta)")
    st.divider()
    # # select input mode:
    # mode = st.radio(
    #     "**What's your preferred input method?**",
    #     ["Text :pencil:", "Audio :microphone:"],
    #     captions=["Enter plain text in English.", "Upload an audio file."]
    # )

    # if mode == "Text :pencil:":
    #     user_question = st.text_area("Enter your question here:")
    # elif mode == "Audio :microphone:":
    #     user_question = st.file_uploader("Upload audio file", type="wav")

    # if user_question:
    #     file_name = f"./{user_question.name}"
    #     text_from_speech = transcribe_file_v2(
    #         project_name, file_name, language_codes)
    #     st.divider()
    #     st.write("Transcribed Audio:", text_from_speech)
    #     st.button('Edit')
    #     st.divider()

    #     if mode == 'Enter Text':
    #         question = user_question
    #     else:
    #         question = text_from_speech

    # # upload context file
    # context = PdfReader("AdeleAI-v1.0.pdf")

    # if st.button('Go!', type='primary'):
    #     analyze(context, question)

    # st.divider()
    # st.caption("Adele AI (c) 2023. All rights reserved.")


if __name__ == '__main__':
    main()
