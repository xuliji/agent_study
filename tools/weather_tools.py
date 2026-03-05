import requests

def get_weather(city: str) -> str:
    """
    通过调用 wttr.in API 查询真实的天气信息。
    city: 需要查询天气的城市名称 （例如 "Beijing" 或 "Shanghai"）不能使用中文，要使用中文拼音
    """
    # API端点，我们请求JSON格式的数据
    url = f"https://api.seniverse.com/v3/weather/daily.json?key=SmdXs9dF2fYlshvUi&location={city}&language=zh-Hans&unit=c&start=-1&days=5"
    
    try:
        # 发起网络请求
        response = requests.get(url)
        # 检查响应状态码是否为200 (成功)
        response.raise_for_status() 
        # 解析返回的JSON数据
        data = response.json()
        
        # 提取当前天气状况
        current_condition = data['results'][0]["daily"][0]
        weather_desc = current_condition['text_day']
        temp_h = current_condition['high']
        temp_l = current_condition['low']
        
        # 格式化成自然语言返回
        return f"{city}当前天气:{weather_desc}，气温{temp_l}-{temp_h}摄氏度"
        
    except requests.exceptions.RequestException as e:
        # 处理网络错误
        return f"错误:查询天气时遇到网络问题 - {e}"
    except (KeyError, IndexError) as e:
        # 处理数据解析错误
        return f"错误:解析天气数据失败，可能是城市名称无效 - {e}"
