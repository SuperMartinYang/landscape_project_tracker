import React, { Component } from 'react';
import ProjectComponent from './components/project-component';

interface AppState {
  count: number;
}

class App extends Component<{}, AppState> {
  state: AppState = {
    count: 0
  };

  increment = () => {
    this.setState({ count: this.state.count + 1 });
  };

  render() {
    return (
      <div className="App">
        <h1>Project Management</h1>
        <ProjectComponent />
        {/* Add other components for Scope and Progress */}
      </div>
    );
  }
}

export default App;
