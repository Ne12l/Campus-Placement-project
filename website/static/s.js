// Dummy job data
let jobs = [];

// Function to display jobs
function displayJobs() {
    const jobList = document.getElementById('jobList');
    jobList.innerHTML = '';

    jobs.forEach((job, index) => {
        const jobItem = document.createElement('div');
        jobItem.classList.add('job-item');
        jobItem.innerHTML = `
            <h3>${job.title}</h3>
            <p>${job.description}</p>
            <button onclick="applyForJob(${index})">Apply</button>
        `;
        jobList.appendChild(jobItem);
    });
}

// Function to post a job
document.getElementById('jobForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const jobTitle = document.getElementById('jobTitle').value;
    const jobDescription = document.getElementById('jobDescription').value;

    if (jobTitle && jobDescription) {
        const job = {
            title: jobTitle,
            description: jobDescription,
            applicants: []
        };
        jobs.push(job);
        displayJobs();
        document.getElementById('jobForm').reset();
    } else {
        alert('Please fill out all fields.');
    }
});

// Function to apply for a job
function applyForJob(jobIndex) {
    const fullName = prompt('Enter your full name:');
    if (fullName) {
        const job = jobs[jobIndex];
        job.applicants.push(fullName);
        alert('You have successfully applied for the job.');
        displayJobs();
    }
}

// Initial display of jobs
displayJobs();
