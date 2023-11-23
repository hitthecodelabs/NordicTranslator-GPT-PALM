# NordicTranslator-GPT-PALM

## Project Overview
This project focuses on translating article titles and descriptions from English to Norwegian using advanced language models. We leverage two leading models: GPT (versions 3.5 and 4) and PALM (Text-Bison models), to achieve high-quality translations.

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
Contributions to DeepFaceRegistry are welcome! Here's how you can contribute:

Fork the repository on GitHub.
Create a new branch for your proposed feature or fix.
Commit your changes with an informative description.
Push your branch and submit a pull request.
We appreciate your input!

## License
DeepFaceRegistry is open source software licensed under the MIT License. See the LICENSE file for more details.


