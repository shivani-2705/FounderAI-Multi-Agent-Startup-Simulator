import client from "../api/client";

import type {
    CreateProjectResponse,
    ProjectResponse,
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