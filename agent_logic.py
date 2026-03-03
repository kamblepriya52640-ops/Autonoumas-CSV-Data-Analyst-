import os
import warnings
import pandas as pd
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_experimental.agents import create_pandas_dataframe_agent
from dotenv import load_dotenv

# Suppress warnings and logging
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", module="tensorflow")
warnings.filterwarnings("ignore", module="langchain")

load_dotenv()

class MockPandasAgent:
    """
    Simulates a LangChain Pandas Agent for offline/demo use.
    """
    def __init__(self, df, chart_dir="charts"):
        self.df = df
        self.chart_dir = chart_dir

    def invoke(self, input_dict):
        query = input_dict.get("input", "").lower()
        print(f"> Entering new AgentExecutor chain (Mock)...")
        
        result = "Mock Agent: Query not recognized."
        
        if "rows" in query:
            result = len(self.df)
        elif "mean" in query and "revenue" in query:
            result = self.df['Revenue'].mean()
        elif "records" in query or "head" in query:
            result = self.df.head(5).to_string()
        elif "total sales" in query:
            result = self.df['Sales'].sum()
        elif "plot" in query:
            import matplotlib.pyplot as plt
            import os
            os.makedirs(self.chart_dir, exist_ok=True)
            plt.switch_backend('Agg')
            self.df.plot(x='Date', y='Sales', title="Sales Over Time")
            save_path = os.path.join(self.chart_dir, "sales_over_time.png")
            plt.savefig(save_path)
            print(f"Chart saved to {save_path}")
            result = save_path
            
        return {"output": str(result)}

def get_pandas_agent(df):
    """
    Initializes and returns a LangChain Pandas DataFrame Agent or a Mock Agent.
    """
    provider = os.getenv("AI_PROVIDER", "OLLAMA").upper()

    if provider == "MOCK":
        chart_dir = os.getenv("CHART_DIR", "charts")
        return MockPandasAgent(df, chart_dir=chart_dir)
    
    if provider == "OLLAMA":
        model = os.getenv("OLLAMA_MODEL", "llama3")
        llm = ChatOllama(model=model, temperature=0)
    else:
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    agent = create_pandas_dataframe_agent(
        llm,
        df,
        verbose=True,
        allow_dangerous_code=True
    )
    return agent
