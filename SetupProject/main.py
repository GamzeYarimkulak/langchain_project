from dotenv import load_dotenv,dotenv_values

load_dotenv()


print(dotenv_values(".env").get("OPENAI_API_KEY"))
print(dotenv_values(".env"))

