#ArcGPT - Cloud Architecture Diagram Generator

##Overview

ArcGPT is a tool that generates cloud architecture diagrams using the Diagrams library, integrated with LangChain and OpenAI for AI-powered diagram creation. This application enables users to describe their cloud architecture in natural language and generates corresponding visual diagrams.

##Installation Guide (Windows)

Follow these steps to install the required dependencies and set up ArcGPT on your Windows machine.

###1. Install Python

Ensure you have Python 3.8+ installed. If not, download and install it from Python Official Website.

###2. Set Up a Virtual Environment (Optional but Recommended)

python -m venv arcgpt-env
arcgpt-env\Scripts\activate

###3. Install Required Libraries

Run the following commands to install dependencies:

pip install diagrams langchain openai graphviz

###4. Install Graphviz (Required for Diagrams Library)

Download Graphviz from: Graphviz Download

Install it and add the installation path to your system environment variables.

Verify the installation by running:

dot -V

You should see the Graphviz version output.

##Usage

After installing all dependencies, you can start using ArcGPT by running:

python app.py

Provide your architecture description, and the system will generate a diagram automatically.

##License

ArcGPT is an open-source project. Feel free to contribute!

