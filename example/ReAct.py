from dotenv import load_dotenv
import os
from agent import ReActAgent, HelloAgentsLLM
from tools import ToolExecutor, search

def main():
    load_dotenv()  # 加载环境变量
    HelloAgentsLLMClient = HelloAgentsLLM()
    toolExecutor = ToolExecutor()
    # 2. 注册我们的实战搜索工具
    search_description = "一个网页搜索引擎。当你需要回答关于时事、事实以及在你的知识库中找不到的信息时，应使用此工具。"
    toolExecutor.registerTool("Search", search_description, search)
    llmClient = ReActAgent(HelloAgentsLLMClient, toolExecutor, 100)
    llmClient.run("请帮我搜索一下，英伟达最新的GPU型号是什么？")

if __name__ == '__main__':
    main()