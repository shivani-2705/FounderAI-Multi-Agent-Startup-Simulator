from app.agents.ceo import CEOAgent
from app.agents.cto import CTOAgent

idea = """
Build an AI-powered travel planner
for college students.
"""

ceo = CEOAgent()
cto = CTOAgent()

ceo_analysis = ceo.generate(idea)

architecture = cto.generate(
    ceo_analysis
)

print(architecture.model_dump_json(indent=4))