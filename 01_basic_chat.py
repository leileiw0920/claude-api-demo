"""
示例 1：基础单次对话
演示最简单的 API 调用方式
"""
from dotenv import load_dotenv
import anthropic

load_dotenv()

# SDK 自动读取环境变量 ANTHROPIC_API_KEY 和 ANTHROPIC_BASE_URL
client = anthropic.Anthropic()

response = client.messages.create(
    model="glm-5.1",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "你好！请用中文自我介绍一下，50字以内。"}
    ]
)

for block in response.content:
    if block.type == "text":
        print(block.text)

print(f"\n--- 用量统计 ---")
print(f"输入 tokens: {response.usage.input_tokens}")
print(f"输出 tokens: {response.usage.output_tokens}")
print(f"停止原因: {response.stop_reason}")
