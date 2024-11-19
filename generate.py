import google.generativeai as genai

genai.configure(api_key="AIzaSyCx30VTgLMHUAcurHuCA_EZevWOQlxCiPg")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

def angel(prompt):
    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

    convo = model.start_chat(history=[
    ])

    convo.send_message(prompt)
    message=convo.last.text
    print(message)
    return message

def gen_text(path,query):

    # Upload the file and print a confirmation.
    sample_file = genai.upload_file(path=path)

    # Choose a Gemini API model.
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Prompt the model with text and the previously uploaded image.
    response = model.generate_content([sample_file, query])
    print("Response: "+response.text)
    return response.text