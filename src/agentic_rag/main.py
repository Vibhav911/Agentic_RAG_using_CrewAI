import warnings

from src.agentic_rag.crew import AgenticRag


warnings.filterwarnings("ignore", category=SyntaxWarning, module = "pysbd")

def run():
    "Run the Crew"
    print("\n" + '='*25)
    print("Starting Crew AI RAG Systems")
    print("="*25)

    query = "Who is Elon Musk ? What is his worth ?"
    print(f"\n Processing query: '{query}'")
    print("-"*25)

    inputs = {
        'query': query
    }

    try:
        print("\n Initializing Crew and executing query")
        result = AgenticRag().crew().kickoff(inputs=inputs)


        print("\n Results:")
        print(result)
        print("Execution completed successfully")

        return result


    except Exception as e:
        print(f"An error occurred while running the crew: {e}")
        raise



if __name__ == "__main__":
    run()