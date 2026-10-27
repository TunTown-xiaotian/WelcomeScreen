from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "你是一个只说重点的助手"},
        {"role": "user", "content": "用一句话解释什么是向量数据库"},
    ],
    temperature=0.2,
    max_tokens=200,
)

print(resp.choices[0].message.content)