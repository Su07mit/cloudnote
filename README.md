☁️ CloudNote — Cloud-Based Note Management Web Application
<img width="1470" height="956" alt="image" src="https://github.com/user-attachments/assets/b3650560-9bdb-4935-b03d-98050acfb694" />


A fully cloud-hosted note management web application built on Amazon Web Services (AWS). Create, organise, search, pin and back up notes from anywhere in the world.

🌐 Live Demo: http://44.204.186.51:5002

📸 Screenshots

Light Mode
<img width="1466" height="928" alt="image" src="https://github.com/user-attachments/assets/93f01425-f168-44ef-8bbd-1a0f99e94f77" />

Dark Mode
<img width="1467" height="954" alt="image" src="https://github.com/user-attachments/assets/af84b705-10be-44a8-ace0-f5b4f1e2e7f9" />


✨ Features
FeatureDescription✏️ Create NotesAdd notes with category, auto timestamp📌 Pin NotesPin important notes to the top✏️ Edit NotesInline editing without page reload🗑️ Delete NotesRemove notes with confirmation prompt🔍 Instant SearchReal-time search with zero page reload🏷️ CategoriesOrganise notes by Work, Personal, Ideas, General☁️ S3 BackupOne-click backup of all notes to AWS S3📊 Stats DashboardTotal notes, pinned count, category breakdown🌙 Dark/Light ModeToggle theme with local persistence📝 Word CounterReal-time character and word count while typing📊 Progress BarsVisual category distribution chart🔔 Toast NotificationsNon-intrusive success/error messages📱 Responsive DesignWorks on desktop and mobile browsers

☁️ AWS Cloud Architecture
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Amazon EC2  │────▶│  DynamoDB   │     │  Amazon S3  │     │  AWS IAM   │
│  t3.micro   │     │  Notes Table│     │   Backups   │     │  Security  │
│  Ubuntu 26  │◀────│  NoSQL DB   │     │  JSON Files │     │  Policies  │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
       │                                       ▲
       │                                       │
       └───────────────────────────────────────┘
                    S3 Backup on demand
AWS ServicePurposeTypeAmazon EC2Hosts the Flask web application (t3.micro, Ubuntu)IaaSAmazon DynamoDBNoSQL database for storing all note recordsDBaaSAmazon S3Object storage for JSON note backup filesStorageAWS IAMIdentity access management & security policiesSecurity

💰 Cost Analysis
ServiceMonthly CostAmazon EC2 (t3.micro)$7.59Amazon DynamoDB$0.56Amazon S3$0.02Data Transfer$0.09AWS IAM$0.00Total$8.26 / month

💡 97% cheaper than equivalent on-premise infrastructure (~$200/month)


🛠️ Tech Stack

Backend: Python 3, Flask
Database: AWS DynamoDB (boto3 SDK)
Storage: AWS S3
Frontend: HTML5, CSS3, JavaScript (vanilla)
Hosting: AWS EC2 (Ubuntu 26.04 LTS)
Process Manager: systemd (auto-restart on reboot)


🚀 Getting Started
Prerequisites

Python 3.x
AWS Account with DynamoDB and S3 access
AWS IAM user with access keys

Installation

Clone the repository

bashgit clone https://github.com/Su07mit/cloudnote.git
cd cloudnote

Install dependencies

bashpip3 install flask boto3

Configure AWS credentials in app.py

pythonAWS_REGION = 'us-east-1'
AWS_ACCESS_KEY = 'your-access-key'
AWS_SECRET_KEY = 'your-secret-key'
S3_BUCKET = 'your-s3-bucket-name'

Create DynamoDB table


Table name: Notes
Partition key: id (String)


Run the application

bashpython3 app.py

Open in browser

http://localhost:5002

📁 Project Structure
cloudnote/
│
├── app.py                 # Flask application & AWS integration
├── templates/
│   └── home.html          # Frontend UI (HTML, CSS, JS)
└── README.md              # Project documentation

🔒 Security Notes

Never commit AWS credentials to GitHub
Use IAM users with least privilege access
Rotate access keys regularly
Use environment variables for credentials in production


🚀 Future Enhancements

 AWS Cognito — multi-user authentication
 CloudWatch — monitoring and alerting
 CloudFront CDN — global performance
 EC2 Auto Scaling — traffic management
 Mobile app via AWS Amplify
 Rich text editor support
 Note sharing and collaboration


👨‍💻 Developer
Sumit Kafle — @Su07mit

📚 Academic Context

This project was developed as part of ICT723 — Virtualisation and Cloud Computing
King's Own Institute (KOI) | T1 2026
Group Assessment — Cloud Application Development


📄 License
This project is for academic purposes only.
