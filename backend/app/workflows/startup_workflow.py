from app.agents.ceo import CEOAgent
from app.agents.cto import CTOAgent
from app.agents.pm import PMAgent
from app.agents.designer import DesignerAgent
from app.agents.marketing import MarketingAgent
from app.agents.investor import InvestorAgent

from app.workflows.state import StartupState

from app.memory.events import (
    AgentEvent,
    EventType,
)

from app.agents.contracts import (
    AgentReview,
)


class StartupWorkflow:

    def __init__(self):
        self.ceo = CEOAgent()
        self.cto = CTOAgent()
        self.pm = PMAgent()
        self.designer = DesignerAgent()
        self.marketing = MarketingAgent()
        self.investor = InvestorAgent()

    # --------------------------------------------------------
    # CEO
    # --------------------------------------------------------

    def run_ceo(
        self,
        state: StartupState,
    ) -> StartupState:

        state.ceo_analysis = self.ceo.generate(
            state.idea,
            state.history,
        )

        state.history.add(
            AgentEvent(
                agent="CEO",
                event_type=EventType.ANALYSIS,
                content=state.ceo_analysis.model_dump_json(
                    indent=2,
                ),
            )
        )

        return state

    def revise_ceo(
        self,
        state: StartupState,
        feedback: str,
    ) -> StartupState:

        state.ceo_analysis = self.ceo.revise(
            state.ceo_analysis,
            feedback,
        )

        state.history.add(
            AgentEvent(
                agent="CEO",
                event_type=EventType.REVISION,
                content=state.ceo_analysis.model_dump_json(
                    indent=2,
                ),
            )
        )

        return state

    # --------------------------------------------------------
    # CTO
    # --------------------------------------------------------

    def run_cto(
        self,
        state: StartupState,
    ) -> StartupState:

        state.technical_architecture = self.cto.generate(
            state.ceo_analysis,
            state.history,
        )

        state.history.add(
            AgentEvent(
                agent="CTO",
                event_type=EventType.ANALYSIS,
                content=state.technical_architecture.model_dump_json(
                    indent=2,
                ),
            )
        )

        return state

    def review_cto(
        self,
        state: StartupState,
    ) -> AgentReview:

        review = self.cto.review(
            state.technical_architecture,
        )

        state.history.add(
            AgentEvent(
                agent="CTO",
                event_type=EventType.REVIEW,
                content=review.model_dump_json(
                    indent=2,
                ),
            )
        )

        return review

    def revise_cto(
        self,
        state: StartupState,
        feedback: str,
    ) -> StartupState:

        state.technical_architecture = self.cto.revise(
            state.technical_architecture,
            feedback,
        )

        state.history.add(
            AgentEvent(
                agent="CTO",
                event_type=EventType.REVISION,
                content=state.technical_architecture.model_dump_json(
                    indent=2,
                ),
            )
        )

        return state

    # --------------------------------------------------------
    # PM
    # --------------------------------------------------------

    def run_pm(
        self,
        state: StartupState,
    ) -> StartupState:

        state.prd = self.pm.generate(
            state.ceo_analysis,
            state.technical_architecture,
            state.history,
        )

        state.history.add(
            AgentEvent(
                agent="PM",
                event_type=EventType.ANALYSIS,
                content=state.prd.model_dump_json(
                    indent=2,
                ),
            )
        )

        return state

    def review_pm(
        self,
        state: StartupState,
    ) -> AgentReview:

        review = self.pm.review(
            state.technical_architecture,
        )

        state.history.add(
            AgentEvent(
                agent="PM",
                event_type=EventType.REVIEW,
                content=review.model_dump_json(
                    indent=2,
                ),
            )
        )

        return review

    # --------------------------------------------------------
    # Designer
    # --------------------------------------------------------

    def run_designer(
        self,
        state: StartupState,
    ) -> StartupState:

        state.design = self.designer.generate(
            state.ceo_analysis,
            state.technical_architecture,
            state.prd,
            state.history,
        )

        state.history.add(
            AgentEvent(
                agent="Designer",
                event_type=EventType.ANALYSIS,
                content=state.design.model_dump_json(
                    indent=2,
                ),
            )
        )

        return state
    # --------------------------------------------------------
    # Marketing
    # --------------------------------------------------------

    def run_marketing(
        self,
        state: StartupState,
    ) -> StartupState:

        state.marketing = self.marketing.generate(
            state.ceo_analysis,
            state.prd,
            state.design,
            state.history,
        )

        state.history.add(
            AgentEvent(
                agent="Marketing",
                event_type=EventType.ANALYSIS,
                content=state.marketing.model_dump_json(
                    indent=2,
                ),
            )
        )

        return state
    # --------------------------------------------------------
    # Investing
    # --------------------------------------------------------

    def run_investor(
        self,
        state: StartupState,
    ) -> StartupState:

        state.investment = self.investor.generate(
            state.ceo_analysis,
            state.technical_architecture,
            state.prd,
            state.design,
            state.marketing,
            state.history,
        )

        state.history.add(
            AgentEvent(
                agent="Investor",
                event_type=EventType.ANALYSIS,
                content=state.investment.model_dump_json(
                    indent=2,
                ),
            )
        )

        return state


startup_workflow = StartupWorkflow()