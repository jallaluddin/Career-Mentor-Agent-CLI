# Roadmap_tool.py
from agents import function_tool

@function_tool
def get_career_roadmap(field: str) -> str:
    maps = {
        "software engineer": "learn Python, DSA, Web Development, and cloud computing.",
        "data scientist": "master python, pandas, ML and real-world datasets.",
        "AI engineer": "learn Python, ML, LLMs, and AI frameworks.",
        "cybersecurity engineer": "master Python, Networking, and security protocols"
    }
    return maps.get(field, "No roadmap found for that field.")