import { useState } from "react";
import { useNavigate } from "react-router-dom";

import { createProject } from "../services/projectService";

export default function HomePage() {
    const navigate = useNavigate();

    const [idea, setIdea] = useState("");
    const [loading, setLoading] = useState(false);

    async function handleGenerate() {
        if (!idea.trim()) return;

        setLoading(true);

        try {
            const project = await createProject(idea);

            navigate(`/projects/${project.project_id}`);
        } finally {
            setLoading(false);
        }
    }

    return (
        <div className="home">

            <section className="hero">

                <span className="hero-badge">
                    🚀 AI Powered Startup Builder
                </span>

                <h1>
                    Build your startup with
                    <br />
                    an AI executive team.
                </h1>

                <p className="hero-description">
                    FounderAI simulates a CEO, CTO,
                    Product Manager, Designer,
                    Marketing Expert and Investor
                    to transform your idea into
                    a complete startup plan.
                </p>

            </section>

            <section className="idea-card">

                <h2>Describe your startup idea</h2>

                <p>
                    Explain your product, target users,
                    problem statement or vision.
                </p>

                <textarea
                    value={idea}
                    onChange={(e) => setIdea(e.target.value)}
                    placeholder="Example:

Build an AI-powered ambulance platform that predicts emergencies,
dispatches the nearest ambulance, optimizes routes,
and shares patient vitals with hospitals before arrival."
                />

                <button
                    disabled={
                        loading ||
                        !idea.trim()
                    }
                    onClick={handleGenerate}
                >
                    {loading
                        ? "Creating Project..."
                        : "Generate Startup"}
                </button>

            </section>

            <section className="features">

                <div className="feature-card">
                    <div className="feature-icon">
                        🧠
                    </div>

                    <h3>CEO</h3>

                    <p>
                        Vision, market,
                        users and business model.
                    </p>
                </div>

                <div className="feature-card">
                    <div className="feature-icon">
                        ⚙️
                    </div>

                    <h3>CTO</h3>

                    <p>
                        Architecture,
                        technology stack
                        and deployment.
                    </p>
                </div>

                <div className="feature-card">
                    <div className="feature-icon">
                        📋
                    </div>

                    <h3>Product Manager</h3>

                    <p>
                        Complete PRD,
                        roadmap and features.
                    </p>
                </div>

                <div className="feature-card">
                    <div className="feature-icon">
                        🎨
                    </div>

                    <h3>Designer</h3>

                    <p>
                        UX flow,
                        screens and design ideas.
                    </p>
                </div>

                <div className="feature-card">
                    <div className="feature-icon">
                        📢
                    </div>

                    <h3>Marketing</h3>

                    <p>
                        Go-to-market strategy
                        and customer acquisition.
                    </p>
                </div>

                <div className="feature-card">
                    <div className="feature-icon">
                        💰
                    </div>

                    <h3>Investor</h3>

                    <p>
                        Funding readiness,
                        risks and investment score.
                    </p>
                </div>

            </section>

        </div>
    );
}