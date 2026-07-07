from app.agents.ceo import CEOAgent

ceo = CEOAgent()

analysis = ceo.generate(
    """
Build an AI travel planner
for college students.
"""
)

print(analysis.model_dump_json(indent=4))