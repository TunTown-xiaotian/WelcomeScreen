import requests

def get_weather(city: str) -> str:
    """
    通过调用 wttr.in API 查询真实的天气信息。
    """
    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        current_condition = data['current_condition'][0]
        weather_desc = current_condition['weatherDesc'][0]['value']
        temp_c = current_condition['temp_C']

        return f"{city}当前天气:{weather_desc}，气温{temp_c}摄氏度"

    except requests.exceptions.RequestException as e:
        return f"错误:查询天气时遇到网络问题 - {e}"
    except (KeyError, IndexError) as e:
        return f"错误:解析天气数据失败，可能是城市名称无效 - {e}"
import os
from tavily import TavilyClient

def get_attraction(city: str, weather: str) -> str:
    """
    根据城市和天气，使用 Tavily Search API 搜索并返回优化后的景点推荐。
    支持无 API Key 的 Keyless 测试模式。
    """
    # 1. 尝试获取 API 密钥，如果没有则为空字符串
    api_key = os.environ.get("TAVILY_API_KEY", "")

    # 2. 初始化 Tavily 客户端
    # 新版 tavily-python SDK 在 api_key 为空时会自动启用 keyless 模式
    try:
        if not api_key:
            tavily = TavilyClient(api_key="")   # 显式启用 Keyless 模式
        else:
            tavily = TavilyClient(api_key=api_key)
    except Exception as e:
        return f"初始化 Tavily 客户端失败: {e}"

    # 3. 构造查询
    query = f"'{city}' 在'{weather}'天气下最值得去的旅游景点推荐及理由"

    try:
        # 4. 调用 API，include_answer=True 会返回一个综合性的回答
        response = tavily.search(
            query=query,
            search_depth="basic",
            include_answer=True
        )

        # 5. 优先使用 Tavily 生成的综合性回答
        if response.get("answer"):
            return response["answer"]

        # 6. 如果没有综合性回答，则格式化原始结果
        formatted_results = []
        for result in response.get("results", []):
            formatted_results.append(f"- {result['title']}: {result['content']}")

        if not formatted_results:
            return "抱歉，没有找到相关的旅游景点推荐。"

        return "根据搜索，为您找到以下信息:\n" + "\n".join(formatted_results)

    except Exception as e:
        return f"错误:执行 Tavily 搜索时出现问题 - {e}"