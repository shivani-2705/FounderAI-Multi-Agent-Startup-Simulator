import { useParams } from "react-router-dom";

import { useProject } from "../hooks/useProject";

import ProgressBar from "../components/ProgressBar";
import LoadingSpinner from "../components/LoadingSpinner";

export default function ProjectPage() {

    const { projectId } = useParams();

    
    const {
        project,
        loading,
        error,
    } = useProject(projectId ?? "");

    if (!projectId) {
        return <p>Invalid project.</p>;
    }

    if (loading) {
        return <LoadingSpinner />;
    }

    if (error) {
        return <p>{error}</p>;
    }

    if (!project) {
        return <p>Project not found.</p>;
    }

    return (
        <div>
            <h1>FounderAI</h1>

            <p>
                <strong>Status:</strong> {project.status}
            </p>

            <p>
                <strong>Current Agent:</strong> {project.current_agent}
            </p>

            <ProgressBar progress={project.progress} />
        </div>
    );
}