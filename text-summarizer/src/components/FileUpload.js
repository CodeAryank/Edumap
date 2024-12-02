/*import React, { useState } from "react";

function FileUpload({ onUpload, onGenerateSummary }) {
  const [files, setFiles] = useState([]);
  const [downloadUrls, setDownloadUrls] = useState([]);
  const [isUploading, setIsUploading] = useState(false);
  const [isUploaded, setIsUploaded] = useState(false);
  const [error, setError] = useState("");

  const handleFileChange = (e) => {
    const selectedFiles = Array.from(e.target.files);
    // Check file types
    const validFiles = selectedFiles.every(file => 
      file.type === 'application/pdf' || file.type === 'text/plain'
    );

    if (!validFiles) {
      setError("Please only upload PDF or TXT files");
      return;
    }

    setFiles(selectedFiles);
    setIsUploaded(false);
    setError("");
  };

  const handleUploadClick = async () => {
    if (files.length === 0) {
      setError("Please select at least one document.");
      return;
    }

    setIsUploading(true);
    setError("");

    try {
      const result = await onUpload(files);
      if (result?.success) {
        setDownloadUrls(result.downloadUrls);
        setIsUploaded(true);
      } else {
        setError("Error uploading files.");
      }
    } catch (error) {
      console.error("Error uploading files:", error);
      setError("Failed to upload files. Please try again.");
    } finally {
      setIsUploading(false);
    }
  };

  const handleGenerateSummary = async () => {
    if (!isUploaded) {
      setError("Please upload files first before generating summary.");
      return;
    }

    try {
      setError("");
      await onGenerateSummary();
    } catch (error) {
      console.error("Error generating summary:", error);
      setError("Failed to generate summary. Please try again.");
    }
  };

  return (
    <div className="file-upload">
      <h className="app-header">Document Summarizer</h>
      <div className="upload-section">
        <h>Upload documents</h>
        <div className="file-input-container">
          <input 
            type="file" 
            multiple 
            onChange={handleFileChange}
            accept=".pdf,.txt"
            className="file-input"
            disabled={isUploading}
          />
          {files.length > 0 && (
            <div className="selected-files">
              <p>Selected files ({files.length}):</p>
              <ul>
                {files.map((file, index) => (
                  <li key={index}>{file.name}</li>
                ))}
              </ul>
            </div>
          )}
        </div>

        {error && <div className="error-message">{error}</div>}

        <div className="button-group">
          { <button 
            onClick={handleUploadClick}
            //className="upload-button"
            disabled={files.length === 0 || isUploading}
          >
            {isUploading ? "Uploading..." : "Upload"}
          </button> }
          { <button 
            onClick={handleGenerateSummary}
            //className="generate-button"
            disabled={!isUploaded}
          >
            Generate Summary
          </button> }
        </div>
      </div>

      {downloadUrls.length > 0 && (
        <div className="download-section">
          <h3>Download Links:</h3>
          <div className="download-links">
            {downloadUrls.map((url, index) => (
              <a
                key={index}
                href={`http://localhost:5000${url}`}
                className="download-link"
                download
              >
                Download {files[index]?.name || `File ${index + 1}`}
              </a>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default FileUpload;*/



import React, { useState } from "react";

function FileUpload({ onUpload, onGenerateSummary }) {
  const [files, setFiles] = useState([]);
  const [downloadUrls, setDownloadUrls] = useState([]);
  const [isUploaded, setIsUploaded] = useState(false);

  const handleFileChange = (e) => {
    setFiles(Array.from(e.target.files));
    setIsUploaded(false); // Reset upload status when new files are selected
  };

  const handleUploadClick = async () => {
    if (files.length > 0) {
      try {
        const result = await onUpload(files);
        if (result?.success) {
          setDownloadUrls(result.downloadUrls);
          setIsUploaded(true);
        } else {
          alert("Error uploading files.");
        }
      } catch (error) {
        console.error("Error uploading files:", error);
        alert("Error uploading files.");
      }
    } else {
      alert("Please select at least one document.");
    }
  };

  const handleGenerateSummary = async () => {
    if (!isUploaded) {
      alert("Please upload files first before generating summary.");
      return;
    }
    try {
      await onGenerateSummary();
    } catch (error) {
      console.error("Error generating summary:", error);
      alert("Error generating summary.");
    }
  };

 

  return (
    <div className="upload-section">
      <h2>Upload Documents</h2>
      <div>
        <input 
          type="file" 
          multiple 
          onChange={handleFileChange}
          className="file-input"
        />
      </div>
      <div className="button-group">
        <button 
          onClick={handleUploadClick}
          className="upload-button"
          disabled={files.length === 0}
        >
          Upload
        </button>
        <button 
          onClick={handleGenerateSummary}
          className="generate-button"
          disabled={!isUploaded}
        >
          Generate Summary
        </button>
      </div>

      {downloadUrls.length > 0 && (
        <div className="download-links">
          <h3>Download Links:</h3>
          {downloadUrls.map((url, index) => (
            <div key={index}>
              <a href={url} download>
                Download File {index + 1}
              </a>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default FileUpload;