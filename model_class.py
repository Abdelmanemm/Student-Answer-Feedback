from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import time

class AIModel:
    """
    A class for managing the AI model and generating feedback based on student responses.

    Attributes:
        model_name (str): The name or path of the model.
        model (PreTrainedModel): The loaded AI model for text generation.
        tokenizer (PreTrainedTokenizer): The tokenizer corresponding to the model.
        system_prompt (str): The system-level prompt to guide the model's behavior.
        pipe (pipeline): The pipeline for text generation.

    Methods:
        generate_feedback(question, student_answer):
            Analyzes the students answer to the given question and generates feedback.
    """
    def __init__(self, model_path: str, tokenizer_path: str, system_prompt: str):
        """
        Initializes the AI model, tokenizer, and generation pipeline.

        Parameters:
            model_path (str): The local path to the pre-trained model weights.
            tokenizer_path (str): The local path to the tokenizer files.
            system_prompt (str): The system prompt that instructs the model on how to respond.
        """
        # Initialize the model and tokenizer from local paths
        self.model_name = model_path
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path, 
            device_map="cuda", 
            torch_dtype="auto", 
            trust_remote_code=True
        )
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
        self.system_prompt = system_prompt
        
        # Initialize the pipeline for text generation
        self.pipe = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
        )
    
    def generate_feedback(self, question: str, student_answer: str) -> str:
        """
        Generates feedback based on the student's answer to the given question.
        
        Parameters:
            question (str): The question posed to the student.
            student_answer (str): The student's response to the question.
        
        Returns:
            str: Feedback, including a score and suggestions for improvement.
        """

        # Validate input types
        if not isinstance(question, str) or not isinstance(student_answer, str):
            raise ValueError("Both question and student_answer must be strings.")
        
        # Handle empty answer case
        if not student_answer or student_answer.strip() == "":
            return "Score: 0\nFeedback: No response provided. Please attempt to answer even if unsure."
        
        if not question:
            return "Error: Question must be provided."
        
        # Prepare the input messages for the model
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": f"Question: {question}"},
            {"role": "user", "content": f"Student Answer: {student_answer}"},
        ]
        
        # Define generation parameters
        generation_args = {
            "max_new_tokens": 500,
            "return_full_text": False,
            "temperature": 0.0,
            "do_sample": False,
        }
        
        # Add timeout error handling
        try:
            start_time = time.time()
            output = self.pipe(messages, **generation_args)
            elapsed_time = time.time() - start_time
            
            # Check if the response time exceeds threshold
            if elapsed_time > 60:  # Timeout threshold of 60 seconds
                return "Error: Request timed out. Please try again."
            
            return output[0]['generated_text']
        
        except Exception as e:
            return f"An error occurred: {str(e)}"

