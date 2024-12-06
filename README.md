<h1 id="netflix-titles-recommender-system---mongodb-implementation">Netflix Titles Recommender System - MongoDB Implementation</h1>
<p>This repository contains the implementation of a scalable movie and TV show recommender system using the Netflix Titles dataset from Kaggle. The project leverages <strong>MongoDB</strong> for data storage and <strong>Python</strong> for data import, analysis, and query execution. The repository includes scripts for dataset import, query performance analysis, and dataset size analysis.</p>
<hr>
<h2 id="features">Features</h2>
<ul>
<li><strong>Dataset Overview</strong>:<ul>
<li>Contains metadata for movies and TV shows, user profiles, and user interactions.</li>
<li><strong>3 collections</strong> in MongoDB:<ul>
<li><code>movies&amp;shows</code>: Metadata about movies and TV shows.</li>
<li><code>users</code>: Simulated user profiles with preferences.</li>
<li><code>interactions</code>: User interactions, including ratings and reviews.</li>
</ul>
</li>
</ul>
</li>
<li><strong>Data Handling</strong>:<ul>
<li>Data imported from CSV and enriched with simulated user and interaction data.</li>
<li>Collections structured for efficient query execution.</li>
</ul>
</li>
<li><strong>Query Execution and Analysis</strong>:<ul>
<li>24 MongoDB queries for various scenarios (e.g., filtering, aggregations, recommendations).</li>
<li>Scripts to evaluate query performance and measure dataset memory usage.</li>
</ul>
</li>
</ul>
<hr>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before running any scripts, ensure you have the following:</p>
<ol>
<li><p><strong>Python 3.8+</strong> installed.</p>
</li>
<li><p><strong>MongoDB Atlas</strong> connection or a local MongoDB instance.</p>
</li>
<li><p>Required Python libraries:</p>
<pre><code class="language-bash">pip install pymongo
</code></pre>
</li>
<li><p>   Update the config.json file with your MongoDB connection string:</p>
<pre><code class="language-bash">{
 &quot;MONGODB_URI&quot;: &quot;your_mongodb_connection_string&quot;
 }
</code></pre>
</li>
</ol>
<h2 id="repository-structure">Repository Structure</h2>
<pre><code class="language-bash">├── config.json                  # Configuration file for MongoDB URI
├── dataset_analysis.py          # Script to analyze dataset size and memory usage
├── import_data.py               # Script to import data into MongoDB
├── query_performance.py         # Script to execute and log query performance
├── netflix_titles.csv           # Dataset (source for movies and shows)
├── mongodb_query_performance.txt# Output file for query performance results
├── dataset_analysis.txt         # Output file for dataset analysis results
├── README.md                    # Project documentation
</code></pre>
<h2 id="running-the-scripts">Running the scripts</h2>
<ol>
<li><p>Import Data (import_data.py)</p>
<p>This script reads the Netflix Titles dataset, simulates user profiles and interactions, and imports them into the MongoDB database.</p>
<p>Steps to Run:</p>
<ol>
<li>   Place the netflix_titles.csv file in the root directory.</li>
<li>   Run the script:</li>
</ol>
</li>
</ol>
<pre><code class="language-bash">python import_data.py
</code></pre>
<ol start="2">
<li><p>Query Performance Analysis (query_performance.py)</p>
<p>This script executes predefined MongoDB queries and logs their performance metrics, including execution time, result counts, and sample results.</p>
<p>Steps to Run:</p>
<ol>
<li>   Run the script:</li>
</ol>
</li>
</ol>
<pre><code class="language-bash">  python query_performance.py
</code></pre>
<ol start="3">
<li><p>Dataset Size Analysis (dataset_analysis.py)</p>
<p>This script analyzes the size and memory footprint of the collections in MongoDB.</p>
<p>Steps to Run:</p>
<ol>
<li>   Run the script:</li>
</ol>
</li>
</ol>
<pre><code class="language-bash">python dataset_analysis.py
</code></pre>


