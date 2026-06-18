# TECH_SPEC.md
## Introduction
The wiki-scribe project is an autonomous wiki-building platform designed to generate high-quality, spoiler-free content utilizing Large Language Models (LLMs). The platform aims to simplify the content creation process for solo developers and fan-wiki operators by automating quality control and editing.

## Architecture Overview
The wiki-scribe platform will consist of the following components:

* **LLM Engine**: Responsible for generating content based on user input and preferences.
* **Quality Control Module**: Evaluates generated content for quality, accuracy, and spoiler-free compliance.
* **Editing Module**: Refines and polishes generated content to ensure readability and consistency.
* **User Interface**: Provides an intuitive interface for users to input preferences, review, and publish generated content.
* **Database**: Stores user preferences, generated content, and editing history.

## Components

### LLM Engine
* Utilizes the vLLM (vllm-project/vllm) production inference engine for content generation.
* Integrates with the SGLang (sgl-project/sglang) structured generation language for controlled content output.

### Quality Control Module
* Employs a combination of natural language processing (NLP) and machine learning algorithms to evaluate content quality.
* Utilizes a knowledge graph to identify and flag potential spoilers.

### Editing Module
* Leverages the auto dataset (~12,802,147 pairs across 18 datasets) for language refinement and polishing.
* Incorporates a style guide to ensure consistency in tone, voice, and formatting.

### User Interface
* Built using modern web technologies (HTML, CSS, JavaScript) for a responsive and user-friendly experience.
* Integrates with the LLM Engine and Quality Control Module to provide real-time feedback and content generation.

### Database
* Utilizes a relational database management system (RDBMS) for storing user preferences, generated content, and editing history.
* Designed to scale horizontally to accommodate growing user bases and content volumes.

## Data Model
The wiki-scribe platform will store the following data entities:

* **User Preferences**: Stores user input and preferences for content generation.
* **Generated Content**: Stores generated content, including text, images, and other media.
* **Editing History**: Stores a record of all edits made to generated content, including user feedback and revisions.
* **Knowledge Graph**: Stores a graph of entities, relationships, and concepts used for spoiler detection and content evaluation.

## Key APIs/Interfaces
The wiki-scribe platform will expose the following APIs and interfaces:

* **Content Generation API**: Allows users to input preferences and generate content.
* **Quality Control API**: Evaluates generated content for quality and spoiler-free compliance.
* **Editing API**: Refines and polishes generated content.
* **User Interface API**: Provides an interface for users to review, edit, and publish generated content.

## Tech Stack
The wiki-scribe platform will utilize the following technologies:

* **Frontend**: HTML, CSS, JavaScript
* **Backend**: Node.js, Express.js
* **Database**: PostgreSQL
* **LLM Engine**: vLLM (vllm-project/vllm)
* **SGLang**: SGLang (sgl-project/sglang)

## Dependencies
The wiki-scribe platform will depend on the following libraries and frameworks:

* **vLLM**: vllm-project/vllm
* **SGLang**: sgl-project/sglang
* **auto dataset**: ~12,802,147 pairs across 18 datasets
* **PostgreSQL**: postgresql/pg

## Deployment
The wiki-scribe platform will be deployed on a cloud-based infrastructure, utilizing containerization (Docker) and orchestration (Kubernetes) for scalability and reliability. The platform will be designed to deploy on a variety of cloud providers, including AWS, Google Cloud, and Microsoft Azure.
