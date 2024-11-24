import asyncio
import websockets
import json

async def send_question(question, student_answer):
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        # Send the question and student answer to the server
        data = {"question": question, "student_answer": student_answer}
        await websocket.send(json.dumps(data))

        # Receive the feedback from the server
        response = await websocket.recv()
        print(response)

# Example question and answer
question = input("Question: ")
student_answer = input("Answer: ")

# Run the client
asyncio.run(send_question(question, student_answer))
