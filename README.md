# 🤖 Custom Code Interpreter
This script serves as an Artificial Intelligence (AI) chatbot 🧠💬, capable of generating and executing scripts based on provided specifications. Basically a custom code interpreter similar to OpenAI's.

## 🔄 How It Works
You can interact with GPT4 in the console window as you would normally. If the GPT4 detects any script-related instructions within the response, it offloads the task to a script generator and executor. It does this by using [SCRIPT DESCRIPTION] tags in its answers. Anything within those tags will be sent to the script writer as feature requirements. If GPT4 does not use these tags while answering your question about scripts, you can remind it by using the following prompt:

```Remember to use the [SCRIPT DESCRIPTION] tags```

## 🏗️ Set Up
To use this you will need an OpenAI api key. I have not tested this with GPT3.5 but I imagine it would still work reasonably fine. You would need to remind it of its ability to use the tags more often I assume. if you don't have an API key, here's how you can get one:

#### Create an OpenAI account
If you do not have an OpenAI account, you can create one by going to OpenAI's registration page. Follow the steps to set up your account.

#### Request an API key
Once your account is set up, log in and navigate to the API section. Here, you can request an API key. Make sure to keep it safe and private, as it provides access to your OpenAI account.

#### Create a .txt file and input the API key
With the API key in hand, create a new text file in the root directory of the chatbot.py script. Name this file openai_key.txt. Open this file and paste your API key here, then save and close the file.

💡 Note: Be sure not to share or upload this file, as it contains your private API key.

That's it! You are all set up! :D

## 💻 Running the Script
You can run the script using a Python interpreter in the terminal or through an IDLE interface.

Happy scripting!
