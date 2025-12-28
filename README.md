# AWS Facial Recognition System

## 📌 Project Overview
This project is a cloud-based facial recognition system developed using AWS services.
It detects and compares human faces from images stored in Amazon S3.

## 🛠️ Technologies Used
- Amazon Rekognition
- AWS Lambda
- Amazon S3
- AWS IAM
- Python
- AWS DynamoDB
- Cloud Shell
- API Gateway

## ⚙️ System Architecture
- User sends an image request through Amazon API Gateway
- API Gateway triggers an AWS Lambda function
- The Lambda function processes the request and accesses Amazon S3
- Image is stored or retrieved from Amazon S3
- AWS Lambda invokes Amazon Rekognition to detect and compare faces
- Recognition results are stored in Amazon DynamoDB
- Final response is returned to the user via API Gateway


## ✨ Features
- Face detection
- Face comparison
- Secure image storage
- Serverless cloud architecture

## 📈 Use Cases
- Attendance systems
- Security and surveillance
- Identity verification systems

## 👩‍💻 Author
Usha Saini  
BTech CSE (Cloud Computing)
