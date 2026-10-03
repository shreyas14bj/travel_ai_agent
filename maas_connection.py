from langchain_openai import ChatOpenAI
import os
import httpx
client = httpx.Client(verify=False)
llm = ChatOpenAI(
   base_url="https://genailab.tcs.in", # set openai_api_base to the LiteLLMProxy
   model = "genailab-maas-sonnet-4.6",
   api_key="sk-Uih1gGn8pKph0HNrr-uwxQ",
   http_client = client
)

response = llm.invoke("Hi")
print(response.content)