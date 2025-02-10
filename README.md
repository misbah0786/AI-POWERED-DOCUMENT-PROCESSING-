# AI-Powered Document Processing for Invoice Processing

An advanced Python application that leverages cutting-edge PDF text extraction and Groq's LLM capabilities to intelligently process and analyze invoices. This tool not only extracts text from multi-page invoice PDFs but also enables interactive Q&A sessions to query and retrieve specific invoice details.

## Table of Contents

- [AI-Powered Document Processing for Invoice Processing](#ai-powered-document-processing-for-invoice-processing)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Setup and Installation](#setup-and-installation)
  - [Usage](#usage)
  - [Project Structure](#project-structure)
  - [Troubleshooting \& Tips](#troubleshooting--tips)
  - [Acknowledgments](#acknowledgments)

## Introduction

This project is designed to streamline invoice processing by combining two powerful tools:

1. **PDF Text Extraction:** Using [pdfplumber](https://pypi.org/project/pdfplumber/), the application extracts text from every page of your invoice PDFs.
2. **Interactive Q&A with Groq:** With the [Groq Python library](https://pypi.org/project/groq/), the tool integrates a chat completion interface powered by large language models (LLMs) to answer questions based on the extracted invoice data.

This solution is ideal for businesses looking to automate the analysis of invoices, reduce manual entry, and quickly retrieve key invoice details.

## Features

-   **PDF Text Extraction:** Automatically extracts and concatenates text from multi-page PDF invoices.
-   **Interactive Q&A Session:** Users can interact with an AI-powered chatbot that answers questions based on the invoice content.
-   **Invoice Analysis:** Utilize natural language processing to query invoice details such as totals, dates, and vendor information.
-   **Customizable Workflow:** Easily adapt the code to handle different types of documents and extend its functionalities.
-   **Open-Source:** Modify and extend the application to suit your needs.

## Prerequisites

-   **Python Version:** Python 3.8 or later.
-   **API Key:** A valid Groq API key (set via a `.env` file).
-   **Required Python Packages:**
    -   [python-dotenv](https://pypi.org/project/python-dotenv/)
    -   [pdfplumber](https://pypi.org/project/pdfplumber/)
    -   [groq](https://pypi.org/project/groq/)

## Setup and Installation

1. **Clone the Repository**

    ```sh
    git clone https://github.com/misbah0786/AI-POWERED-DOCUMENT-PROCESSING-
    ```

2. **Navigate to the Project Folder**

    ```sh
    cd AI-POWERED-DOCUMENT-PROCESSING-
    ```

3. **Install Dependencies**

    It is recommended to use a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

4. **Create a .env File**

    In the project root, create a `.env` file and add your Groq API key:

    ```dotenv
    GROQ_API_KEY="your_groq_api_key_here"
    ```

## Usage

1. **Run the Application**

    Start the application with:

    ```sh
    python app.py
    ```

2. **Follow the On-Screen Instructions**

    - **PDF Input:** When prompted, enter the path to your invoice PDF.
    - **Text Extraction:** The application will extract text from the PDF and display a snippet.
    - **Interactive Q&A:** Ask questions about the invoice (e.g., "What is the total amount?" or "When is the due date?"). Type `exit` or `quit` to end the session.

3. **Example Interaction**

    ```
    Enter the path to your PDF file: /path/to/invoice.pdf

    Extracting text from PDF...
    Text extraction successful.

    --- Extracted Text Snippet ---
    --- Page 1 ---
    Invoice Number: 12345
    Date: 09/02/2025
    Total: $500.00
    ...

    PDF processing complete. You can now ask questions about the PDF.
    Type 'exit' or 'quit' to end the session.

    Your question: What is the invoice number?
    Answer: 12345

    Your question: exit
    Exiting the Q&A session.
    ```

## Project Structure

```
AI-POWERED-DOCUMENT-PROCESSING-
├── app.py          # Main application logic (PDF extraction and interactive Q&A)
├── .env            # Environment file containing sensitive information (API key)
├── requirements.txt# Lists required Python packages
├── README.md       # Project documentation (this file)
└── .gitignore      # Specifies files and directories to be ignored by Git
```

## Troubleshooting & Tips

-   **Large PDFs:** If the invoice PDF is very large, consider summarizing or chunking the text to avoid token limits with the Groq API.
-   **API Errors:** Ensure that your `GROQ_API_KEY` is valid and correctly set in your `.env` file.
-   **Environment Issues:** Verify that all required packages are installed. Use `pip freeze` to check installed versions if needed.
-   **Customization:** Feel free to modify the `system_message` content in `app.py` to tailor the context provided to the AI.

## Acknowledgments

-   [pdfplumber](https://github.com/jsvine/pdfplumber) for robust PDF text extraction.
-   [Groq](https://www.groq.ai/) for providing powerful LLM chat completion capabilities.
-   The open-source community for continuous support and contributions.
