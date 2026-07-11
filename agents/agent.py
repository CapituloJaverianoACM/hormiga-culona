import asyncio
import os
import dotenv
from agent_framework import Agent

# 1. Swap FoundryChatClient for the standard OpenAI wrapper
from agent_framework_openai import OpenAIChatClient 

dotenv.load_dotenv()


def _openai_base_url() -> str:
    endpoint = (os.getenv("FOUNDRY_PROJECT_ENDPOINT") or "").rstrip("/")
    if endpoint.endswith("/openai/v1"):
        return endpoint
    return f"{endpoint}/openai/v1"


assert _openai_base_url().endswith("/openai/v1")


async def main():
    agent = Agent(
        client=OpenAIChatClient(
            model=os.getenv("FOUNDRY_MODEL_DEPLOYMENT_NAME"),
            api_key=os.getenv("AZURE_AI_FOUNDRY_API_KEY"),
            base_url=_openai_base_url(),
        ),
        name="HelpfulAgent",
        instructions="You are a precise, helpful assistant."
    )

    response = await agent.run("What is the capital of France?")
    print(response)

if __name__ == "__main__":
    asyncio.run(main())