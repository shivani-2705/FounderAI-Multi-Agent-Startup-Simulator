from app.agents.ceo import CEOAgent
from app.agents.cto import CTOAgent
from app.agents.pm import PMAgent
from app.workflows.state import StartupState
from app.memory.events import (
    AgentEvent,
    EventType,
)
from app.agents.contracts import ReviewDecision


class StartupWorkflow:
    """
    Orchestrates all startup agents.

    Currently:
        Idea -> CEO

    Future:
        Idea -> CEO -> CTO -> PM -> Marketing -> Investor
    """

    def __init__(self):
        self.ceo = CEOAgent()
        self.cto = CTOAgent()
        self.pm = PMAgent()

    def run(self, idea: str) -> StartupState:

        state = StartupState(
            idea=idea,
        )

        state.ceo_analysis = self.ceo.generate(
            state.idea,
        )

        state.history.add(
            AgentEvent(
                agent="CEO",
                event_type=EventType.ANALYSIS,
                content=state.ceo_analysis.model_dump_json(
                    indent=2
                ),
            )
        )

        state.technical_architecture = self.cto.generate(
            state.ceo_analysis,
        )

       

        state.history.add(
            AgentEvent(
                agent="CTO",
                event_type=EventType.ANALYSIS,
                content=state.technical_architecture.model_dump_json(
                    indent=2
                ),
            )
        )

        review = self.cto.review(
            state.technical_architecture,
        )

        if review.decision == ReviewDecision.REVISION_REQUIRED:



         state.history.add(
            AgentEvent(
                agent="CTO",
                event_type=EventType.REVIEW,
                content=review.model_dump_json(indent=2),
            )
        )


        state.ceo_analysis = self.ceo.revise(
            state.ceo_analysis,
            review.feedback,
        )

        state.history.add(
            AgentEvent(
                agent="CEO",
                event_type=EventType.REVISION,
                content=state.ceo_analysis.model_dump_json(indent=2),
            )
        )


        state.prd = self.pm.generate(
            state.ceo_analysis,
            state.technical_architecture,
        )

        

        state.history.add(
            AgentEvent(
                agent="PM",
                event_type=EventType.ANALYSIS,
                content=state.prd.model_dump_json(
                    indent=2
                ),
            )
        )

        return state

startup_workflow = StartupWorkflow()