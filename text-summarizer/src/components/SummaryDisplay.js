
import React from "react";

function SummaryDisplay({ summary }) {
  return (
    <div className="summary-section">
      <h2>Summary</h2>
      {summary ? (
        <p>{summary}</p>
      ) : (
        <p>Upload documents and click "Generate Summary" to see results here.</p>
      )}
    </div>
  );
}

export default SummaryDisplay;









