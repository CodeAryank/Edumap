/*
import React from "react";

function DownloadButton({ summary }) {
  const handleDownload = () => {
    const blob = new Blob([summary], { type: "text/plain" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "summary.txt";
    a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <button onClick={handleDownload} style={{ marginTop: "20px" }}>
      Download Summary
    </button>
  );
}

export default DownloadButton;
*/


import React, { useState } from "react";
import { jsPDF } from "jspdf";

function DownloadButton({ summary }) {
  const [format, setFormat] = useState("txt");

  const handleDownload = () => {
    if (!summary || summary.length === 0) {
      alert("No summary available to download!");
      return;
    }

    if (format === "txt") {
      // Generate TXT file
      const blob = new Blob([summary.join("\n")], { type: "text/plain" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = "summary.txt";
      a.click();
      URL.revokeObjectURL(url);
    } else if (format === "pdf") {
      // Generate PDF file
      const doc = new jsPDF();
      doc.setFont("Helvetica", "normal");
      doc.setFontSize(12);

      summary.forEach((point, index) => {
        doc.text(`${index + 1}. ${point}`, 10, 10 + index * 10); // Add each point
      });

      doc.save("summary.pdf");
    }
  };

  return (
    <div style={{ marginTop: "20px" }}>
      <label>
        Select format: 
        <select value={format} onChange={(e) => setFormat(e.target.value)}>
          <option value="txt">TXT</option>
          <option value="pdf">PDF</option>
        </select>
      </label>
      <button onClick={handleDownload} style={{ marginLeft: "10px" }}>
        Download Summary
      </button>
    </div>
  );
}

export default DownloadButton;

