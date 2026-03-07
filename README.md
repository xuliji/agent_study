# Agent 学习项目

这是一个用于学习 Agent（智能体）开发的示例项目，包含两种主流智能体架构的实现。

## 架构概览

### ReAct 架构
推理-行动循环模式，每一步都进行思考、选择行动、观察结果。

```
用户问题 → [思考 → 行动 → 观察] 循环 → 最终答案
```

**特点**：
- 逐步推理，灵活应对
- 支持工具调用
- 适合需要动态决策的任务

### Plan & Solve 架构
先制定完整计划，再按步骤执行。

```
用户问题 → 生成计划 → 按步骤执行 → 最终答案
```

**特点**：
- 全局规划，结构清晰
- 分步执行，易于理解
- 适合结构化任务

## 项目结构

```
agent-study/
├── agent/                          # Agent 核心模块
│   ├── ReActAgent.py              # ReAct 智能体实现
│   ├── PlanAndSolveAgent.py       # Plan & Solve 智能体实现
│   ├── Planner.py                 # 计划生成器
│   ├── Executor.py                # 计划执行器
│   ├── HelloAgentsLLM.py          # LLM 客户端（流式响应）
│   ├── OpenAICompatibleClient.py  # OpenAI 兼容 API 客户端
│   └── autogen/                   # AutoGen 工具
├── tools/                          # 工具函数
│   ├── weather_tools.py           # 天气查询工具
│   ├── place_tools.py             # 旅游景点推荐工具
│   ├── search_tools.py            # 网页搜索工具
│   └── ToolExecutor.py            # 工具执行器
├── example/                        # 示例代码
│   ├── travel_assistant.py        # 旅行助手示例
│   ├── ReAct.py                   # ReAct 智能体示例
│   └── PlannerAgent.py            # Plan & Solve 智能体示例
├── .env                           # 环境变量配置
├── pyproject.toml                 # 项目配置
└── requirements.txt               # 依赖列表
```

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

或手动安装核心依赖：

```bash
pip install openai python-dotenv requests tavily-python google-search-results
```

### 2. 配置环境变量

创建 `.env` 文件并配置以下环境变量：

```env
# LLM 配置
API_KEY="your-api-key"
BASE_URL="https://your-endpoint/v1"
LLM_MODEL_ID="your-model-id"
LLM_TIMEOUT=60

# 工具 API Keys
TAVILY_API_KEY="your-tavily-api-key"
SENIVERSE_API_KEY="your-seniverse-api-key"
SERPAPI_API_KEY="your-serpapi-api-key"
```

### 3. 运行示例

```bash
# ReAct 智能体示例
python -m example.ReAct

# Plan & Solve 智能体示例
python -m example.PlannerAgent

# 旅行助手示例
python -m example.travel_assistant
```

## 核心组件

### LLM 客户端

#### HelloAgentsLLM
为 Agent 定制的 LLM 客户端，支持流式响应。

```python
from agent import HelloAgentsLLM

llm_client = HelloAgentsLLM(
    apiKey=os.getenv("API_KEY"),
    baseUrl=os.getenv("BASE_URL"),
    model="your-model"
)

response = llm_client.think(messages=[{"role": "user", "content": "你好"}])
```

#### OpenAICompatibleClient
支持任意兼容 OpenAI API 的 LLM 服务。

### 智能体

#### ReActAgent
基于 ReAct 架构的智能体实现，支持工具调用。

```python
from agent import ReActAgent, HelloAgentsLLM
from tools import ToolExecutor

llm_client = HelloAgentsLLM()
tool_executor = ToolExecutor()
tool_executor.registerTool("Search", "搜索工具", search_function)

agent = ReActAgent(llm_client, tool_executor, max_steps=5)
result = agent.run("今天北京天气怎么样？")
```

#### PlanAndSolveAgent
基于 Plan & Solve 架构的智能体。

```python
from agent import PlanAndSolveAgent, HelloAgentsLLM

llm_client = HelloAgentsLLM()
agent = PlanAndSolveAgent(llm_client)

result = agent.run("帮我制定一周学习 Python 的计划")
```

### 工具系统

#### ToolExecutor
工具注册与执行管理器。

