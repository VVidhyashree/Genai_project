import openai
import os
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

# Set your OpenAI API Key securely
os.environ["OPENAI_API_KEY"] = "your-openai-key"  # Replace with your actual API key

# Define a prompt template
prompt = PromptTemplate(
    input_variables=["description"],
    template="Create a detailed visual artwork based on: {description}"
)

# Initialize the OpenAI model
llm = OpenAI(temperature=0.7)

# Function to generate image using OpenAI's DALL-E (new method)
def generate_image(description):
    response = openai.Image.create(
        prompt=description,
        n=1,  # Number of images
        size="1024x1024"  # Image size (you can adjust)
    )
    image_url = response['data'][0]['url']
    return image_url

# Function to get user input
def get_user_input():
    description = input("Describe the image you want to generate: ")
    return description

def main():
    # Get user input (description for image)
    description = get_user_input()

    # Use the prompt template to generate a detailed prompt for DALL-E
    enhanced_prompt = prompt.format(description=description)

    # Use the OpenAI model to process the prompt and generate an image
    image_url = generate_image(enhanced_prompt)

    # Print the generated image URL
    print(f"Your generated image is available at: {image_url}")

if __name__ == "__main__":
    main()
