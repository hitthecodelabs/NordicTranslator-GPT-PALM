# NordicTranslator-GPT-PALM

## Project Overview
This project focuses on translating article titles and descriptions from English to Norwegian using advanced language models. We leverage two leading models: GPT (versions 3.5 and 4) and PALM (Text-Bison models), to achieve high-quality translations focusing on eCommerce platforms.

## Methodology
- **Input**: English text (titles and descriptions).
- **Processing**: Utilizing GPT-3.5/GPT-4 and Text-Bison models through their respective APIs.
- **Output**: Translated content in Norwegian, formatted in JSON.

## Features
- **Bilingual Translation**: Converts English text into Norwegian while preserving the original context and nuances.
- **Dual Model Approach**: Uses the strengths of both GPT and PALM models for translation.
- **JSON Output**: Easy integration and usage in various applications due to JSON format.

## Dependencies

   To run this project, you need to install the following Python libraries:
   
   ```bash
   !pip install openai --quiet
   !pip install -q "shapely<2.0.0"
   !pip install python-telegram-bot==13.7 --quiet
   !pip install -q google-cloud-aiplatform==1.35.0
   ```

## Setup and Authentication
1. OpenAI GPT API
   
   Set your OpenAI API key:
   ```python
   import os
   from openai import OpenAI
   
   client = OpenAI(
    # api_key='your-api-key',
    api_key=os.environ.get("OPENAI_API_KEY")
   )
   ```
3. Google PALM API using Google Colab
   
   Initialize Vertex AI with your Google Cloud project details:
   ```python
   from google.colab import auth as google_auth
   google_auth.authenticate_user()
   ```
   ```python
   import vertexai
   from vertexai.language_models import TextGenerationModel
   from google.api_core.exceptions import ResourceExhausted
   
   vertexai.init(project="your-gcp-project", location="your-gcp-location")

   parameters = {
    "candidate_count": 1,
    "max_output_tokens": 2048,
    "temperature": 1,
    "top_p": 0.8,
    "top_k": 40
   }
   
   model = TextGenerationModel.from_pretrained("text-bison")
   ```

## Using the APIs
To use both APIs, you will be sending prompts to each model and then processing their outputs.

### GPT API Usage
1. Create a prompt for the GPT model.
2. Send the prompt to the GPT API and retrieve the response:

   ```python
   prompt = "your-prompt-for-gpt"
   title_response = client.chat.completions.create(
       messages=[{"role": "user","content": prompt}],
       model="gpt-4",
   )
   json_output_gpt = title_response.choices[0].message.content.strip()
   ```
3. Bonus: Calculating number of tokens in a prompt.

   The function `num_tokens_from_string` takes a string (the prompt) and an encoding name. It first tries to get the encoding directly using tiktoken.get_encoding.
   ```python
   import tiktoken
   
   def num_tokens_from_string(string: str, encoding_name: str) -> int:
       """
       Returns the number of tokens in a text string according to a specified encoding.
   
       Parameters:
       string (str): The text string to be tokenized.
       encoding_name (str): The name of the encoding or model to use for tokenization. 
           Encoding values: cl100k_base, r50k_base, p50k_base.
           Model values: gpt-3.5-turbo, gpt-4.
   
       Returns:
       int: The number of tokens in the text string.
       """
       try:
           # Attempt to get the encoding directly
           encoding = tiktoken.get_encoding(encoding_name) ### cl100k_base, r50k_base, p50k_base
       except ValueError:
           # If direct retrieval fails, attempt to map the model name to an encoding
           try:
               encoding = tiktoken.encoding_for_model(encoding_name) ### gpt-3.5-turbo, gpt-4
           except KeyError as e:
               # If mapping also fails, raise the error
               raise e
   
       # Encode the string and return the number of tokens
       l_tokens = encoding.encode(string)
       num_tokens = len(l_tokens)
       return num_tokens, l_tokens
   ```

Don't forget to install `tiktoken` by running `pip install tiktoken`.

### PALM API Usage
1. Set parameters for the PALM model.
2. Send the same or a modified prompt to the PALM API and retrieve the response:
   ```python
   prompt = "your-prompt-for-gpt"
   response_palm = model.predict(prompt, **parameters)
   json_output_palm = [i.text for i in response_palm.candidates]
   ```
## Combining the Outputs
After receiving responses from both APIs, you can compare, contrast, or combine the outputs as needed for your project. This might involve additional processing or data manipulation based on your specific requirements.

## Script Overview
The main Python script performs several key functions:

1. GPT Notebook
   - Translation and Generation: It takes English titles, sends them to the LLM API, and retrieves Norwegian translations.
   - Data Handling: Combines CSV files, processes data, and handles errors efficiently.
   - Custom Functions: Includes functions like replace_mayusculas_noruego for specific text manipulations in Norwegian.
2. PALM Notebook
   - Translation and Generation: Takes titles and descriptions, sends them to the PALM API, and retrieves translations.
   - Vertex AI Integration: Uses Vertex AI for managing model interactions.
   - Custom Functions: Includes specific text manipulations and data handling routines.


## Acknowledgements
- GPT-3.5 and GPT-4 by OpenAI
- PALM (Text-Bison) by Google

## Contributing
Contributions to NordicTranslator-GPT-PALM are welcome! Here's how you can contribute:

Fork the repository on GitHub.
Create a new branch for your proposed feature or fix.
Commit your changes with an informative description.
Push your branch and submit a pull request.
We appreciate your input!

## License
NordicTranslator-GPT-PALM is open source software licensed under the MIT License. See the LICENSE file for more details.


