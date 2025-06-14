# Cyberbullying_tweets

# NLP Data Processing Pipeline

##  Overview
A complete ETL pipeline for processing cyberbullying text data with NLP enrichment, storing in MongoDB, and indexing in Elasticsearch.

##  Prerequisites
- Python 3.8+
- MongoDB 5.0+
- Elasticsearch 7.0+
- Required packages:
  ```bash
  pip install pymongo elasticsearch pandas langdetect textblob nltk beautifulsoup4
  ```

## File Structure
```
.
├── scripts/
│   ├── scraper.py          # CSV to Mongo 
│   ├── preprocessing.py    # Text cleaning
│   ├── preprocess_mongo.py # MongoDB text 
│   ├── nlp_pipeline.py     # Language & sentiment analysis
│   └── es_ingest.py       
│   ├── test_scraper.py
│   ├── test_preprocessing.py
│   └── test_nlp_pipeline.py
└── requirements.txt
```

## Pipeline Workflow
1. **Extract**: `scraper.py` loads CSV data
2. **Transform**: 
   - `preprocess_mongo.py` cleans text
   - `nlp_pipeline.py` adds NLP features
3. **Load**: `es_ingest.py` migrates to Elasticsearch

## Quick Start
```bash
# 1. Load sample data (update CSV path in scraper.py)
python scripts/scraper.py

# 2. Clean text data
python scripts/preprocess_mongo.py

# 3. Add NLP features
python scripts/nlp_pipeline.py

# 4. Index in Elasticsearch
python scripts/es_ingest.py
```

## Configuration
| Script               | Default Values                     |
|----------------------|------------------------------------|
| `scraper.py`         | MongoDB URI: `mongodb://localhost:27017/` |
| `preprocess_mongo.py`| DB: `harcelement`, Collection: `posts` |
| `nlp_pipeline.py`    | Sentiment thresholds: ±0.1         |
| `es_ingest.py`       | ES Host: `http://localhost:9200`   |

##  Customization
Override defaults by modifying:
```python
# Example for es_ingest.py
migrate_to_elasticsearch(
    mongo_uri="your_uri",
    es_host="your_es_host",
    index_name="custom_index"
)
```

##  Testing
```bash
python -m unittest discover -s tests
```

## NLP Features
- **Language Detection**: Using `langdetect`
- **Sentiment Analysis**: 
  - Positive (>0.1)
  - Neutral (-0.1 to 0.1)  
  - Negative (<-0.1)
- **Text Cleaning**:
  ```python
  "HELLO! Visit https://test.com " → "hello visit"
  ```

## Sample Data Flow
| Field          | Source        | Example Value          |
|----------------|---------------|------------------------|
| `Text`         | Original CSV  | "U R SO UGLY!! "     |
| `cleaned_text` | preprocessing | "ugly"                |
| `language`     | NLP Pipeline  | "en"                  |
| `sentiment`    | NLP Pipeline  | "negative"            |

##  Notes
1. Requires NLTK data downloads:
   ```python
   import nltk
   nltk.download('stopwords')
   nltk.download('wordnet')
   ```
2. Elasticsearch index gets recreated on each run
3. MongoDB collection gets cleared before new inserts

##  License
MIT
``` 

This README includes:
- Clear installation/usage instructions
- Visual workflow diagram
- Configuration reference table
- Data transformation examples
- Testing instructions
- Customization options
- File structure overview
- Important notes about system behavior

The markdown formatting uses:
- Emojis for visual scanning
- Code blocks for commands
- Tables for configuration/data examples
- Clear section headers
- Consistent indentation
