// App.js
import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
  const [image, setImage] = useState(null);
  const [analysisResult, setAnalysisResult] = useState('');

  const handleImageChange = (event) => {
    setImage(event.target.files[0]);
  };

  const handleSubmit = async () => {
    const formData = new FormData();
    formData.append('image', image);

    try {
      const response = await axios.post('/api/analyze', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setAnalysisResult(response.data.result);
    } catch (error) {
      console.error('Error analyzing image:', error);
    }
  };

  return (
    <div>
      <input type="file" onChange={handleImageChange} />
      <button onClick={handleSubmit}>Analyze Image</button>
      {analysisResult && <p>Analysis Result: {analysisResult}</p>}
    </div>
  );
};

export default App;