```python
from tools import ToolExecutor, search

executor = ToolExecutor()
executor.registerTool("Search", "网页搜索引擎", search)

# 获取工具
tool_func = executor.getTool("Search")
result = tool_func("Python 教程")

# 获取所有工具描述
tools_desc = executor.getAvailableTools()
```

#### 内置工具

| 工具 | 功能 | 依赖 |
|------|------|------|
| `get_weather` | 查询指定城市天气 | Seniverse API |
| `get_attraction` | 根据天气推荐旅游景点 | Tavily API |
| `search` | 网页搜索 | SerpApi |

## 示例说明

### 1. ReAct 智能体示例

演示如何使用 ReAct 智能体进行实时信息查询：

```bash
python -m example.ReAct
```

特点：
- 自动调用搜索工具
- 推理-行动循环
- 动态决策

### 2. Plan & Solve 智能体示例

演示如何使用 Plan & Solve 智能体制定学习计划：

```bash
python -m example.PlannerAgent
```

特点：
- 先生成完整计划
- 按步骤执行
- 结构化输出

### 3. 旅行助手示例

演示如何使用工具进行旅行规划：

```bash
python -m example.travel_assistant
```

功能：
- 查询城市天气
- 根据天气推荐景点

## 学习路径

建议按以下顺序学习：

### 第一步：理解 LLM 客户端
- 阅读 `agent/HelloAgentsLLM.py`
- 理解如何调用 LLM API
- 掌握流式响应处理

### 第二步：学习工具系统
- 阅读 `tools/ToolExecutor.py`
- 了解工具注册机制
- 实现自己的工具

### 第三步：实践 ReAct 架构
- 阅读 `agent/ReActAgent.py`
- 理解思考-行动循环
- 运行 `example/ReAct.py`

### 第四步：实践 Plan & Solve 架构
- 阅读 `agent/Planner.py` 和 `agent/Executor.py`
- 理解计划生成和执行
- 运行 `example/PlannerAgent.py`

### 第五步：对比两种架构
- 分析不同场景下的表现
- 选择合适的架构

## 架构对比

| 维度 | ReAct | Plan & Solve |
|------|-------|--------------|
| **决策方式** | 动态推理 | 预先规划 |
| **执行流程** | 循环式 | 线性式 |
| **灵活性** | 高（可随时调整） | 中（计划相对固定） |
| **可解释性** | 中 | 高（计划清晰） |
| **适用场景** | 需要动态决策的任务 | 结构化任务 |
| **工具依赖** | 强 | 弱 |
| **示例** | 实时搜索、问答 | 制定计划、分步指导 |

**选择建议**：
- 需要**实时信息**或**多次工具调用** → **ReAct**
- 需要**结构化输出**或**清晰步骤** → **Plan & Solve**

## 核心概念

### ReAct 循环

```
Thought: 分析问题，规划下一步
Action: 选择工具并执行
Observation: 观察执行结果
[重复直到得出最终答案]
```

### Plan & Solve 流程

```
1. Planner: 分析问题，生成步骤列表
2. Executor: 按步骤依次执行
   - 传递历史上下文
   - 执行当前步骤
   - 记录结果
3. 输出最终答案
```

## 扩展开发

### 添加新工具

1. 在 `tools/` 目录创建新工具文件
2. 实现工具函数
3. 在 `tools/__init__.py` 中导入
4. 使用 `ToolExecutor` 注册

示例：

```python
# tools/my_tool.py
def my_custom_tool(query: str) -> str:
    """我的自定义工具"""
    # 实现逻辑
    return "结果"
```

### 创建新智能体

1. 在 `agent/` 目录创建新文件
2. 继承或参考现有架构
3. 实现核心逻辑
4. 在 `agent/__init__.py` 中导出

## 常见问题

### Q: 如何选择合适的智能体架构？

**A**: 
- 需要多次查询、动态调整 → ReAct
- 任务结构清晰、步骤明确 → Plan & Solve

### Q: 如何添加新的工具？

**A**: 参考现有工具实现，使用 ToolExecutor 注册即可。

### Q: LLM 响应很慢怎么办？

**A**: 
- 检查网络连接
- 调整 timeout 参数
- 考虑使用更快的模型

## 贡献指南

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License
