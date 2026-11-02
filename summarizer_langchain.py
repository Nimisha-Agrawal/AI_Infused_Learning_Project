# import os
# from openai import OpenAI
# from dotenv import load_dotenv
# from scraper import fetch_website_contents

# load_dotenv()          # <-- this reads your .env file
# client = OpenAI(
#     api_key=os.getenv("GROQ_API_KEY"),
#     base_url="https://api.groq.com/openai/v1"
# )

# system_prompt = """You analyze the contents of a website and
# give a short, friendly summary. Ignore navigation menus.
# Respond in markdown."""

# def summarize(url):
#     website = fetch_website_contents(url)
#     response = client.chat.completions.create(
#         model="openai/gpt-oss-120b",
#         messages=[
#             {"role":"system", "content": system_prompt},
#             {"role":"user",   "content": f"Summarize this website:\n\n{website}"},
#         ],
#     )
#     return response.choices[0].message.content
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from scraper import fetch_website_contents   # reuse Class 1's scraper
load_dotenv()

prompt = ChatPromptTemplate.from_template(            # ①
    "Give a short, friendly summary of this website:\n\n{website}")

model  = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)   # ②

parser = StrOutputParser()                             # ③

chain = prompt | model | parser                        # ④

def summarize(url):
    return chain.invoke({"website": fetch_website_contents(url)})   # ⑤

print(summarize("https://anthropic.com"))

#agent = LLM + tool + loop