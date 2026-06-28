```markdown
# Dataflow Architecture

## External Data Sources
- **Wiki Content APIs**: APIs from existing wikis (e.g., Fandom, Wikia) for initial content seeding.
- **User-Generated Content**: Direct user inputs via web interface or API.
- **Third-Party Data Sources**: APIs for additional reference data (e.g., movie databases, game databases).

## Ingestion Layer
- **API Gateways**: RESTful APIs for receiving user-generated content and external data.
- **Webhooks**: For real-time updates from external data sources.
- **Batch Ingestion**: Scheduled jobs for pulling data from external APIs.

## Processing/Transform Layer
- **Content Parsing Module**: Parses and cleans incoming content.
- **LLM Integration**: Utilizes LLMs to generate spoiler-free content and perform initial quality checks.
- **Content Moderation Module**: Automated moderation for quality control.
- **Editing Automation**: Automates editing tasks based on predefined rules and LLM outputs.

## Storage Tier
- **Content Database**: Stores raw and processed wiki content (e.g., PostgreSQL).
- **User Data Database**: Stores user information and authentication data (e.g., PostgreSQL).
- **Cache Layer**: Redis for caching frequently accessed content and user sessions.

## Query/Serving Layer
- **Content Delivery Network (CDN)**: For fast delivery of static content.
- **API Servers**: Serves processed content to users via RESTful APIs.
- **Web Interface**: Frontend application for user interaction.

## Egress to User
- **Web Application**: Main interface for users to interact with the wiki.
- **Mobile Application**: Optional mobile app for on-the-go access.
- **API Access**: For third-party integrations and custom applications.

## ASCII Block Diagram
```
+---------------------+     +---------------------+     +---------------------+
| External Data       |     | Ingestion Layer     |     | Processing/Transform|
| Sources             |<--->|                     |<--->| Layer               |
| - Wiki Content APIs |     | - API Gateways      |     | - Content Parsing   |
| - User-Generated    |     | - Webhooks          |     | - LLM Integration   |
| - Third-Party Data  |     | - Batch Ingestion   |     | - Content Moderation|
+---------------------+     +---------------------+     | - Editing Automation|
                                                     +---------------------+
                                                     v
+---------------------+     +---------------------+     +---------------------+
| Storage Tier        |     | Query/Serving Layer |     | Egress to User      |
| - Content DB        |<--->| - CDN               |<--->| - Web Application   |
| - User Data DB      |     | - API Servers       |     | - Mobile Application|
| - Cache Layer       |     | - Web Interface     |     | - API Access        |
+---------------------+     +---------------------+     +---------------------+
```

## Auth Boundaries
- **User Authentication**: OAuth 2.0 for user authentication and authorization.
- **API Authentication**: API keys for third-party integrations.
- **Data Encryption**: TLS for data in transit and encryption at rest for sensitive data.
```