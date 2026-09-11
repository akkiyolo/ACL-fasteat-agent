from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from prompt import SYSTEM_CHEF_PROMPT
from langchain.messages import HumanMessage

load_dotenv()

model=init_chat_model(model="qwen/qwen3.6-27b",
                   model_provider="groq")

agent=create_agent(model=model,
                   system_prompt=SYSTEM_CHEF_PROMPT)

response=agent.invoke({
  "messages":[HumanMessage(content="Hello, How are you ?")]
})

print(response["messages"][-1].content)