import { useParams } from "react-router-dom";

import { useHistory } from "../hooks/useHistory";

function getIcon(type: string): string {
    switch (type) {
        case "analysis":
            return "🧠";

        case "review":
            return "🔍";

        case "revision":
            return "✏️";

        case "question":
            return "❓";

        case "answer":
            return "💬";

        case "decision":
            return "✅";

        default:
            return "📄";
    }
}

export default function HistoryPage() {
    const { projectId } = useParams();

    const history = useHistory(projectId ?? "");

    if (!history) {
        return <p>Loading...</p>;
    }

    if (history.events.length === 0) {
        return (
            <div className="container">
                <h1>Workflow Timeline</h1>

                <p>No history available.</p>
            </div>
        );
    }

    return (
        <div className="container">
            <h1>Workflow Timeline</h1>

            {history.events.map((event, index) => (
                <div
                    key={index}
                    className="timeline-item"
                >
                    <div className="timeline-header">
                        <span className="timeline-icon">
                            {getIcon(event.event_type)}
                        </span>

                        <strong>{event.agent}</strong>

                        {event.timestamp && (
                            <span className="timeline-time">
                                {new Date(
                                    event.timestamp
                                ).toLocaleString()}
                            </span>
                        )}
                    </div>

                    <div className="timeline-message">
                        {event.content}
                    </div>
                </div>
            ))}
        </div>
    );
}