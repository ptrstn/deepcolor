import React from 'react';
import { PageLayout } from './components/PageLayout';

import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons';
import './App.css';

library.add(fas, fab)


function App() {
  return (
    <div className="App">
        <PageLayout />
    </div>
  );
}

export default App;
