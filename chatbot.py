import openai
import traceback
import re

# Import your script execution functions
from script_generator import generate_script, run_script

def get_response(prompt, chat_history, model="gpt-4", temperature=1):
    chat_history.append({
        "role": "user",
        "content": prompt
    })
    
    response = openai.ChatCompletion.create(
        model=model,
        messages=chat_history,
        temperature=temperature,
    )
    
    chat_history.append({
        "role": "assistant",
        "content": response.choices[0].message['content']
    })
    
    return response.choices[0].message['content']

def extract_text_from_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return str(e)

def main():
    key = extract_text_from_file('openai_key.txt')
    openai.api_key = key
    
    chat_history = [
        {
            "role": "system",
            "content": """
            You are a helpful assistant. 
            If the user is requesting a script, or if a task would be completed easier with a script, write the following:
            [SCRIPT DESCRIPTION]
            description of the script you need
            [SCRIPT DESCRIPTION]

            Anything within the [SCRIPT DESCRIPTION] section will be written into a script and then executed.
            The outputs of the script will be given back to you so you can better answer the user's question.
            If the user asks you to modify a script, but the previous version of the script with the modification request within the [SCRIPT DESCRIPTION] section.
            """
        }
    ]
    
    while True:
        try:
            prompt = input("\n\033[37mUser: \033[0m")
            response = get_response(prompt, chat_history)

            # Check for SCRIPT directive
            matches = re.findall(r"\[SCRIPT DESCRIPTION\](.*?)\[SCRIPT DESCRIPTION\]", response, re.DOTALL)

            if matches:
                print(f"\n\033[90mGPT-4: {response}\033[0m")
                for script_description in matches:
                    # Generate script
                    script = generate_script(script_description.strip())
                    # Run script
                    result = run_script(script, script_description.strip())
                    print(f"\n\033[34mEXECUTOR: {result}\033[0m")
                    response = get_response(result, chat_history)
                    print(f"\n\033[90mGPT-4: {response}\033[0m")

            else:
                print(f"\n\033[90mGPT-4: {response}\033[0m")

        except Exception as e:
            error_message = traceback.format_exc()
            with open("error.txt", "a") as error_file:
                error_file.write(f"An error occurred: {str(e)}\n")
                error_file.write(f"Traceback:\n{error_message}\n")
            print(f"An error occurred and has been written to error.txt. Error: \033[91m{str(e)}\033[0m")

if __name__ == "__main__":
    main()
