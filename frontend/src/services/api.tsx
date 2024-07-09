import axios from 'axios';
import { ProjectMetadata, ProjectScope, ProjectProgress } from '../models/project-models';

const API_URL = 'http://localhost:5000';

export const createProject = (data: ProjectMetadata) => axios.post(`${API_URL}/project_metadata`, data);
export const getProject = (id: number) => axios.get<ProjectMetadata>(`${API_URL}/project_metadata/${id}`);
export const updateProject = (id: number, data: ProjectMetadata) => axios.put(`${API_URL}/project_metadata/${id}`, data);
export const deleteProject = (id: number) => axios.delete(`${API_URL}/project_metadata/${id}`);
export const getAllProjects = () => axios.get<ProjectMetadata[]>(`${API_URL}/projects`);

export const createProjectScope = (data: ProjectScope) => axios.post(`${API_URL}/project_scope`, data);
export const getProjectScope = (id: number) => axios.get<ProjectScope>(`${API_URL}/project_scope/${id}`);
export const updateProjectScope = (id: number, data: ProjectScope) => axios.put(`${API_URL}/project_scope/${id}`, data);
export const deleteProjectScope = (id: number) => axios.delete(`${API_URL}/project_scope/${id}`);

export const createProjectProgress = (data: ProjectProgress) => axios.post(`${API_URL}/project_progress`, data);
export const getProjectProgress = (id: number) => axios.get<ProjectProgress>(`${API_URL}/project_progress/${id}`);
export const updateProjectProgress = (id: number, data: ProjectProgress) => axios.put(`${API_URL}/project_progress/${id}`, data);
export const deleteProjectProgress = (id: number) => axios.delete(`${API_URL}/project_progress/${id}`);
