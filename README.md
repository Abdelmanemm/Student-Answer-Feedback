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

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Download and Place the Model**:
- Download the[Phi-3.5-mini-instruct](https://huggingface.co/) model files.
- Place the files in a folder named Phi-3.5-mini-instruct/ in the project root.
4. **Run the Server**:
     ```bash
      python server.py
     ```
5. **Run the Client**:
   ```bash
   python client.py
   ```
Enter a question and student response when prompted to receive feedback.

---

## File Structure
```
.
├── model_class.py    # Handles model initialization and feedback generation
├── server.py         # WebSocket server implementation
├── client.py         # Client implementation for interaction
├── unitest.py        # Unit tests to verify system functionality
├── requirements.txt  # List of dependencies
└── README.md         # Project documentation
```

---

## Example Usage
### Running Client
```bash
python client.py
```
input Example
```vbnet
Question: What is supervised learning?
Answer: It is when data is labeled.
```
output Example
```vbnet
Score: 75/100
Feedback: "Correct, but incomplete. Supervised learning involves training models on labeled datasets to map inputs to outputs. Examples include classification and regression."
```

---
## Testing
**Run the unit tests to verify system functionality**:
```bash
python -m unittest unitest.py
```
---

## Known Issues
- Large inputs may cause delays; adjust the max_new_tokens parameter for optimization.
- Ensure the model path is correctly set in server.py.

---

## Contributions
Contributions are welcome! Feel free to fork the repository and submit pull requests for improvements or bug fixes.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

  
