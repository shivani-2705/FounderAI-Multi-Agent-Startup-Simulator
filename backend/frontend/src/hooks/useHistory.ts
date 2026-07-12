import { useEffect, useState } from "react";

import { getHistory } from "../services/projectService";
import type{ HistoryResponse } from "../types/project";

export function useHistory(projectId: string) {
    const [history, setHistory] = useState<HistoryResponse>({
        project_id: "",
        events: [],
    });

    const [loading, setLoading] = useState(true);

    const [error, setError] = useState("");

    useEffect(() => {

        if (!projectId) return;
    
        async function load() {
    
            try {
    
                const data = await getHistory(projectId);
    
                setHistory(data);
    
            } catch {
    
                setError("Unable to load history.");
    
            } finally {
    
                setLoading(false);
    
            }
        }
    
        load();
    
        const interval = setInterval(load, 2000);
    
        return () => clearInterval(interval);
    
    }, [projectId]);

    return {
        history,
        loading,
        error,
    };
}