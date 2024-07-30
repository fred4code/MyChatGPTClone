# Overview
This project is a prototype for a clone of ChatGPT utilizing the OpenAI API. The clone has been implemented in HTML with CSS and jQuery for the client-side (the part where the end user interacts), and Python for the server-side (the part where the API calls are made).

The application consists of three files: `MyChatGPTCloneHTTPServer.py`, `MyChatGPTCloneOnHTTPServer.html`, and `config.json`.

`config.json` is where you need to set up the API Key obtained from your OpenAI Account.

`MyChatGPTCloneHTTPServer.py` is the server-side configured to use the GPT-3.5 model.

`MyChatGPTCloneOnHTTPServer.html` is the end-user interface that you can open in your browser.

# Important Notes
You can change the GPT-3.5 model in the `MyChatGPTCloneHTTPServer.py` file, but before doing so, consider the following:

- You pay for every request made using the API.
- The 3.5 model is cheaper than the 4.0 model.
- This application maintains the memory of the conversation until the maximum token limit per request is reached. You pay for the number of tokens in each request. In simpler terms, the more you chat, the more you pay. This application is intended for study purposes only (i.e., a limited number of requests for testing, thus incurring minimal costs). If you plan to have extensive chat usage, consider using ChatGPT instead.

# How to Set It Up and use it
After downloading, you have to:

1) Create an OpenAI Account to use the API.
2) Ensure Python is installed on your system, capable of importing the following libraries: `http.server`, `socketserver`, and `json`.
3) Enter your API key in the `config.json` file. Be sure to keep your API key secret and do not share it. If you no longer intend to use the key, ensure it is removed from both the `config.json` file and your OpenAI account.
4) Start the server-side by running the following command: `python MyChatGPTCloneHTTPServer.py`, or by running the script from an IDE that supports Python.
5) Open `MyChatGPTCloneOnHTTPServer.html` in your browser. If everything works correctly, you will see: "[gpt]: Hello! How can I assist you today?"
6) Type your input in the "Write your question here..." section and press ">" to get a response.
7) The "f" button is for full screen.
8) The "z" button is for zoom.
9) The "+" button is for starting a new chat. Alternatively, you can also type "NEW_CHAT" in the "Write your question here..." section to start a new chat.
10) Logging: Various logs have been implemented for troubleshooting:
    - Client-side: Press F12 in your browser, and you will see some log messages in the console.
    - Server-side: In the console window where the Python script is running, you will see the messages being sent and the responses received.

# Known Issues
Sometimes, the application may freeze with no response from the Python server. To resolve this, terminate the Python process, restart it, close the browser and reopen the file MyChatGPTCloneOnHTTPServer.html.

# Further Reading
For more information on the OpenAI API, example uses, and extensive documentation, please visit the official OpenAI platform at [https://platform.openai.com/](https://platform.openai.com/).

# Screenshot
A screenshot of the front end chat (on the left) with the backend server in python with the response from the OpenAI API (on the right):

![image](https://github.com/user-attachments/assets/9a97d4cd-748a-47f7-87a8-21444f81019e)

