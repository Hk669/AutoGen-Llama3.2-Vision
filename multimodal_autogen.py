import os
import autogen
from autogen.agentchat.contrib.multimodal_conversable_agent import (
    MultimodalConversableAgent
    )


config_list = [
    {
        "api_type": "bedrock",
        "model": "us.meta.llama3-2-11b-instruct-v1:0",
        "aws_region": "us-east-1",
        "aws_access_key": os.getenv("AWS_ACCESS_KEY"),
        "aws_secret_key": os.getenv("AWS_SECRET_KEY"),
    }
]

llama3_2_config = {
    "config_list": config_list, 
    "cache_seed": 42
    }

image_agent = MultimodalConversableAgent(
    name="image-explainer",
    max_consecutive_auto_reply=10,
    llm_config=llama3_2_config,
)

user_proxy = autogen.UserProxyAgent(
    name="User_proxy",
    system_message="A human admin.",
    human_input_mode="NEVER",  # Try between ALWAYS or NEVER
    max_consecutive_auto_reply=0,
    code_execution_config={
        "use_docker": False
    },  # Please set use_docker=True if docker is available to run the generated code. Using docker is safer than running the generated code directly.
)

user_proxy.initiate_chat(
    image_agent,
    message="""What's the image about?
<img https://raw.githubusercontent.com/Hk669/Llama3.2-Bedrock/refs/heads/main/images/mlnotes-res.png>.""",
)
