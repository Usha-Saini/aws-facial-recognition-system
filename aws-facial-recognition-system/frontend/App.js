import React, { useState } from "react";
import { v4 as uuidv4 } from "uuid";
import "./App.css";

function App() {
  const [visitorImage, setVisitorImage] = useState(null);
  const [message, setMessage] = useState("Facial Recognition System");
  const [messageType, setMessageType] = useState("title");
  const [loading, setLoading] = useState(false);

  const handleFileChange = (event) => {
    setVisitorImage(event.target.files[0]);
    setMessage("Image selected. Ready to authenticate!");
    setMessageType("info");
  };

  const handleAuthenticate = async () => {
    if (!visitorImage) {
      setMessage("Please select an image first!");
      setMessageType("error");
      return;
    }

    setLoading(true);
    setMessage("Authenticating...");
    setMessageType("loading");

    // Simulated delay like real API call
    setTimeout(() => {
      const randomId = uuidv4().slice(0, 6).toUpperCase();

      setMessage(`Authentication Successful! Welcome User-${randomId}`);
      setMessageType("success");
      setLoading(false);
    }, 1200);
  };

  return (
    <div className="container">
      <h1 className={`message ${messageType}`}>{message}</h1>

      <div className="upload-section">
        <input type="file" accept="image/*" onChange={handleFileChange} />
        <button onClick={handleAuthenticate} disabled={loading}>
          {loading ? "Please wait..." : "Authenticate"}
        </button>
      </div>

      {visitorImage && (
        <img
          src={URL.createObjectURL(visitorImage)}
          alt="Visitor"
          className="preview-image"
        />
      )}
    </div>
  );
}

export default App;
