/*
import React, { useState } from "react";  // Remove useEffect since we don't need it anymore
import FileUpload from "./components/FileUpload";
import SummaryDisplay from "./components/SummaryDisplay";
import DownloadButton from "./components/DownloadButton";
import "./App.css";

function App() {
  const [summary, setSummary] = useState("");

  // Function to fetch the summary from backend
  const fetchSummary = async () => {
    try {
      const response = await fetch("http://localhost:5000/get-summary");
      const data = await response.json();
      
      if (data.success) {
        setSummary(data.summary);
      } else {
        console.error("Failed to fetch summary:", data.error);
      }
    } catch (error) {
      console.error("Error fetching summary:", error);
    }
  };

  // Handler for file upload
  const handleUpload = async (files) => {
    const fileData = new FormData();
    files.forEach((file) => fileData.append("files", file));

    try {
      const response = await fetch("http://localhost:5000/upload", {
        method: "POST",
        body: fileData,
      });

      if (!response.ok) {
        throw new Error("Failed to upload files");
      }

      return await response.json();
    } catch (error) {
      console.error("Error:", error);
      return null;
    }
  };

  return (
    <div>
      <FileUpload onUpload={handleUpload} onGenerateSummary={fetchSummary} />
      <SummaryDisplay summary={summary} />
      <DownloadButton />
    </div>
  );
}

export default App;

*/



import React, { useState } from "react";
import FileUpload from "./components/FileUpload";
import SummaryDisplay from "./components/SummaryDisplay";
import DownloadButton from "./components/DownloadButton";
import "./App.css";

function App() {
  const [summary, setSummary] = useState([]);

  // Function to fetch the summary from backend
  
  const fetchSummary = async () => {
    try {
      const response = await fetch("http://localhost:3000/get-summary");
      const data = await response.json();

      if (data.success) {
        // Assume the backend sends the summary as a single string; split it into points
        setSummary(data.summary.split("\n").map((point) => point.trim()));
      } else {
        console.error("Failed to fetch summary:", data.error);
      }
    } catch (error) {
      console.error("Error fetching summary:", error);
    }
  };
  
  // Handler for file upload
  const handleUpload = async (files) => {
    const fileData = new FormData();
    files.forEach((file) => fileData.append("files", file));

    try {
      const response = await fetch("http://localhost:3000/upload", {
        method: "POST",
        body: fileData,
      });

      if (!response.ok) {
        throw new Error("Failed to upload files");
      }

      return await response.json();
    } catch (error) {
      console.error("Error:", error);
      return null;
    }
  };

  return (
    <div>
      <FileUpload onUpload={handleUpload} onGenerateSummary={fetchSummary} />
      <SummaryDisplay summary={summary} />
      <DownloadButton summary={summary} />
    </div>
  );
}

export default App;










