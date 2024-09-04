from crewai import Task
from agents import HealthAdvisorAgent
from tools import web_search_tool

agents = HealthAdvisorAgent()
Analyzer= agents.Analyzer_agent()
Researcher = agents.researcher_agent()
Recommender = agents.recommender_agent()


read_and_summarize_task = Task(
    description="Extract relevant data from the provided blood test report and summarize it.",
    expected_output="A simplified summary of the blood test results.",
    tools=[],
    agent=Analyzer,
    async_execution=False,
    output_file='report_summary.txt'
)


find_articles_task = Task(
    description="Search for health-related articles based on the summarized blood test report findings.",
    expected_output="A list of URLs to relevant health articles.",
    tools=[web_search_tool],
    agent=Researcher,
    async_execution=False,
    output_file='articles_urls.txt'
)


provide_recommendations_task = Task(
    description="Read the relevant articles and provide health recommendations based on their content.",
    expected_output="A list of health recommendations",
    tools=[web_search_tool],
    agent=Recommender,
    async_execution=False,
    output_file='recommendations.txt'
)
