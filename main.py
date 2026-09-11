from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from prompt import SYSTEM_CHEF_PROMPT,CHEF_PROMPT
from langchain.messages import HumanMessage
from tools import web_search
from photo_decoder import choose_image_file,build_image_message
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


load_dotenv()

logging.info("creating our agent...")

model=init_chat_model(model="qwen/qwen3.6-27b",
                   model_provider="groq")

agent=create_agent(model=model,
                   system_prompt=SYSTEM_CHEF_PROMPT,
                   tools=[web_search])

logging.info("choosing our image...")

path=choose_image_file()

message=build_image_message(path,CHEF_PROMPT)

logging.info("invoking our agent...")

response=agent.invoke({
  "messages":[message]
})

print(response["messages"][-1].content)