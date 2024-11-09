import requests

# Set your Gemini API key here
GEMINI_API_KEY = "YOUR_API_KEY_HERE"

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

def create_gemini_prompt(content, parse_description):
    """Creates the prompt for the Gemini API using the content and description."""
    return template.format(dom_content=content, parse_description=parse_description)

def parse_with_gemini(chunks, parse_description):
    """Sends requests to the Gemini API and parses responses."""
    parsed_results = []

    for i, chunk in enumerate(chunks, start=1):
        prompt = create_gemini_prompt(chunk, parse_description)

        # Sending request directly to the Gemini AI API
        response = requests.post(
            "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent",
            headers={
                "Authorization": f"Bearer {GEMINI_API_KEY}",
                "Content-Type": "application/json"
            },
            json={"prompt": prompt}  # Adjust the payload according to Gemini API documentation
        )

        if response.status_code == 200:
            reply = response.json().get('content', '').strip()  # Adjust according to the actual response format
            print(f"parsed_batch {i} of {len(chunks)}")
            parsed_results.append(reply)
        else:
            print(f"Error: {response.status_code} - {response.text}")
            parsed_results.append("")  # Append empty string on error

    return "\n".join(parsed_results)

def main():
    """Main function to read local files or use predefined chunks."""
    # Example of predefined chunks of content
    chunks = ["This is the first piece of content.", "This is the second piece of content."] 
    
    # Or read from a local text file
    # with open('example.txt', 'r') as file:
    #     chunks = file.readlines()

    parse_description = input("Describe what you want to parse: ")

    result = parse_with_gemini(chunks, parse_description)
    print("Parsed Results:")
    print(result)

