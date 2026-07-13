import { useState } from "react";
import { Link, useParams } from "react-router-dom";

import { useProject } from "../hooks/useProject";

import AgentCard from "../components/AgentCard";
import ProgressBar from "../components/ProgressBar";
import LoadingSpinner from "../components/LoadingSpinner";
import ResultCard from "../components/ResultCard";
import StatusBadge from "../components/StatusBadge";

export default function ProjectPage() {
    const { projectId } = useParams();

    const {
        project,
        status,
        loading,
        error,
    } = useProject(projectId ?? "");

    const [activeTab, setActiveTab] =
        useState("CEO");

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

    function renderActiveResult() {
        if (!project) return null;

        switch (activeTab) {
            case "CEO":
                return (
                    <ResultCard
                        title="CEO Analysis"
                        data={project.results.ceo_analysis}
                    />
                );

            case "CTO":
                return (
                    <ResultCard
                        title="Technical Architecture"
                        data={
                            project.results
                                .technical_architecture
                        }
                    />
                );

            case "PM":
                return (
                    <ResultCard
                        title="Product Requirements (PRD)"
                        data={project.results.prd}
                    />
                );

            case "Designer":
                return (
                    <ResultCard
                        title="UI / UX Design"
                        data={project.results.design}
                    />
                );

            case "Marketing":
                return (
                    <ResultCard
                        title="Marketing Strategy"
                        data={project.results.marketing}
                    />
                );

            case "Investor":
                return (
                    <ResultCard
                        title="Investment Analysis"
                        data={project.results.investment}
                    />
                );

            default:
                return null;
        }
    }

    return (
        <div className="container">
            <h1>🚀 FounderAI</h1>

            {/* Summary */}

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

            {/* Workflow */}

            <section>

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

            </section>

            {/* Spinner */}

            {loading && (
                <div style={{ marginTop: 24 }}>
                    <LoadingSpinner />
                </div>
            )}

            {/* Results */}

            {project && (
                <>

                    <section>

                        <h2>💡 Startup Idea</h2>

                        <div className="summary-card">
                            <p>{project.idea}</p>
                        </div>

                    </section>

                    <section className="results-section">

                        <h2>AI Executive Reports</h2>

                        <div className="results-tabs">

                            <button
                                className={
                                    activeTab === "CEO"
                                        ? "tab-button active"
                                        : "tab-button"
                                }
                                onClick={() =>
                                    setActiveTab("CEO")
                                }
                            >
                                CEO
                            </button>

                            <button
                                className={
                                    activeTab === "CTO"
                                        ? "tab-button active"
                                        : "tab-button"
                                }
                                onClick={() =>
                                    setActiveTab("CTO")
                                }
                            >
                                CTO
                            </button>

                            <button
                                className={
                                    activeTab === "PM"
                                        ? "tab-button active"
                                        : "tab-button"
                                }
                                onClick={() =>
                                    setActiveTab("PM")
                                }
                            >
                                PM
                            </button>

                            <button
                                className={
                                    activeTab === "Designer"
                                        ? "tab-button active"
                                        : "tab-button"
                                }
                                onClick={() =>
                                    setActiveTab(
                                        "Designer",
                                    )
                                }
                            >
                                Designer
                            </button>

                            <button
                                className={
                                    activeTab ===
                                    "Marketing"
                                        ? "tab-button active"
                                        : "tab-button"
                                }
                                onClick={() =>
                                    setActiveTab(
                                        "Marketing",
                                    )
                                }
                            >
                                Marketing
                            </button>

                            <button
                                className={
                                    activeTab ===
                                    "Investor"
                                        ? "tab-button active"
                                        : "tab-button"
                                }
                                onClick={() =>
                                    setActiveTab(
                                        "Investor",
                                    )
                                }
                            >
                                Investor
                            </button>

                        </div>

                        <div className="tab-content">
                            {renderActiveResult()}
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