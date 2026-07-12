import client from "./client";

export interface CreateProjectResponse {
    project_id: string;
    message: string;
}

export interface ProjectStatus {
    project_id: string;
    status: string;
    current_agent: string;
    progress: number;
}

export interface ProjectResults {
    ceo_analysis: Record<string, unknown> | null;
    technical_architecture: Record<string, unknown> | null;
    prd: Record<string, unknown> | null;
    design: Record<string, unknown> | null;
    marketing: Record<string, unknown> | null;
    investment: Record<string, unknown> | null;
}

export interface ProjectResponse {
    project_id: string;
    status: string;
    idea: string;
    current_agent: string;
    progress: number;
    error_message: string | null;

    results: ProjectResults;
}

export interface HistoryEvent {
    timestamp: string;
    agent: string;
    event_type: string;
    content: string;
}

export interface HistoryResponse {
    project_id: string;
    events: HistoryEvent[];
}

export async function createProject(
    idea: string,
): Promise<CreateProjectResponse> {

    const response = await client.post(
        "/projects",
        null,
        {
            params: {
                idea,
            },
        },
    );

    return response.data;
}

export async function getProject(
    projectId: string,
): Promise<ProjectResponse> {

    const response = await client.get(
        `/projects/${projectId}`,
    );

    return response.data;
}

export async function getProjectStatus(
    projectId: string,
): Promise<ProjectStatus> {

    const response = await client.get(
        `/projects/${projectId}/status`,
    );

    return response.data;
}

export async function getProjectHistory(
    projectId: string,
): Promise<HistoryResponse> {

    const response = await client.get(
        `/projects/${projectId}/history`,
    );

    return response.data;
}