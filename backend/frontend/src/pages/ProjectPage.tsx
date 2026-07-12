import { useParams } from "react-router-dom";
import { Link } from "react-router-dom";
import { useProject } from "../hooks/useProject";

import AgentCard from "../components/AgentCard";
import ResultCard from "../components/ResultCard";
import ProgressBar from "../components/ProgressBar";
import LoadingSpinner from "../components/LoadingSpinner";
import StatusBadge from "../components/StatusBadge";

export default function ProjectPage() {
    const { projectId } = useParams();

    const {
        project,
        status,
        loading,
        error,
    } = useProject(projectId ?? "");

    if (!projectId) {
        return <p>Invalid project.</p>;
    }

    if (error) {
        return <p>{error}</p>;
    }

    const agents = [
        "CEO",
        "CTO",
        "PM",
        "Designer",
        "Marketing",
        "Investor",
    ];

    const displayStatus = status ?? project;

    if (!displayStatus) {
        return <LoadingSpinner />;
    }

    const currentAgent =
        displayStatus.current_agent ?? "";

    const currentIndex =
        currentAgent === "Completed"
            ? agents.length
            : agents.indexOf(currentAgent);

    return (
        <div className="container">
            <h1>FounderAI</h1>

            <div className="project-summary">

                <div className="summary-card">
                    <h3>Status</h3>

                    <StatusBadge
                        status={displayStatus.status}
                    />
                </div>

                <div className="summary-card">
                    <h3>Current Agent</h3>

                    <p>{displayStatus.current_agent}</p>
                </div>

                <div className="summary-card">
                    <h3>Progress</h3>

                    <ProgressBar
                        progress={displayStatus.progress}
                    />
                </div>

            </div>

            <h2>Workflow</h2>

            <div className="agent-list">
                {agents.map((agent, index) => (
                    <AgentCard
                        key={agent}
                        name={agent}
                        state={
                            index < currentIndex
                                ? "completed"
                                : index === currentIndex
                                ? "running"
                                : "waiting"
                        }
                    />
                ))}
            </div>

            {loading && (
                <div
                    style={{
                        marginTop: "24px",
                    }}
                >
                    <LoadingSpinner />
                </div>
            )}

            {project && (
                <>
                    <hr />

                    <section>
                        <h2>Startup Idea</h2>

                        <div className="summary-card">
                            <p>{project.idea}</p>
                        </div>
                    </section>

                    <hr />

                    <section>
                        <h2>AI Results</h2>

                        <div className="results-grid">

                            <ResultCard
                                title="CEO Analysis"
                                data={project.results.ceo_analysis}
                            />

                            <ResultCard
                                title="Technical Architecture"
                                data={project.results.technical_architecture}
                            />

                            <ResultCard
                                title="Product Requirements (PRD)"
                                data={project.results.prd}
                            />

                            <ResultCard
                                title="UI / UX Design"
                                data={project.results.design}
                            />

                            <ResultCard
                                title="Marketing Strategy"
                                data={project.results.marketing}
                            />

                            <ResultCard
                                title="Investment Analysis"
                                data={project.results.investment}
                            />

                        </div>
                    
                    </section>
                    <div className="project-actions">

                        <Link
                            to={`/projects/${projectId}/history`}
                            className="secondary-button"
                        >
                            View Workflow History
                        </Link>

                    </div>
                </>
            )}
        </div>
    );
}