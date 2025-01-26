import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 0.7,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 65536,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  # model_name="learnlm-1.5-pro-experimental",
  # model_name="gemini-2.0-flash-exp",
  # model_name="gemini-exp-1206",
  model_name="gemini-2.0-flash-thinking-exp-01-21",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)

prompt = 'Hi'

response = chat_session.send_message(prompt)

print(response.text)
