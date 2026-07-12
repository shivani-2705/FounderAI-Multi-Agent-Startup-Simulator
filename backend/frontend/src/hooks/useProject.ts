import { useEffect, useState } from "react";

import { getProject } from "../services/projectService";

import type { ProjectResponse } from "../types/project";

export function useProject(
    projectId: string
) {
    const [project, setProject] =
        useState<ProjectResponse | null>(null);

    const [loading, setLoading] =
        useState(true);

    const [error, setError] =
        useState("");

        useEffect(() => {
            let timeoutId: number | undefined;
            let cancelled = false;

            if (!projectId) {
                return;
            }
    
        
            async function loadProject() {
                try {
                    const data = await getProject(projectId);
        
                    if (cancelled) return;
        
                    setProject(data);
                    setLoading(false);
        
                    if (
                        data.status !== "completed" &&
                        data.status !== "failed"
                    ) {
                        timeoutId = window.setTimeout(
                            loadProject,
                            2000
                        );
                    }
                } catch {
                    if (cancelled) return;
        
                    setError("Failed to load project");
                    setLoading(false);
                }
            }
        
            loadProject();
        
            return () => {
                cancelled = true;
        
                if (timeoutId) {
                    clearTimeout(timeoutId);
                }
            };
        }, [projectId]);
    return {
        project,
        loading,
        error,
    };
}