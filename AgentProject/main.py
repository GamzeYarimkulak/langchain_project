from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
#from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain import hub
from langchain.agents import create_react_agent,AgentExecutor

load_dotenv()
model = ChatOpenAI(model = "gpt-4")
memory = SqliteSaver.from_conn_string(":memory:")
search = TavilySearchResults(max_results=2)

prompt = hub.pull("lc://agents/react")


tools =[search]

agent = create_react_agent(model, tools,prompt)
agent_executor=AgentExecutor(agent=agent,tools=tools,verbose=True ,checkpoint=memory)

config ={"configurable":{"thread_id":"abc123"}}

if __name__ == '__main__':
    chat_history =[]
    while True:
        user_input=input("> ")
        response=[]
        for chunk in agent_executor.stream(
            {"input":user_input,
             "chat_history":"\n".join(chat_history)
             },
            config =config

        ):
            if 'text' in chunk:
                print(chunk['text'],end="")
                response.append(chunk['text'])

            chat_history.append(f"AI: {''.join(response)}")


