import os
from dotenv import load_dotenv
import pdfplumber
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def extract_pdf_text(file_path):
    """
    Extract text from all pages of the PDF file.
    """
    full_text = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for i, page in enumerate(pdf.pages):
                page_text = page.extract_text()
                if page_text:
                    full_text += f"\n--- Page {i+1} ---\n" + page_text
    except Exception as e:
        print("Error reading PDF:", e)
    return full_text


def interactive_qa(pdf_context):
    """
    Create an interactive Q&A session that uses the Groq chat API.
    The PDF content is provided as context via a system message.
    """

    print("\nPDF processing complete. You can now ask questions about the PDF.")
    print("Type 'exit' or 'quit' to end the session.\n")

    # Prepare the system message with PDF context.
    # NOTE: For very large PDFs, you might need to summarize or chunk the content.
    system_message = {
        "role": "system",
        "content": f"The following is the content of a PDF file:\n{pdf_context}\nPlease answer questions based on this document.",
    }

    while True:
        user_question = input("Your question: ")
        if user_question.lower() in ["exit", "quit"]:
            print("Exiting the Q&A session.")
            break

        messages = [system_message, {"role": "user", "content": user_question}]

        try:
            chat_completion = client.chat.completions.create(
                messages=messages,
                model="llama3-8b-8192",  # You can change the model as needed
            )
            answer = chat_completion.choices[0].message.content
            print("\nAnswer:", answer, "\n")
        except Exception as e:
            print("Error during chat completion:", e)


def main():
    pdf_path = input("Enter the path to your PDF file: ").strip()
    print("\nExtracting text from PDF...")
    pdf_text = extract_pdf_text(pdf_path)

    if pdf_text:
        print("Text extraction successful.")
        # Optionally, print a snippet of the extracted text
        print("\n--- Extracted Text Snippet ---")
        print(pdf_text[:500] + "\n...")
        interactive_qa(pdf_text)
    else:
        print("No text could be extracted from the PDF.")


if __name__ == "__main__":
    main()
