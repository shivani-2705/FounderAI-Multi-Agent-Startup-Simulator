# from app.agents.ceo import CEOAgent
# from app.agents.cto import CTOAgent
# from app.agents.pm import PMAgent

# idea = """
# Build an AI-powered travel planner
# for college students.
# """

# ceo = CEOAgent()
# cto = CTOAgent()
# pm = PMAgent()

# ceo_analysis = ceo.generate(idea)

# architecture = cto.generate(
#     ceo_analysis
# )

# prd = pm.generate(
#     ceo_analysis,
#     architecture,
# )

# print(prd.model_dump_json(indent=4))


# from app.agents.ceo import CEOAgent
# from app.agents.cto import CTOAgent
# from app.agents.pm import PMAgent
# from app.agents.designer import DesignerAgent
# from app.agents.marketing import MarketingAgent

# from app.memory.events import EventHistory

# idea = """
# Build an AI-powered travel planner
# for college students.
# """

# history = EventHistory()

# ceo = CEOAgent()
# cto = CTOAgent()
# pm = PMAgent()
# designer = DesignerAgent()
# marketing = MarketingAgent()

# # CEO
# ceo_analysis = ceo.generate(
#     idea,
#     history,
# )

# # CTO
# architecture = cto.generate(
#     ceo_analysis,
#     history,
# )

# # PM
# prd = pm.generate(
#     ceo_analysis,
#     architecture,
#     history,
# )

# # Designer
# design = designer.generate(
#     ceo_analysis,
#     architecture,
#     prd,
#     history,
# )

# # Marketing
# marketing_strategy = marketing.generate(
#     ceo_analysis,
#     prd,
#     design,
#     history,
# )

# print(marketing_strategy.model_dump_json(indent=4))



from app.agents.ceo import CEOAgent
from app.agents.cto import CTOAgent
from app.agents.pm import PMAgent
from app.agents.designer import DesignAgent
from app.agents.marketing import MarketingAgent
from app.agents.investor import InvestorAgent

from app.memory.events import EventHistory

idea = """
Build an AI-powered travel planner
for college students.
"""

history = EventHistory()

ceo = CEOAgent()
cto = CTOAgent()
pm = PMAgent()
design = DesignAgent()
marketing = MarketingAgent()
investor = InvestorAgent()

ceo_analysis = ceo.generate(idea)

architecture = cto.generate(
    ceo_analysis,
)

prd = pm.generate(
    ceo_analysis,
    architecture,
)

design_doc = design.generate(
    ceo_analysis,
    prd,
    history,
)

marketing_doc = marketing.generate(
    ceo_analysis,
    prd,
    design_doc,
    history,
)

investment = investor.generate(
    ceo_analysis,
    architecture,
    prd,
    design_doc,
    marketing_doc,
    history,
)

print(investment.model_dump_json(indent=4))