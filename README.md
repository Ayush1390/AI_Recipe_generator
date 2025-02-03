# Recipe Recommender App

## Overview

The **Recipe Recommender App** uses artificial intelligence to generate recipes based on the ingredients provided by the user. The application utilizes the Hugging Face API for text generation, and Streamlit to build a user-friendly interface.

By inputting a list of ingredients, the app will generate a recipe along with the steps on how to prepare the dish.

## Features

- **Enter Ingredients**: User can input a list of ingredients.
- **Generate Recipe**: Click on the "Recommend" button to generate a recipe and cooking instructions based on the ingredients provided.
- **Beautiful UI**: The app has a modern design with a custom background image, appealing colors, and attractive font styles.
  
## Tech Stack

- **Hugging Face API**: Used for generating the recipe.
- **Streamlit**: Framework for building the user interface.
- **Python**: Programming language used for the application.
- **dotenv**: For handling API tokens securely.

## Requirements

Before running the application, make sure you have the following libraries installed:

```
pip install -r requirements.txt
```
Here’s the content for requirements.txt:
```
streamlit
huggingface_hub
python-dotenv
```

The .env file should contain the following:
```
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token
```
Make sure to replace your_huggingface_api_token with your actual Hugging Face API token. You can obtain the token from your Hugging Face account settings.

How to Run the Application

Clone the repository:
```
git clone https://github.com/your_username/AI_Recipe_Generator.git
cd AI_Recipe_Generator
```

Install the required dependencies:
```
pip install -r requirements.txt
```

Run the app using Streamlit:
```
streamlit run app.py
```

## How it Works
- The app will prompt you to enter a list of ingredients (e.g., eggs, flour, sugar, milk, butter).
- After you click the "Recommend" button, the app will generate a recipe based on those ingredients using the Hugging Face model.
- The generated recipe, including the dish name and cooking steps, will appear in the text area on the right side of the app.

## Code Explanation
- Streamlit Layout: The app is divided into two columns. The left column contains a text area for the user to input ingredients and a button to generate the recipe. The right column displays the generated recipe.
- Hugging Face API: The Hugging Face Inference API is used to query the model (mistralai/Mistral-7B-Instruct-v0.2) for text generation.
- Styling: Custom CSS is used for styling the app, including the background image, fonts, and buttons.
- This will launch the app in your default web browser.


## Contributing
Contributions are always welcome! If you'd like to contribute, you can fork the repository, create a new branch, and submit a pull request with your changes.

- Fork the repository.
- Create a new branch for your feature (git checkout -b feature-name).
- Commit your changes (git commit -am 'Add new feature').
- Push to your branch (git push origin feature-name).
- Open a pull request.

## Live Link
https://airecipegenerator-ssm3ivajhbr8dakzjlkdk9.streamlit.app/  
