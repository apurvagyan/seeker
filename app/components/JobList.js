// components/JobList.js

import React from 'react';

const JobList = ({ companies }) => {
  return (
    <div>
      {companies.map(company => (
        <div key={company.id}>
          <h2>{company.name}</h2>
          <p>{company.description}</p>
          <ul>
            {company.jobs.map(job => (
              <li key={job.id}>
                <h3>{job.title}</h3>
                <p>{job.description}</p>
                <p>Start Date: {job.start_date}</p>
                <p>End Date: {job.end_date}</p>
              </li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
};

export default JobList;
