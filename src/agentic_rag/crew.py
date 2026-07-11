from crewai import Agent, Task, Process, Crew
from crewai.project import CrewBase, agent, task, crew
from crewai_tools import SerperDevTool
from agentic_rag.tools.custom_tool import DocumentSearchTool
import os
from dotenv import load_dotenv

# Initializing the tool with specific pdf path for exclusive search within 
load_dotenv()
os.environ['SERPER_API_KEY'] = os.getenv("SERPER_API_KEY")
os.environ["OPENAI_API_KEY"] = os.environ("SERPER_API_KEY")

pdf_tool = DocumentSearchTool(file_path="knowledge/dspy.pdf")
web_search_tool = SerperDevTool()


@CrewBase
class AgenticRag():
    "Agentic Rag Crew"

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"


    @agent
    def retriever_agent(self) -> Agent:
        return Agent(
            config = self.agents_config['retriever_agent'],
            verbose = True,
            tools = [pdf_tool, web_search_tool]
        )

    @agent
    def response_synthesizer_agent(self) -> Agent:
        return Agent(
            config = self.agents_config['response_synthesizer_agent'],
            verbose = True,
        )


    @task
    def retrieval_task(self) -> Task:
        return Task(
            config = self.tasks_config['retrieval_task']
        )

    def response_task(self) -> Task:
        return Task(
            config=self.tasks_config['response_task']
        )


    @crew
    def crew(self) -> Crew:
        "Create the Agentic Rag"
        return Crew(
            agents = self.agents,   # Automatically created by @agent decorator
            tasks = self.tasks,   # Automatically created by @task decorator
            process = Process.sequential,
            verbose = True
        )