# Job Recommender System

## Project Overview
This is a Python-based Job Recommender System that suggests relevant job postings based on a user's skill set. The system uses text vectorization and cosine similarity to match user-provided skills with job descriptions from the dataset.

## Dataset
The dataset used for this project contains LinkedIn job postings and is available on Kaggle.

**Dataset link:** [LinkedIn Job Postings](https://www.kaggle.com/datasets/arshkon/linkedin-job-postings)

The dataset includes the following key features:
- `job_id`: Unique ID for each job
- `company_name`: Name of the company
- `title`: Job title
- `description`: Detailed job description
- `min_salary`, `med_salary`, `max_salary`: Salary range for the job
- `skills_desc`: Job requirements and desired skills
- And more...

## Features
- **Skill-Based Recommendation**: Users input their skills, and the system finds matching jobs based on the job descriptions.
- **Text Vectorization**: The job descriptions are vectorized using TF-IDF to analyze the similarity between user skills and job requirements.
- **Cosine Similarity**: The similarity between user input and job descriptions is measured to recommend the best-fit jobs.

## How to Run
1. Clone the repository:
    ```bash
    git clone https://github.com/unusualmold2003/job-recommender.git
    cd job-recommender
    ```
2. Install the required Python packages:
    ```bash
    pip install --upgrade scikit-learn

    pip install --upgrade pandas
    ```
3. Import the dataset from Kaggle and place it in the project folder.
    - [LinkedIn Job Postings Dataset](https://www.kaggle.com/datasets/arshkon/linkedin-job-postings)
4. Run the script:
    ```bash
    python main.py
    ```

## Example Output
```bash
Based on your skills, the recommended jobs are:
-------------------------------------------------
Job Title: Data Scientist
Company: XYZ Inc.
Location: Remote
Skills Required: Python, Machine Learning, TensorFlow

Job Title: Software Engineer
Company: ABC Corp.
Location: New York, NY
Skills Required: Python, Java, SQL
