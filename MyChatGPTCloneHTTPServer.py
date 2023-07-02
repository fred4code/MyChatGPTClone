# This python script MyChatGPTCloneHTTPServer.py is licensed under the MIT License.
# See http://opensource.org/licenses/MIT for more information.
#
# Copyright (c) 2023 fred4code

# Import the required libraries
import http.server
import socketserver
import json


class MChatGPTClone():
    
    def __init__(self, pApiKey):
        import openai as oai
        self.MP_oai = oai
        self.MP_oai.api_key = pApiKey

    def MF_Initialize(self):  
        self.MP_messages = []
        self.MP_messages.append({"role": "system", "content": "An all purpose assistant"})
        
    def format_conversation_history(self, conversation):
        formatted_text = ""
        for message in conversation:
            role, content = message["role"], message["content"]
            formatted_text += f"{role}: {content}\n"
        return formatted_text
        
    def MF_SendMessage(self, pMessage):
        self.MP_messages.append({"role": "user", "content": pMessage})
        response = self.MP_oai.ChatCompletion.create(model="gpt-3.5-turbo", messages=self.MP_messages)
        print("Response:")
        print(response)
        answer = response["choices"][0]["message"]["content"]
        
        self.MP_messages.append({"role": "assistant", "content": answer})
        print("Messages:")
        print(self.MP_messages)
        
        return answer


# Define the main server class
class MSimpleServer:

    # Define a request handler class
    class MSimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):

        # Define a method to set the CORS headers
        def MM_CorsHeaders(self):
            # Set the CORS headers
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')

        # Handle OPTIONS request to include CORS headers
        def do_OPTIONS(self):
            # Send response with CORS headers
            self.send_response(200, "ok")
            self.MM_CorsHeaders()
            self.end_headers()


        # Handle POST request to include CORS headers
        def do_POST(self):
            # Read the content length and post data
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)

            # Process the data as needed
            #print("Data received: ", data)

            # Send response with CORS headers
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.MM_CorsHeaders()
            self.end_headers()

            # Process the data using the custom function
            response = self.server.MM_MethodToProcessRequest(data)
            # Send the response data
            self.wfile.write(json.dumps(response).encode())

    # Initialize the server with the specified IP, port, and custom function
    def __init__(self, pMethodToProcessRequest, pIp, pPort):
        self.MP_Ip = pIp
        self.MP_Port = pPort
        self.MM_MethodToProcessRequest = pMethodToProcessRequest
        requestHandlerClass = self.MSimpleHTTPRequestHandler
        with socketserver.TCPServer((self.MP_Ip, self.MP_Port), RequestHandlerClass=requestHandlerClass) as socketserver_TCPServer:
            socketserver_TCPServer.MM_MethodToProcessRequest = self.MM_MethodToProcessRequest
            print(f"Serving on {self.MP_Ip}:{self.MP_Port}")
            socketserver_TCPServer.serve_forever()


# Start the server with the custom function
if __name__ == "__main__":
         
    # Initialize the ChatGPT variable
    MV_ChatGPT = None
    MV_ConfigFile = open('config.json')
    MV_ConfigData = json.load(MV_ConfigFile)
    MV_ConfigFile.close()  
    
    # Custom function to process the data and generate a JSON response
    def MF_MethodToProcessRequest(pData):

        # Check if the message is "NEW_CHAT"
        if pData['question'] == "NEW_CHAT":
                     
            # Access the global variables
            global MV_ChatGPT
            global MV_ConfigFile
            
            # Initialize the ChatGPT instance
            MV_ChatGPT = MChatGPTClone(MV_ConfigData["apikey"])
            MV_ChatGPT.MF_Initialize()
            # Send the message to the ChatGPT instance and get the result
            response = MV_ChatGPT.MF_SendMessage(pData['question'])
            
            #print("Data sent: ", response)
            return response
        # If the message is not "NEW_CHAT"
        else:
            # Send the message to the ChatGPT instance and get the result
            response = MV_ChatGPT.MF_SendMessage(pData['question'])
            
            #print("Data sent: ", response)
            return response
    
    
    #
    mSimpleServer = MSimpleServer(MF_MethodToProcessRequest, pIp=MV_ConfigData['host'], pPort=int(MV_ConfigData['port']))
    
    
 
    


    



