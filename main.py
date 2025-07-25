import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from Roadmap_tool import get_career_roadmap

# ✅ Load API key
load_dotenv()
client = AsyncOpenAI(
    api_key = os.getenv("GEMINI_API_KEY"),
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)
model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client)
config = RunConfig(model=model, tracing_disabled=True)

career_agent = Agent(
    name="CareerAgent",
    instructions="You ask about intrests and suggest a career path based on that",
    model=model
)
skill_agent = Agent(
    name="SkillAgent",
    instructions="You share the roadmap using the get_career_roadmap tool",
    model=model,
    tools=[get_career_roadmap]
)
job_agent = Agent(
    name="JobAgent",
    instructions="You suggest job titles in the chosen career field",
    model=model
)

def main():
    print("\U0001F393 career mentor agent\n")
    intrests = input("🎓 What are your intrests? ->")

    result1= Runner.run_sync(career_agent, intrests, run_config=config)
    field = result1.final_output.strip()
    print("\n✅ Suggested Career:", field)

    result2 = Runner.run_sync(skill_agent, field, run_config=config)
    print("\n🛠️ Required Skills:", result2.final_output)

    result3= Runner.run_sync(job_agent, field, run_config=config)
    print("\n💼 Possible Jobs:", result3.final_output)

if __name__ == "__main__":
    main()
