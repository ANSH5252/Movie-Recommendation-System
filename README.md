# 🎬 Movie Recommendation System

This is a **Content-Based Movie Recommendation System** that suggests movies based on their similarity to other movies using metadata like genres, cast, crew, keywords, and overview. The goal is to provide personalized movie recommendations to users—similar to what platforms like **Netflix** or **Amazon Prime Video** offer.

## 🚀 Features

- Recommends top 5 similar movies based on input.
- Uses Natural Language Processing (NLP) and Machine Learning.
- Converts text data to numerical vectors (Bag of Words model).
- Calculates similarity using **Cosine Similarity**.
- Clean and optimized DataFrame with key features.
- Can be deployed as a web application.



## 📊 Tech Stack

- **Language**: Python 🐍  
- **Libraries**:  
  - `pandas`, `numpy` – data handling  
  - `scikit-learn` – ML tools  
  - `nltk` – natural language processing  
  - `ast` – safely parsing stringified lists
  - `streamlit` - for running the app in your local server  
  - `TMDB API` - to fetch the movie_poster
  - `pickle` - To read and write the binary files
- **Model**: Content-Based Filtering  
- **Vectorizer**: CountVectorizer (Bag of Words)  
- **Similarity Metric**: Cosine Similarity



## 📂 Project Structure
```
Movie-Recommendation-System/
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── movie_dict.pkl
├── similarity.pkl
├── requirements.txt
├── .env
├── .gitignore
├── m_r_s.ipynb
├── app.py
└── README.md
```

## 📥 How to Run

**1. Clone the Repository**
   ```bash
   git clone https://github.com/ANSH5252/Movie-Recommendation-System.git
   ```
  - Change Directory to Movie-Recommendation-System
   ```
   cd Movie-Recommendation-System
   ```
**2. Install Dependencies**  
  - Make sure you have Python 3.x installed. Then run:
   ```
   pip install -r requirements.txt
   ```
**3. Download Dataset**  
 -  Place `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` in the root folder (already present in this repo).

**4. Run the `m_r_s.ipynb file`**  
- After running all the cells in the `Jupyter Notebook`, it creates Two `Binary Files` in the `Current Working Directory` with the names:
```
• movie_dict.pkl  
• similarity.pkl
```
**5. Create your `TMDB API Key`**  
- Click here https://www.themoviedb.org to navigate to TMDB's official website and create your account if it does not exist. After that request for an `API Key`, copy it and navigate back to your `Current Working Directory` and create a new file and name it `.env`. Inside the .env file write :
```
your_api_key = <paste_your_api_key>
```
**6. Run it in your local server**
- Open the terminal in your VS Code and type :
```
streamlit run app.py
```

## 🧠 How It Works

**1. Load & Merge Data**  
  
  - Merges `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` on the title column.  

**2. Preprocess Features**

  - Extracts useful columns: `genres`, `keywords`, `cast`, `crew`, `overview`

- Converts stringified lists into usable Python lists

  - Retains top 3 cast members and director

  - Combines all relevant text into a new column called `tags`

**3. Text Normalization with NLP**

- Uses `PorterStemmer` from `nltk` to stem similar words (e.g., "love", "loving" →"love")  
- Cleans and converts the combined `tags` text into lowercase, space-separated strings

**4. Vectorization with CountVectorizer**

- Encodes the text into numeric vectors using Bag of Words  
- Limits vocabulary to top 5000 words and removes stop words

**5. Cosine Similarity Calculation**

- Computes cosine similarity matrix (4806 x 4806)  
- Identifies the top 5 most similar movies based on cosine score



## 🧪 Example Usage
```
recommend('Iron Man')
```
**Output:**
```
•  Iron Man 2

•  Avengers: Age of Ultron

•  Captain America: Civil War

•  The Avengers

•  Iron Man 3
```

## 📸 Screenshots 

![Image-3](https://github.com/user-attachments/assets/bc7ac367-7e7b-451b-b829-fc34b74ba76f)
![Image-2](https://github.com/user-attachments/assets/26ab01ba-4543-4dd9-9b5d-2d4db085b45c)
![Image-1](https://github.com/user-attachments/assets/a3f0bed9-9e4f-4f21-9af7-2316cb2e33d6)

## 🤝 Contributing  

Feel free to fork this repo, raise issues, or submit pull requests.


## 📄 License
This project is licensed under the MIT License.

## 🙋‍♂️ Author
Anshuman Dash  
[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?logo=github)](https://github.com/ANSH5252)
