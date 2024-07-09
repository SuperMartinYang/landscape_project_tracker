export interface ProjectMetadata {
    id: number;
    address: string;
    owner: string;
    phone: string;
    status: string;
    total_price: number;
}

export interface ProjectScope {
    id: number;
    project_id: number;
    scope: string;
}

export interface ProjectProgress {
    id: number;
    project_id: number;
    work_done: string;
    payment_percentage: number;
    payment_value: number;
}
