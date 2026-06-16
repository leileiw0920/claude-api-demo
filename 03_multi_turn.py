"""
示例 3：多轮对话
API 是无状态的，需要每次带上完整的历史消息
"""
from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic()

SYSTEM_PROMPT = "你是一个友好的中文编程助手，回答简洁但准确。"

history = []

print("多轮对话示例（输入 'quit' 退出）\n")

while True:
    user_input = input("你: ").strip()
    if user_input.lower() in ("quit", "exit", "退出"):
        print("再见！")
        break
    if not user_input:
        continue

    history.append({"role": "user", "content": user_input})

    response = client.messages.create(
        model="glm-5.1",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=history
    )

    assistant_reply = response.content[0].text
    print(f"\n助手: {assistant_reply}\n")

    history.append({"role": "assistant", "content": assistant_reply})
