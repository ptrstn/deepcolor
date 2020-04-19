import React from 'react';
import './App.scss';
import { PageLayout } from './components/PageLayout';

import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons';

library.add(fas, fab)


function App() {
  return (
    <div className="App">
      <div className="App-content">
        <PageLayout />
      </div>
    </div>
  );
}

export default App;
