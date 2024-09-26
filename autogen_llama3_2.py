import os
from autogen import UserProxyAgent, AssistantAgent

config_list = [
    {
        "api_type": "bedrock",
        "model": "us.meta.llama3-2-11b-instruct-v1:0",
        "aws_region": "us-east-1",
        "aws_access_key": os.getenv("AWS_ACCESS_KEY"),
        "aws_secret_key": os.getenv("AWS_SECRET_KEY"),
    }
]


user_proxy = UserProxyAgent(
    "user",
    code_execution_config=False
)

assistant = AssistantAgent(
    "assistant",
    llm_config={
        "config_list": config_list,
        "cache": None,
        "cache_seed": None
    }
)

user_proxy.initiate_chat(
    assistant,
    message="Write a blog post on the topic of artificial intelligence and its impact on society with consideration \
    of security. Generate the blog post in Markdown format only.",
)

blog = assistant.last_message()["content"]
with open("blog_post.md", "w") as f:
    f.write(blog)

