import { useEffect, useState } from "react";

import { getHistory } from "../services/historyService";

import type {
    ProjectHistoryResponse,
} from "../types/project";

export function useHistory(
    projectId: string
) {

    const [history, setHistory] =
        useState<ProjectHistoryResponse | null>(null);

    useEffect(() => {

        if (!projectId) return;

        getHistory(projectId)
            .then(setHistory);

    }, [projectId]);

    return history;

}