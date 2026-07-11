from app.memory.events import EventHistory


class HistoryFormatter:

    def format(
        self,
        history: EventHistory,
    ) -> str:

        if not history.events:
            return "No previous history."

        sections = []

        for event in history.events:

            sections.append(
                f"""
Agent:
{event.agent}

Event:
{event.event_type.value}

Content:
{event.content}
"""
            )

        return "\n\n".join(sections)


history_formatter = HistoryFormatter()