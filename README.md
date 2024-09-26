# Llama 3.2 Models using AWS Bedrock

This project demonstrates how to use Llama 3.2 models, specifically the 11B Instruct v1 version, through AWS Bedrock. It showcases the capabilities of these large language models in processing and analyzing images along with text prompts.

## Features

- Utilizes AWS Bedrock to access Llama 3.2 models
- Supports image and text input for versatile queries
- Demonstrates OCR-like capabilities for image analysis

## Prerequisites

- AWS account with access to Bedrock
- Python 3.x
- Boto3 library
- Proper AWS credentials configured

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/llama-3-2-aws-bedrock.git
   cd llama-3-2-aws-bedrock
   ```

2. Install required dependencies:
   ```
   pip install boto3
   ```

3. Configure your AWS credentials (if not already done):
   ```
   aws configure
   ```

## Usage

# Llama 3.2 Models using AWS Bedrock

[... previous sections remain unchanged ...]

## Usage

1. Prepare your image file (e.g., `converted_image.png`).
   **Important:** The model only considers pixels within a 1024x1024 area. If your image is larger, only the top-left 1024x1024 pixel region will be processed. For best results, resize your image to 1024x1024 or smaller before processing.

2. Modify the `user_message` in the script to suit your specific query.

3. Run the script:
   ```
   python llama_3_2_bedrock.py
   ```

4. The script will output the model's response, which includes the analysis based on the image and text prompt.

Tip: If you're working with larger images, consider using image processing libraries like Pillow (PIL) to resize your images before sending them to the model:

```python
from PIL import Image

def resize_image(image_path, size=(1024, 1024)):
    with Image.open(image_path) as img:
        img.thumbnail(size)
        img.save('resized_' + image_path)

# Use this function before processing your image
resize_image('your_image.png')
```

This will ensure that all the relevant parts of your image are considered in the model's analysis.

5. Modify the `user_message` in the script to suit your specific query.

6. Run the script:
   ```
   python llama_3_2_bedrock.py
   ```

7. The script will output the model's response, which includes the analysis based on the image and text prompt.

## Example

Here's an example of the model's response to an OCR-like task:

![Model Response](/images/response.png)

This example shows the model's ability to recognize and transcribe handwritten text from an image.

## Model Details

- Model ID: `us.meta.llama3-2-11b-instruct-v1:0`
- This model is part of the Llama 3.2 family, known for its advanced language understanding and generation capabilities.

## Important Notes

- Ensure you have the necessary permissions and comply with AWS Bedrock's terms of service.
- Be mindful of the costs associated with using AWS Bedrock and Llama models.
- The accuracy of image analysis and text generation may vary depending on the input quality and specificity of the prompt.
