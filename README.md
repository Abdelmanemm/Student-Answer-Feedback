# Student-Answer-Feedback
This project is a **Student Answer Feedback System** designed to evaluate student responses to AI-related questions. The system uses a **language model** to generate detailed feedback and assign scores to student answers, helping improve their understanding and learning outcomes.

---

## Features

1. **AI-Generated Feedback**:
   - Provides a score (0–100) based on the accuracy and completeness of the answer.
   - Offers detailed, constructive feedback to improve student learning.

2. **WebSocket Communication**:
   - Enables seamless interaction between a client and server using asynchronous WebSocket communication.

3. **Response Caching**:
   - Reduces redundant computations by caching responses for repeated queries.

4. **Error Handling**:
   - Robust handling of invalid inputs, timeouts, and server-side errors.

---

## System Components

### 1. **Model**
The system uses the [Phi-3.5-mini-instruct](https://huggingface.co/) language model for generating feedback. It uses Hugging Face's `transformers` library to initialize the model and tokenizer.

### 2. **Server**
The `server.py` file implements an asynchronous WebSocket server that:
   - Receives questions and student answers from the client.
   - Generates feedback using the AI model.
   - Sends the feedback back to the client.

### 3. **Client**
The `client.py` file allows users to:
   - Input a question and a student's answer.
   - Send the data to the server and receive feedback.

### 4. **Unit Testing**
The `unitest.py` file includes comprehensive unit tests to ensure the reliability of the AI model and system functionality.

---

## How to Set Up and Use

### Prerequisites
- Python 3.8 or higher
- CUDA-compatible GPU (optional but recommended for faster model inference)
- Required Python libraries:
  - `transformers`
  - `torch`
  - `websockets`

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
