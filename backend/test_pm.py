from app.agents.ceo import CEOAgent
from app.agents.cto import CTOAgent
from app.agents.pm import PMAgent

idea = """
Build an AI-powered travel planner
for college students.
"""

ceo = CEOAgent()
cto = CTOAgent()
pm = PMAgent()

ceo_analysis = ceo.generate(idea)

architecture = cto.generate(
    ceo_analysis
)

prd = pm.generate(
    ceo_analysis,
    architecture,
)

print(prd.model_dump_json(indent=4))