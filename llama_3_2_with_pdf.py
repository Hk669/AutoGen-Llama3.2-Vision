import boto3
from pdf2image import convert_from_path
from PIL import Image
import io
import json

# AWS Bedrock and model settings
MODEL_ID = "us.meta.llama3-2-11b-instruct-v1:0"
REGION_NAME = "us-east-1"

# PDF file to process
PDF_FILE = "./template.pdf"

# Initialize AWS Bedrock client
bedrock_runtime = boto3.client("bedrock-runtime", region_name=REGION_NAME)

def resize_image(img, size=(1024, 1024)):
    """Resize image to fit within 1024x1024 pixels"""
    img.thumbnail(size)
    return img

def image_to_bytes(img):
    """Convert PIL Image to bytes"""
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    return img_byte_arr.getvalue()

def process_page(page_image):
    """Process a single page image with the Llama 3.2 model"""
    resized_img = resize_image(page_image)
    img_bytes = image_to_bytes(resized_img)
    
    user_message = """
    Act as an OCR assistant. Analyze the provided image and:
    1. Transcribe all visible text in the image as accurately as possible.
    2. Maintain the original structure and formatting of the text.
    3. If any words or phrases are unclear, indicate this with [unclear] in your transcription.

    Provide only the transcription without any additional comments.
    """

    messages = [
        {
            "role": "user",
            "content": [
                {"image": {"format": "png", "source": {"bytes": img_bytes}}},
                {"text": user_message},
            ],
        }
    ]

    try:
        response = bedrock_runtime.converse(
            modelId=MODEL_ID,
            messages=messages,
        )
        return response["output"]["message"]["content"][0]["text"]
    except Exception as e:
        return f"Error processing page: {str(e)}"

def process_pdf(pdf_path):
    """Process all pages in the PDF"""
    pages = convert_from_path(pdf_path)
    print(pages)
    results = []

    for i, page in enumerate(pages):
        print(f"Processing page {i+1}/{len(pages)}...")
        ocr_result = process_page(page)
        results.append({"page": i+1, "text": ocr_result})

    return results

if __name__ == "__main__":
    print(f"Processing PDF: {PDF_FILE}")
    ocr_results = process_pdf(PDF_FILE)
    
    # Save results to a JSON file
    with open("ocr_results.json", "w") as f:
        json.dump(ocr_results, f, indent=2)
    
    print(f"OCR processing complete. Results saved to ocr_results.json")