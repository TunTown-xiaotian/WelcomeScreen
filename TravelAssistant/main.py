
import re

from TravelAssistant.OpenAICompatibleClient import OpenAICompatibleClient
from TravelAssistant.available_tools import available_tools
from TravelAssistant.system_prompt import AGENT_SYSTEM_PROMPT




# main.py 中的修改
client = OpenAICompatibleClient(
    model="deepseek-flash", # 免费模型
    api_key="",
    base_url="https://api.deepseek.com"
)

# --- 2. 初始化 ---
user_prompt = "你好，请帮我查询一下今天成都的天气，然后根据天气推荐一个合适的旅游景点。"
prompt_history = [f"用户请求: {user_prompt}"]

print(f"用户输入: {user_prompt}\n" + "=" * 40)

# --- 3. 运行主循环 ---
for i in range(3):  # 设置最大循环次数
    print(f"--- 循环 {i + 1} ---\n")

    # 3.1. 构建Prompt
    full_prompt = "\n".join(prompt_history)

    # 3.2. 调用LLM进行思考
    llm_output =client.generate(full_prompt, system_prompt=AGENT_SYSTEM_PROMPT)
    # 模型可能会输出多余的Thought-Action，需要截断
    match = re.search(r'(Thought:.*?Action:.*?)(?=\n\s*(?:Thought:|Action:|Observation:)|\Z)', llm_output, re.DOTALL)
    if match:
        truncated = match.group(1).strip()
        if truncated != llm_output.strip():
            llm_output = truncated
            print("已截断多余的 Thought-Action 对")
    print(f"模型输出:\n{llm_output}\n")
    prompt_history.append(llm_output)

    # 3.3. 解析并执行行动
    action_match = re.search(r"Action: (.*)", llm_output, re.DOTALL)
    if not action_match:
        observation = "错误: 未能解析到 Action 字段。请确保你的回复严格遵循 'Thought: ... Action: ...' 的格式。"
        observation_str = f"Observation: {observation}"
        print(f"{observation_str}\n" + "=" * 40)
        prompt_history.append(observation_str)
        continue
    action_str = action_match.group(1).strip()

    if action_str.startswith("Finish"):
        m = re.match(r"Finish\[(.*)\]", action_str, re.DOTALL)
        if m:
            final_answer = m.group(1)
        else:
            # 模型没按格式给答案，直接把它当答案，或者提示它重来
            final_answer = action_str[len("Finish"):].strip(" []") or "（模型没给出答案内容）"
        print(f"任务完成，最终答案: {final_answer}")
        break
    tool_match = re.search(r"(\w+)\(", action_str)
    args_match = re.search(r"\((.*)\)", action_str)

    if not tool_match or not args_match:
        observation = f"错误: Action 格式不正确，无法解析工具调用: {action_str}"
        observation_str = f"Observation: {observation}"
        print(f"{observation_str}\n" + "=" * 40)
        prompt_history.append(observation_str)
        continue
    tool_name = tool_match.group(1)
    args_str = args_match.group(1)

    # tool_name = re.search(r"(\w+)\(", action_str).group(1)
    # args_str = re.search(r"\((.*)\)", action_str).group(1)
    kwargs = dict(re.findall(r'(\w+)="([^"]*)"', args_str))

    # if tool_name in available_tools:
    #     print(f"调试: tool_name={tool_name}, type={type(available_tools[tool_name])}")
    #     observation = available_tools[tool_name](**kwargs)

    if tool_name in available_tools:
        observation = available_tools[tool_name](**kwargs)
    else:
        observation = f"错误:未定义的工具 '{tool_name}'"

    # 3.4. 记录观察结果
    observation_str = f"Observation: {observation}"
    print(f"{observation_str}\n" + "=" * 40)
    prompt_history.append(observation_str)
