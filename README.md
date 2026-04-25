TechPulse Archiver - Automated News Data Engineering

The TechPulse Archiver is an autonomous Python-based microservice that aggregates technology news from Hacker News and archives them into a structured Excel database daily. The goal of the project is to demonstrate a scalable data collector workflow without any human interaction.


Features:

Web Scraping: Automated data extraction using BeautifulSoup4 and Requests libraries
Intelligent datahandling: Data processing and removing duplicates by using Pandas
Persistent Storage: Long-term storage in Excel
Autonomous Scheduling: Embedded scheduler mechanism, which starts the script daily at 9:00 AM
Always-on Architecture: Dockerized executability (```restart: always``` policy)

Tech Stack:

Language: Python
Data Processing: Pandas
Scraping: BeautifulSoup4
Scheduling: Schedule library
Environment: Docker és Docker Compose (timezone synchronized)


Quick Start:
1. Clone the Repository
git clone https://github.com/username/techpulse-archiver.git cd techpulse-archiver

3. Start
docker compose up -d

Development Process & Challenges:
Data consistency and duplication: The biggest challenge was to handle the duplicate news. I used the ```drop_duplicates``` function on the titles of the news to solve the problem. This way the archive contains only unique posts regardless of how many days a news item is on the front page.

Bypassing bot protection: Many websites block the script-based requests. I implemented a dedicated User-Agent header that simulates a modern web browser guarenteeing undisturbed datascraping.

Docker timezone handling: The container environment uses the default timezone which could cause timing shifts. Therefore, I implemented the ```TZ=Europe/Budapest``` environment variable in the Dockerfile so the scheduling occurs exactly at 09:00 AM local time.

Structure:
.
├── main.py                     # Main logic
├── tech_hirek_archivum.xlsx    # Automatically generated database
├── Dockerfile                  # Container definition (with timezone config)
├── docker-compose.yml          # Orchestration (Volumes & Restart policy)
└── requirements.txt            # Project Dependencies

Created by: Molnár Gergő - https://www.linkedin.com/in/gerg%C5%91-moln%C3%A1r-3920b53a7/
