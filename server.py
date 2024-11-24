import asyncio
import websockets
import json
from model_class import AIModel  


# Define the system prompt template
system_prompt = """
You are an AI tutor evaluating a student's answer to a question about artificial intelligence. Your task is to:
1. Provide a score from 0 to 100 based on the accuracy and completeness of the answer.
2. Give detailed, constructive feedback to help the student improve. 
   
Feedback should be clear, concise, and suggest specific improvements. Avoid overly verbose responses. 

For example:  
- **Question**: "What is supervised learning?"  
- **Student Answer**: "It uses labeled data for training."  
- **Your Response**:  
  - **Score**: 70/100  
  - **Feedback**: "Partially correct. You should mention that supervised learning involves mapping inputs to outputs using labeled data, and provide examples like classification or regression."
"""

# Define model path to use it to load the model
model_path = 'Phi-3.5-mini-instruct/'
tokenizer_path = 'Phi-3.5-mini-instruct/'
# Initialize the AI model
# Please note that I work localy so I downloaded model weghits and then load them using this class 
# Make Sure you have the model loded and clarify its path in the prev varibales
model = AIModel(model_path,tokenizer_path, system_prompt)

# Response cache to improve performance
response_cache = {}

async def handle_request(websocket):
    try:
        # Receive the question and student answer from client
        data = await websocket.recv()
        request_data = json.loads(data)
        question = request_data.get("question")
        student_answer = request_data.get("student_answer")
        
        # Check if the response is cached
        cache_key = f"{question}_{student_answer}"
        if cache_key in response_cache:
            await websocket.send(response_cache[cache_key])
            return

        # Generate feedback using the AI model
        feedback = model.generate_feedback(question, student_answer)

        # Cache the response
        response_cache[cache_key] = feedback

        # Send the feedback to the client
        await websocket.send(feedback)
    except Exception as e:
        await websocket.send(f"Error: {str(e)}")

async def main():
    server = await websockets.serve(handle_request, "localhost", 8765)
    await server.wait_closed()

# Run the server
asyncio.get_event_loop().run_until_complete(main())
