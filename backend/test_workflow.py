from app.workflows.startup_workflow import startup_workflow

idea = """
Build an AI-powered travel planner
for college students.
"""

result = startup_workflow.run(idea)

print(result.model_dump_json(indent=4))