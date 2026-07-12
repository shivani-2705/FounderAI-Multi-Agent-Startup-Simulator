import client from "../api/client";

import type {
    ProjectHistoryResponse,
} from "../types/project";

export async function getHistory(
    projectId: string
): Promise<ProjectHistoryResponse> {

    const response = await client.get(
        `/projects/${projectId}/history`
    );

    return response.data;
}