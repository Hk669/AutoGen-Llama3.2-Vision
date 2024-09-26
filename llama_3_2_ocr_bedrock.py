import boto3
import json

MODEL_ID = "us.meta.llama3-2-11b-instruct-v1:0"
# MODEL_ID = "us.meta.llama3-2-90b-instruct-v1:0"

IMAGE_NAME = "./images/mlnotes-res.png"

bedrock_runtime = boto3.client("bedrock-runtime", region_name="us-east-1")

try:
    with open(IMAGE_NAME, "rb") as f:
        image = f.read() # the max pixels is 1024x1024 for the llama3-2-11b-instruct-v1 model in AWS Bedrock

    user_message = """You are an OCR assistant specialized in handwritten text recognition. Please analyze the 
    provided image of handwritten notes and:

    1. Transcribe all visible text in the image as accurately as possible.
    2. Maintain the original structure and formatting of the notes (e.g., bullet points, numbered lists, sections) in your transcription.
    3. If any words or phrases are unclear or ambiguous, indicate this with [unclear] in your transcription.
    4. After the transcription, provide a brief summary (2-3 sentences) of the main topics or ideas covered in the notes.

    Please begin your response with the transcription, followed by the summary. Aim for the highest possible accuracy in your text recognition.

    Transcription:
    [Your transcription here]

    Summary:
    [Your summary here]
    """

    messages = [
        {
            "role": "user",
            "content": [
                {"image": {"format": "png", "source": {"bytes": image}}},
                {"text": user_message},
            ],
        }
    ]

    response = bedrock_runtime.converse(
        modelId=MODEL_ID,
        messages=messages,
    )
    
    if 'output' in response and 'message' in response['output'] and 'content' in response['output']['message']:
        response_text = response["output"]["message"]["content"][0]["text"]
        print("Model response:\n--------\n")
        print(response_text)
        
    else:
        print("Unexpected response structure from the model.")

except Exception as e:
    print(f"An error occurred: {str(e)}")
