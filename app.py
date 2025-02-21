import os
from dotenv import load_dotenv
import streamlit as st
import pdfplumber
from groq import Groq

# Load environment variables and initialize Groq client
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def extract_pdf_text(pdf_file):
    """Extract text from uploaded PDF file"""
    full_text = ""
    try:
        with pdfplumber.open(pdf_file) as pdf:
            for i, page in enumerate(pdf.pages):
                page_text = page.extract_text()
                if page_text:
                    full_text += f"\n--- Page {i+1} ---\n" + page_text
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
    return full_text


def get_groq_response(messages):
    """Get response from Groq API"""
    try:
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama3-8b-8192",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        st.error(f"Error during chat completion: {e}")
        return None


def main():
    st.title("PDF Question Answering System")

    # Initialize session state for conversation history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # File upload
    uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

    if uploaded_file:
        # Extract text when file is uploaded
        if (
            "pdf_text" not in st.session_state
            or st.session_state.current_file != uploaded_file.name
        ):
            with st.spinner("Extracting text from PDF..."):
                st.session_state.pdf_text = extract_pdf_text(uploaded_file)
                st.session_state.current_file = uploaded_file.name
                st.session_state.messages = []  # Reset conversation for new file

            st.success("PDF processed successfully!")
            with st.expander("View extracted text"):
                st.text(st.session_state.pdf_text[:1000] + "...")

        # Chat interface
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])

        if prompt := st.chat_input("Ask a question about the PDF"):
            # Display user message
            with st.chat_message("user"):
                st.write(prompt)

            # Prepare messages including system context and conversation history
            messages = (
                [
                    {
                        "role": "system",
                        "content": f"The following is the content of a PDF file:\n{st.session_state.pdf_text}\nPlease answer questions based on this document.",
                    }
                ]
                + st.session_state.messages
                + [{"role": "user", "content": prompt}]
            )

            # Get and display assistant response
            with st.chat_message("assistant"):
                response = get_groq_response(messages)
                if response:
                    st.write(response)

            # Update conversation history
            st.session_state.messages.extend(
                [
                    {"role": "user", "content": prompt},
                    {"role": "assistant", "content": response},
                ]
            )


if __name__ == "__main__":
    main()
