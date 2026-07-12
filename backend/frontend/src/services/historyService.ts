import client from "../api/client";

import type {
    HistoryResponse
} from "../types/project";

export async function getHistory(
    projectId: string
): Promise<HistoryResponse> {

    const response = await client.get(
        `/projects/${projectId}/history`
    );

    return response.data;
}