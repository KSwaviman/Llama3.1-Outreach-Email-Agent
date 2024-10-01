import pandas as pd
import chromadb
import uuid
import sys


# Define the data
data = {
    'Techstack': [
        'React, Node.js, MongoDB', 'Angular, .NET, SQL Server', 'Vue.js, Ruby on Rails, PostgreSQL',
        'Python, Django, MySQL', 'Java, Spring Boot, Oracle', 'Flutter, Firebase, GraphQL',
        'WordPress, PHP, MySQL', 'Magento, PHP, MySQL', 'React Native, Node.js, MongoDB',
        'iOS, Swift, Core Data', 'Android, Java, Room Persistence', 'Kotlin, Android, Firebase',
        'Android TV, Kotlin, Android NDK', 'iOS, Swift, ARKit', 'Cross-platform, Xamarin, Azure',
        'Backend, Kotlin, Spring Boot', 'Frontend, TypeScript, Angular', 'Full-stack, JavaScript, Express.js',
        'Machine Learning, Python, TensorFlow', 'DevOps, Jenkins, Docker',
        'Excel, Communication, Business Analytics, SEO, Powerpoint' 
    ],
    'Links': [
        'https://example.com/react-portfolio', 'https://example.com/angular-portfolio', 
        'https://example.com/vue-portfolio', 'https://example.com/python-portfolio', 
        'https://example.com/java-portfolio', 'https://example.com/flutter-portfolio', 
        'https://example.com/wordpress-portfolio', 'https://example.com/magento-portfolio', 
        'https://example.com/react-native-portfolio', 'https://example.com/ios-portfolio', 
        'https://example.com/android-portfolio', 'https://example.com/kotlin-android-portfolio', 
        'https://example.com/android-tv-portfolio', 'https://example.com/ios-ar-portfolio', 
        'https://example.com/xamarin-portfolio', 'https://example.com/kotlin-backend-portfolio', 
        'https://example.com/typescript-frontend-portfolio', 'https://example.com/full-stack-js-portfolio', 
        'https://example.com/ml-python-portfolio', 'https://example.com/devops-portfolio',
        'https://example.com/seo-maketing-portfolio'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

client = chromadb.PersistentClient('vectorstore')
collection = client.get_or_create_collection(name="portfolio")

if not collection.count():
    for _, row in df.iterrows():
        collection.add(documents=row["Techstack"],
                       metadatas={"links": row["Links"]},
                       ids=[str(uuid.uuid4())])

class Portfolio:
    def __init__(self, df):
        self.data = df
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        # self.chroma_client = chromadb.Client()
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(documents=row["Techstack"],
                                    metadatas={"links": row["Links"]},
                                    ids=[str(uuid.uuid4())])

    def query_links(self, skills):
        return self.collection.query(query_texts=skills, n_results=2).get('metadatas', [])

