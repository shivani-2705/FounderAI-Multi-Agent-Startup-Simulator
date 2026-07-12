import type { HistoryEvent } from "../types/project";

interface Props {
    event: HistoryEvent;
}

function getIcon(type: HistoryEvent["event_type"]) {
    switch (type) {
        case "analysis":
            return "🧠";

        case "review":
            return "🔍";

        case "revision":
            return "✏️";

        case "decision":
            return "✅";

        case "question":
            return "❓";

        case "answer":
            return "💬";

        default:
            return "•";
    }
}

function formatTime(timestamp: string) {
    return new Date(timestamp).toLocaleString();
}

export default function TimelineItem({
    event,
}: Props) {
    return (
        <div className="timeline-item">

            <div className="timeline-header">

                <span className="timeline-icon">
                    {getIcon(event.event_type)}
                </span>

                <strong>
                    {event.agent}
                </strong>

                <span className="timeline-time">
                    {formatTime(event.timestamp)}
                </span>

            </div>

            <div className="timeline-message">
                {event.content}
            </div>

        </div>
    );
}