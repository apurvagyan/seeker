// components/Calendar.js

import React from 'react';

const Calendar = ({ applications }) => {
  return (
    <div>
      <h2>Application Timeline</h2>
      <ul>
        {applications.map(application => (
          <li key={application.id}>
            <h3>{application.job.title}</h3>
            <p>Company: {application.company.name}</p>
            <p>Application Opening Date: {application.opening_date}</p>
            <p>Application Due Date: {application.due_date}</p>
            <p>Status: {application.status}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Calendar;
