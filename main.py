import sys
from crewai import Crew, Process
from agents import HealthAdvisorAgent
from tasks import read_and_summarize_task, find_articles_task, provide_recommendations_task
from pdf_reader import text_from_pdf

def main(pdf_path):
    try:
        print("Starting Crew...")
       
        agents = HealthAdvisorAgent()
        Analyzer= agents.Analyzer_agent()
        Researcher = agents.researcher_agent()
        Recommender = agents.recommender_agent()
      
        crew = Crew(
            agents=[Analyzer, Researcher, Recommender],
            tasks=[read_and_summarize_task, find_articles_task, provide_recommendations_task],
            process=Process.sequential,  
            memory=True,  
            cache=True,  
            max_rpm=100,  
            share_crew=True,  
        )

       
        report_data = text_from_pdf(pdf_path)

        print("Starting Crew kickoff...")
        result = crew.kickoff(inputs={'report_data': report_data})
        print('\n\n\nFinal verdict: \n', result, '\n\n\n')

    except FileNotFoundError:
        print(f"File not found: {pdf_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
    else:
        pdf_path = r'D:/crewai-health-advisor/report.pdf'
    main(pdf_path)
