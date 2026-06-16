"""
示例 2：流式输出（Streaming）
适合长回复场景，实时看到输出
"""
from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic()

print("正在回答（流式输出）：\n")

with client.messages.stream(
    model="glm-5.1",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "请解释一下什么是递归，并给一个 Python 示例。"}
    ]
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)

final_message = stream.get_final_message()
print(f"\n\n--- 用量统计 ---")
print(f"输入 tokens: {final_message.usage.input_tokens}")
print(f"输出 tokens: {final_message.usage.output_tokens}")
