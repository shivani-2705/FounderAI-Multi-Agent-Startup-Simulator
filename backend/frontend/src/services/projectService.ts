import client from "../api/client";

import type {
    CreateProjectResponse,
    ProjectResponse,
    ProjectStatusResponse,
} from "../types/project";

import type{
    HistoryResponse,
} from "../types/project";

export async function createProject(
    idea: string
): Promise<CreateProjectResponse> {

    const response = await client.post(
        "/projects",
        null,
        {
            params: {
                idea,
            },
        }
    );

    return response.data;
}

export async function getProject(
    projectId: string
): Promise<ProjectResponse> {

    const response = await client.get(
        `/projects/${projectId}`
    );

    return response.data;
}

export async function getProjectStatus(
    projectId: string
): Promise<ProjectStatusResponse> {

    const response = await client.get(
        `/projects/${projectId}/status`
    );

    return response.data;
}

export async function getHistory(
    projectId: string
): Promise<HistoryResponse> {

    const response = await client.get<HistoryResponse>(
        `/projects/${projectId}/history`
    );

    return response.data;
}