1 *Agents*
    - Three agents  `Analyzer`, `Researcher`, and `recommender`.
    - Agent is assigned a specific role, goal, and backstory, and is powered by the `ChatGroq` language model.
    - The agents can perform tasks sequentially, retaining memory and context across tasks.

2 *Tasks*:
    - Tasks are defined in the `tasks.py` file and include:
     
3 *PDF Text Extraction*:
    Extract text from PDf


 Installation

1 Clone the Repo
   Using Git clone
   

 Install all the dependency
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    ```

 Set Up Environment Variables:
    - Create a `.env` file in the root directory of the project.
    - Add your API keys
      GROQ_API_KEY=your_groq_api_key
      SERPER_API_KEY=your_serper_api_key

 Run Your main.py file

    - The script will print the results, including the summary of the blood test report, relevant articles, and health recommendations. It will also save the outputs to specified files (report_summary.txt`, `articles_urls.txt`, `recommendations.txt`).
