import { useNavigate } from "react-router-dom";
import { useState } from "react";

import { createProject } from "../api/projectApi";

export function useCreateProject() {

    const navigate = useNavigate();

    const [loading, setLoading] = useState(false);

    const [error, setError] = useState("");

    async function submit(idea: string) {

        try {

            setLoading(true);
            setError("");

            const project = await createProject(idea);

            navigate(`/projects/${project.project_id}`);

        } catch {

            setError("Failed to create project.");

        } finally {

            setLoading(false);

        }
    }

    return {
        submit,
        loading,
        error,
    };
}