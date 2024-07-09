import axios from 'axios';

const API_URL = 'http://localhost:5000';

export const createProject = (data) => axios.post(`${API_URL}/project_metadata`, data);
export const getProject = (id) => axios.get(`${API_URL}/project_metadata/${id}`);
export const updateProject = (id, data) => axios.put(`${API_URL}/project_metadata/${id}`, data);
export const deleteProject = (id) => axios.delete(`${API_URL}/project_metadata/${id}`);

export const createProjectScope = (data) => axios.post(`${API_URL}/project_scope`, data);
export const getProjectScope = (id) => axios.get(`${API_URL}/project_scope/${id}`);
export const updateProjectScope = (id, data) => axios.put(`${API_URL}/project_scope/${id}`, data);
export const deleteProjectScope = (id) => axios.delete(`${API_URL}/project_scope/${id}`);

export const createProjectProgress = (data) => axios.post(`${API_URL}/project_progress`, data);
export const getProjectProgress = (id) => axios.get(`${API_URL}/project_progress/${id}`);
export const updateProjectProgress = (id, data) => axios.put(`${API_URL}/project_progress/${id}`, data);
export const deleteProjectProgress = (id) => axios.delete(`${API_URL}/project_progress/${id}`);
