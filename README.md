# Agent 学习项目

这是一个用于学习 Agent（智能体）开发的示例项目。

## 项目结构

```
agent-study/
├── agent/              # Agent 核心模块
│   ├── OpenAICompatibleClient.py   # OpenAI 兼容 API 客户端
│   ├── HelloAgentsLLM.py            # LLM 客户端（流式响应）
│   └── ReActAgent.py                 # ReAct 智能体实现
├── tools/              # 工具函数
│   ├── weather_tools.py            # 天气查询工具
│   ├── place_tools.py              # 旅游景点推荐工具
│   ├── search_tools.py             # 网页搜索工具
│   └── ToolExecutor.py             # 工具执行器
├── example/            # 示例代码
│   ├── travel_assistant.py         # 旅行助手示例
│   └── ReAct.py                     # ReAct 智能体示例
├── .env               # 环境变量配置
└── pyproject.toml     # 项目配置
```

## 快速开始

1. 安装依赖：

```bash
pip install openai python-dotenv
```

2. 配置环境变量，编辑 `.env` 文件：

```env
API_KEY="your-api-key"
BASE_URL="https://your-endpoint/v1"
```

3. 运行示例：

```bash
python -m example.travel_assistant
```

## 功能介绍

- **OpenAICompatibleClient**: 支持任意兼容 OpenAI API 的 LLM 服务
- **HelloAgentsLLM**: 为 Agent 定制的 LLM 客户端，支持流式响应
- **ReActAgent**: 基于 ReAct 架构的智能体实现
- **ToolExecutor**: 工具执行器，管理工具注册和执行
- **get_weather**: 查询指定城市天气
- **get_attraction**: 根据天气推荐旅游景点
- **search**: 网页搜索工具

## 示例

### 旅行助手

运行后将启动一个交互式旅行助手，可以：
1. 查询城市天气
2. 根据天气推荐适合的旅游景点

```bash
python -m example.travel_assistant
```

### ReAct 智能体

运行后将启动一个基于 ReAct 架构的智能体，支持调用工具回答问题：

```bash
python -m example.ReAct
```
