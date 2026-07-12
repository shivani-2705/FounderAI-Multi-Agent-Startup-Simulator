import { useState } from "react";
import { createProject } from "../services/projectService";
import { useNavigate } from "react-router-dom";

export default function HomePage() {

    const [idea, setIdea] = useState("");
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    async function handleSubmit() {

        if (!idea.trim()) {
            return;
        }

        try {

            setLoading(true);

            const response = await createProject(
                idea
            );

            navigate(
                `/projects/${response.project_id}`
            );

        } catch {

            alert(
                "Failed to create project."
            );

        } finally {

            setLoading(false);

        }

    }

    return (

        <div className="home">

            <h1>
                Validate Your Startup Idea
            </h1>

            <p>
                Our AI board members will review your startup
                from CEO, CTO, PM, Design, Marketing and Investor perspectives.
            </p>

            <textarea
                value={idea}
                onChange={(e) => setIdea(e.target.value)}
                placeholder="Describe your startup idea..."
                rows={8}
            />

            <button
                onClick={handleSubmit}
                disabled={loading}
            >
                {loading
                    ? "Creating..."
                    : "Analyze Startup"}
            </button>

        </div>

    );
}