import { useEffect, useState } from "react";

import {
    getProject,
    getProjectStatus,
} from "../services/projectService";

import type {
    ProjectResponse,
    ProjectStatusResponse,
} from "../types/project";

export function useProject(
    projectId: string,
) {
    const [project, setProject] =
        useState<ProjectResponse | null>(null);

    const [status, setStatus] =
        useState<ProjectStatusResponse | null>(null);

    const [loading, setLoading] =
        useState(true);

    const [error, setError] =
        useState("");

    useEffect(() => {
        if (!projectId) {
            return;
        }

        let cancelled = false;
        let timeoutId: number | undefined;

        async function pollStatus() {
            try {
                const [statusData, projectData] =
                    await Promise.all([
                        getProjectStatus(projectId),
                        getProject(projectId),
                    ]);
        
                if (cancelled) {
                    return;
                }
        
                setStatus(statusData);
                setProject(projectData);
        
                if (statusData.status === "completed") {
                    setLoading(false);
                    return;
                }
        
                if (statusData.status === "failed") {
                    setLoading(false);
                    setError("Project execution failed.");
                    return;
                }
        
                setLoading(false);
        
                timeoutId = window.setTimeout(
                    pollStatus,
                    2000,
                );
            } catch {
                if (cancelled) {
                    return;
                }
        
                setLoading(false);
                setError("Failed to load project.");
            }
        }
        pollStatus();

        return () => {
            cancelled = true;

            if (timeoutId) {
                clearTimeout(timeoutId);
            }
        };
    }, [projectId]);

    return {
        project,
        status,
        loading,
        error,
    };
}