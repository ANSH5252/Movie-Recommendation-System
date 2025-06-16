# Movie-Recommendation-System <br>

This is a content based movie recommendation system. It recommends the movies based on it's similarity with the other movies in the database. 
Example - Netflix uses Movie Recommendation system to recommend movies to their users based on the type of movie they watch.
Machine Learning is used build this recommendation system. It includes several steps which are listed below :-<br>
<br>
STEP-1 : Loading the data into a Pandas Dataframe.<br>
STEP-2 : Data preprocessing.<br>
STEP-3 : Model Building to recommend movies.<br>
Step-4 : Convert it into a Website.<br>
STEP-5 : Deployment of the Product.<br>

## Step 1: Loading the data into a Pandas Dataframe 
The data is loaded into a Pandas Dataframe from a CSV file. There are two CSV files,i.e.,"tmdb_5000_movies.csv" and "tmdb_5000_credits.csv" which are separately stored into two pandas dataframes movies and credits respectively.The first CSV file contains information about the movies such as title, genre, director, release year, etc while the second CSV file contains only four colums,i.e. ,movie_id, title, cast and crew. Both the dataframes are merged into one on title column. <br>

## Step 2: Data Preprocessing 
Since, there are 23 columns in total we need to filter out only those features which are important for the building of a recommendation system. Taking a look at the data we can point out the features required for our recommendation system which are listed as follows :-<br>
<br>
1 -> genres (Important because it helps to recommend similar content)<br>
2 -> id (Important for fetching the posters of the movies)<br>
3 -> keywaords (Important to generate tags which results in better recommendation)<br>
4 -> title (Important to Recommend the movie_name)<br>
5 -> overview (Important to calculate the similarity between two movies)<br>
6 -> cast (Important to recommend the movies based on the cast people like)<br>
7 -> crew (Important to recommend the movies based on the director of the movie)<br>

Now the new Dataframe consists of 7 columns. The next step is to create a Dataframe which consists of only three columns,i.e., "id" , "title" and "tags". The tags column is a mixture of the columns overview , generes , keywords , cast and crew. But firstly we need to check for missing values and handle them.

### Cleaning of Genres Feature<br>
The genre feature consists of list of dictionaries and has the genres as string. Therefore, we need to extract it in the form of list for which the ast module of python is quite helpful. The ast module consists of literal_eval method which can be used to safely evaluate a string containing a Python literal structure. It's main purpose is to safely evaluate strings containing Python literals or containers of Python literals. After which the dataframe is updated with the new genres feature.<br>
### Cleaning of Keywords Feature<br>
The keywords feature was cleaned using the same approach as the genres feature.<br>
### Cleaning of Cast Feature<br>
The cast feature was cleaned using the same feature and only the top 3 actors/actresses were kept for each movie to select from.<br>
### Cleaning of Crew Feature<br>
The crew feature was cleaned and the Director name was fetched from the crew and stored successfully in the Crew column in the form of list.<br>
### Cleaning of Overview Feature<br>
The overview feature was converted into a list to perform furthur operations.<br>
## Final Dataframe<br>
The Final Dataframe consists of only 3 columns with the id , title and tags. The tags column is a mixture of the columns overview , generes , cast and crew.

The system uses the concept of cosine similarity to find the similarity between the movies.