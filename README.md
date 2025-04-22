# MapReduce Workflow for Social Media Analytics

## 📁 Project Overview
This project implements a multi-stage MapReduce workflow to analyze large-scale social media data. The system performs data cleansing, user activity aggregation, trending content detection, and joins with user profiles to produce enriched analytics.

## 🗂️ Directory Structure
```
social_media_analytics_mapreduce/
├── input/
│   ├── social_media_logs.txt
│   └── user_profiles.txt
├── mappers/
│   ├── cleanse_mapper.py
│   ├── aggregate_mapper.py
│   ├── trending_mapper.py
│   ├── join_mapper_profiles.py
│   └── join_mapper_activity.py
├── reducers/
│   ├── cleanse_reducer.py
│   ├── aggregate_reducer.py
│   ├── trending_reducer.py
│   └── join_reducer.py
├── output/ (HDFS will generate this)
├── README.md
└── report.pdf / report.docx
```

## 📥 Input Files
- `social_media_logs.txt`: Tab-separated records of user interactions.
- `user_profiles.txt`: Comma-separated user profiles with UserID, Name, and Location.

## 🛠️ How to Run (Hadoop Streaming)
Upload input files to HDFS:
```bash
hdfs dfs -mkdir /data
hdfs dfs -put input/social_media_logs.txt /data/
hdfs dfs -put input/user_profiles.txt /data/
```

### 🧹 Job 1: Data Cleansing
```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
 -input /data/social_media_logs.txt \
 -output /output/cleansed_logs \
 -mapper mappers/cleanse_mapper.py \
 -reducer reducers/cleanse_reducer.py \
 -file mappers/cleanse_mapper.py \
 -file reducers/cleanse_re
