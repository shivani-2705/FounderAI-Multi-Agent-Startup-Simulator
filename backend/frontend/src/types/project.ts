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

    error_message: string | null;

    idea: string;

    results: ProjectResults;
}

export interface ProjectStatusResponse {
    project_id: string;

    status: string;

    current_agent: string;

    progress: number;
}

export interface CreateProjectResponse {
    project_id: string;

    status: string;
}


export interface HistoryEvent {
    timestamp: string;
    agent: string;
    event_type:
        | "analysis"
        | "review"
        | "question"
        | "answer"
        | "revision"
        | "decision";

    content: string;

}

export interface ProjectHistoryResponse {
    project_id: string;
    events: HistoryEvent[];

}