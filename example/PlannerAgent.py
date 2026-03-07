from agent import PlanAndSolveAgent, HelloAgentsLLM
from dotenv import load_dotenv
import os

def main():
    load_dotenv()  # 加载环境变量
    # 初始化LLM客户端
    llm_client = HelloAgentsLLM(
        apiKey=os.getenv("API_KEY"), baseUrl=os.getenv("BASE_URL"), model="kimi-k2.5", timeout=1000
    )
    # 创建PlanAndSolveAgent实例
    agent = PlanAndSolveAgent(llm_client)
    # 定义一个复杂的问题
    question = "请帮我制定一个计划，告诉我如何在一周内学习Python编程，并且每天需要完成哪些具体的任务。"
    # 运行智能体
    agent.run(question)

if __name__ == "__main__":
    main()
