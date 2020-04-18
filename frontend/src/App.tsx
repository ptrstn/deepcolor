import React from 'react';
import './App.scss';
import { ImageUpload } from './components/ImageUpload';

import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons';

library.add(fas, fab)


function App() {
  return (
    <div className="App">
      <div className="App-content">
        <ImageUpload />
      </div>
    </div>
  );
}

export default App;
