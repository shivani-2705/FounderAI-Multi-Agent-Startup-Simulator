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

    current_agent: string;

    progress: number;

    idea: string;

    results: ProjectResults;
}

export interface CreateProjectResponse {
    project_id: string;
    status: string;
}