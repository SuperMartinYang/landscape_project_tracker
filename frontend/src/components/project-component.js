import React, { useState, useEffect } from 'react';
import { createProject, getProject, updateProject, deleteProject } from '../services/api';

const ProjectComponent = () => {
  const [projects, setProjects] = useState([]);
  const [project, setProject] = useState({ address: '', owner: '', phone: '', status: '', total_price: '' });
  const [editMode, setEditMode] = useState(false);
  const [projectId, setProjectId] = useState(null);

  useEffect(() => {
    // Load initial projects
    fetchProjects();
  }, []);

  const fetchProjects = async () => {
    // Implement the API call to fetch all projects
    // This assumes there's an endpoint to get all projects, which isn't shown in your Flask code.
    // You might need to implement this endpoint in your Flask backend.
    // Example:
    // const response = await getAllProjects();
    // setProjects(response.data);
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setProject({ ...project, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (editMode) {
      await updateProject(projectId, project);
    } else {
      await createProject(project);
    }
    setEditMode(false);
    setProjectId(null);
    setProject({ address: '', owner: '', phone: '', status: '', total_price: '' });
    fetchProjects();
  };

  const handleEdit = async (id) => {
    setEditMode(true);
    setProjectId(id);
    const response = await getProject(id);
    setProject(response.data);
  };

  const handleDelete = async (id) => {
    await deleteProject(id);
    fetchProjects();
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type="text" name="address" value={project.address} onChange={handleInputChange} placeholder="Address" />
        <input type="text" name="owner" value={project.owner} onChange={handleInputChange} placeholder="Owner" />
        <input type="text" name="phone" value={project.phone} onChange={handleInputChange} placeholder="Phone" />
        <input type="text" name="status" value={project.status} onChange={handleInputChange} placeholder="Status" />
        <input type="number" name="total_price" value={project.total_price} onChange={handleInputChange} placeholder="Total Price" />
        <button type="submit">{editMode ? 'Update' : 'Create'}</button>
      </form>
      <ul>
        {projects.map((proj) => (
          <li key={proj.id}>
            {proj.address} - {proj.owner} - {proj.phone}
            <button onClick={() => handleEdit(proj.id)}>Edit</button>
            <button onClick={() => handleDelete(proj.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ProjectComponent;
