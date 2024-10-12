import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#loading the data
df = pd.read_csv('archive\\postings.csv')

df['Job_Info'] = df['title'].fillna('') + ' ' + df['description'].fillna('') + ' ' + df['skills_desc'].fillna('')

def recommend_jobs(user_skills, num_recommendations=3):
    #convert text to numeric vectors
    vectorizer = TfidfVectorizer(stop_words='english')
    job_vectors = vectorizer.fit_transform(df['Job_Info'])

    #convert the user's skills into the same vectorized form
    user_skills = [user_skills]
    user_vector = vectorizer.transform(user_skills)
    
    #cosine similarity between the user's skills and job descriptions
    similarity_scores = cosine_similarity(user_vector, job_vectors)

    # Get the top job recommendations based on similarity scores
    top_indices = similarity_scores.argsort()[0][-num_recommendations:][::-1]
    
    # Fetch the job details of the recommended jobs
    recommendations = df.iloc[top_indices][['title', 'company_name']]
    
    # Print the recommended jobs in a more readable format
    print(f"\nBased on your skills, the top {num_recommendations} recommended jobs are:\n")
    
    for idx, row in recommendations.iterrows():
        print(f"Job Title   : {row['title']}")
        print(f"Company     : {row['company_name']}")
        print("-" * 40)  # Separator line for readability

# Test the recommendation system
user_skills = "Python, SQL"
recommended_jobs = recommend_jobs(user_skills)

