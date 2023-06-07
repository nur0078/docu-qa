from flask import Flask, request, render_template
import openai
import os

app = Flask(__name__)

# Set your API key and organization ID here
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORGANIZATION_ID")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/answer', methods=['POST'])
def answer_question():
    document = request.files['document']
    question = request.form['question']

    # Read the content of the document
    document_text = document.read().decode('utf-8')

    # Call the language model API
    response = openai.Completion.create(
        engine="text-davinci-003",  # Replace with your desired language model
        prompt=f"Document: {document_text}\nQuestion: {question}\nAnswer:",
        max_tokens=100  # Adjust as needed
    )

    answer = response.choices[0].text.strip()

    # Postprocess the answer if needed

    return answer


if __name__ == '__main__':
    app.run(debug=True)
