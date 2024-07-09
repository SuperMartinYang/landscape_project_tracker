import React, { useState, useEffect, ChangeEvent, FormEvent } from 'react';
import { createProject, getProject, updateProject, deleteProject, getAllProjects } from '../services/api';
import { ProjectMetadata } from '../models/project-models';

const ProjectComponent: React.FC = () => {
  const [projects, setProjects] = useState<ProjectMetadata[]>([]);
  const [ProjectMetadata, setProject] = useState<ProjectMetadata>({
    id: 0,
    address: '',
    owner: '',
    phone: '',
    status: '',
    total_price: 0
  });
  const [editMode, setEditMode] = useState(false);
  const [projectId, setProjectId] = useState<number | null>(null);

  useEffect(() => {
    // Load initial projects
    fetchProjects();
  }, []);

  const fetchProjects = async () => {
    // Implement the API call to fetch all projects
    // This assumes there's an endpoint to get all projects, which isn't shown in your Flask code.
    // You might need to implement this endpoint in your Flask backend.
    // Example:
    const response = await getAllProjects();
    setProjects(response.data);
  };

  const handleInputChange = (e: ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setProject({ ...ProjectMetadata, [name]: value });
  };

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    if (editMode) {
      if (projectId !== null) {
        await updateProject(projectId, ProjectMetadata);
      }
    } else {
      await createProject(ProjectMetadata);
    }
    setEditMode(false);
    setProjectId(null);
    setProject({
      id: 0,
      address: '',
      owner: '',
      phone: '',
      status: '',
      total_price: 0
    });
    fetchProjects();
  };

  const handleEdit = async (id: number) => {
    setEditMode(true);
    setProjectId(id);
    const response = await getProject(id);
    setProject(response.data);
  };

  const handleDelete = async (id: number) => {
    await deleteProject(id);
    fetchProjects();
  };

  return (
    <div>
      <form onSubmit={handleSubmit} className="project-form">
        <div className="form-group">
          <label htmlFor="address">Address</label>
          <input
            type="text"
            name="address"
            id="address"
            value={ProjectMetadata.address}
            onChange={handleInputChange}
            placeholder="Address"
          />
        </div>
        <div className="form-group">
          <label htmlFor="owner">Owner</label>
          <input
            type="text"
            name="owner"
            id="owner"
            value={ProjectMetadata.owner}
            onChange={handleInputChange}
            placeholder="Owner"
          />
        </div>
        <div className="form-group">
          <label htmlFor="phone">Phone</label>
          <input
            type="text"
            name="phone"
            id="phone"
            value={ProjectMetadata.phone}
            onChange={handleInputChange}
            placeholder="Phone"
          />
        </div>
        <div className="form-group">
          <label htmlFor="status">Status</label>
          <input
            type="text"
            name="status"
            id="status"
            value={ProjectMetadata.status}
            onChange={handleInputChange}
            placeholder="Status"
          />
        </div>
        <div className="form-group">
          <label htmlFor="total_price">Total Price</label>
          <input
            type="number"
            name="total_price"
            id="total_price"
            value={ProjectMetadata.total_price}
            onChange={handleInputChange}
            placeholder="Total Price"
          />
        </div>
        <button type="submit" className="submit-button">
          {editMode ? 'Update' : 'Create'}
        </button>
      </form>

      <table>
        <thead>
          <tr>
            <th>Address</th>
            <th>Owner</th>
            <th>Phone</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {projects.map((proj) => (
            <tr key={proj.id}>
              <td>{proj.address}</td>
              <td>{proj.owner}</td>
              <td>{proj.phone}</td>
              <td>
                <button onClick={() => handleEdit(proj.id!)}>Edit</button>
                <button onClick={() => handleDelete(proj.id!)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

    </div>
  );
};

export default ProjectComponent;
