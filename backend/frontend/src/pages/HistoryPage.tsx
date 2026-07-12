import { Link, useParams } from "react-router-dom";

import { useHistory } from "../hooks/useHistory";

import LoadingSpinner from "../components/LoadingSpinner";
import TimelineItem from "../components/TimelineItem";

export default function HistoryPage() {
    const { projectId } = useParams();

    const {
        history,
        loading,
        error,
    } = useHistory(projectId ?? "");

    if (!projectId) {
        return <p>Invalid project.</p>;
    }

    if (loading) {
        return <LoadingSpinner />;
    }

    if (error) {
        return <p>{error}</p>;
    }

    return (
        <div className="container">

            <div className="page-header">

                <div>
                    <h1>Workflow History</h1>

                    <p>
                        Every conversation between the AI executives.
                    </p>
                </div>

                <Link
                    className="back-button"
                    to={`/projects/${projectId}`}
                >
                    ← Back to Project
                </Link>

            </div>

            <div className="timeline">

                {history.events.length === 0 ? (
                    <p>No history available.</p>
                ) : (
                    history.events.map((event, index) => (
                        <TimelineItem
                            key={index}
                            event={event}
                        />
                    ))
                )}

            </div>

        </div>
    );
}