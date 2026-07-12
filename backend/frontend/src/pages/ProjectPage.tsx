import { useParams } from "react-router-dom";

import { useProject } from "../hooks/useProject";

import AgentCard from "../components/AgentCard";
import ResultCard from "../components/ResultCard";
import ProgressBar from "../components/ProgressBar";
import LoadingSpinner from "../components/LoadingSpinner";

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

    const agents = [
        "CEO",
        "CTO",
        "PM",
        "Designer",
        "Marketing",
        "Investor",
    ];

    const currentAgent =
        status?.current_agent ??
        project?.current_agent ??
        "";

    const currentIndex =
        currentAgent === "Completed"
            ? agents.length
            : agents.indexOf(currentAgent);

    if (error) {
        return <p>{error}</p>;
    }

    if (loading && status) {
        return (
            <div className="container">
                <h1>FounderAI</h1>

                <p>
                    <strong>Status:</strong>{" "}
                    {status.status}
                </p>

                <p>
                    <strong>Current Agent:</strong>{" "}
                    {status.current_agent}
                </p>

                <ProgressBar
                    progress={status.progress}
                />

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

                <LoadingSpinner />
            </div>
        );
    }

    if (!project) {
        return <LoadingSpinner />;
    }

    return (
        <div className="container">
            <h1>FounderAI</h1>

            <p>
                <strong>Status:</strong>{" "}
                {project.status}
            </p>

            <p>
                <strong>Current Agent:</strong>{" "}
                {project.current_agent}
            </p>

            <ProgressBar
                progress={project.progress}
            />

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

            <hr />

            <h2>Startup Idea</h2>

            <p>{project.idea}</p>

            <hr />

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
        </div>
    );
}