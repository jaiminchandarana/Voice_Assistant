from audio import speak,takecommand
import pandas as pd
import re
from textblob import TextBlob

def choice():
    if choice:
        input()
    else:
        speak("Would you like to give voice command or text command sir.")
        choice = takecommand().lower()
        input()
        
    def input():
        if "voice" in choice:
            user_prompt = takecommand().lower()
            return user_prompt
        elif "text" in choice:
            user_prompt = input("Enter your analysis prompt: ")
            return user_prompt
        else:
            speak("Please select from voice or text")
            choice()
        
def load_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        speak("Data loaded successfully sir!")
        return data
    except Exception as e:
        speak(f"Error in loading Data sir.")
        return None

def analyze_data(df, prompt):
    prompt = prompt.lower()
    
    if "summary" in prompt or "describe" in prompt:
        description = df.describe(include='all')
        speak(f"summary is {description} sir.")

    elif "missing values" in prompt:
        Missing_value = df.isnull().sum()
        speak(f"There are {Missing_value} missing values sir.")

    elif "correlation" in prompt or "corelation" in prompt:
        correlation =  df.corr()
        speak(f"Correlation of Matrix is {correlation} sir.")

    elif "unique" in prompt:
        column = extract_column_name(prompt, df.columns)
        if column:
            unique =  df[column].unique()
            speak(f"Unique values in column {column} is {unique} sir.")
        else:
            return "Column not found. Please specify a correct column name."

    elif "average" in prompt or "mean" in prompt:
        column = extract_column_name(prompt, df.columns)
        if column:
            average =  df[column].mean().round()
            speak(f"Average of column {column} is {average}.")
        else:
            return "Column not found sir."

    else:
        return "Please try again sir."

def extract_column_name(prompt, columns):
    matched_columns = [col for col in columns if col.lower() in prompt.lower()]
    return matched_columns if matched_columns else None


if __name__ == "__main__":
    file_path = input("Enter the CSV file path: ")
    data = load_csv(file_path)

    if data is not None:
        speak(f"\nColumns in the data: {list(data.columns)}")
        user_prompt = input("Enter your analysis prompt: ")
        result = analyze_data(data, user_prompt)
        speak("\nAnalysis Result:")
        speak(result)