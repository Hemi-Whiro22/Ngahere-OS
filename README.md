# 🌲 Ngahere-OS - Living Forest of Kaitiaki

Ngahere-OS is a living forest system where kaitiaki (guardian birds) serve as AI-powered utilities, each embodying the spirit and purpose of native New Zealand birds. The system is sustained by Tāne Mahuta (the forest god) and powered by the rito (heart of the forest).

## 🐦 Kaitiaki (Native Birds) - Complete Guardian Ecosystem

Each kaitiaki acts as a utility/service in the backend, wrapping functions with the spirit of its role:

### **Core Functionality**
- **🦅 Kea**: Curious trickster — testing, debugging, stress checking, searching
- **🦉 Ruru (Morepork)**: Wisdom in the night — summarisation, memory recall
- **🐦 Kōtare (Sacred Kingfisher)**: Quick strike — embeddings and fast recall
- **🦜 Kākā**: Noisy carver — carving code and patterns into shape
- **🦅 Kārearea (NZ Falcon)**: Sharp sight — OCR scanning of PDFs and images
- **🎶 Tūī**: Voice of the ngahere — text-to-speech, translation, reo flows
- **🐦 Pīwakawaka**: Prompt dancer — zipping around chirping about prompts

### **Security & Protection**
- **🕊️ Kererū**: Gentle auditor — watchful guardian recording every manu's flight
- **🦆 Pūkeko**: Data guardian — territorial protector of data integrity and backups
- **🦅 Kahu**: Security sentinel — sharp-eyed threat detection and monitoring
- **🐦 Tauhou**: Health monitor — keen observation of system health and performance

### **Coordination & Management**
- **🐦 Riroriro**: Communication coordinator — powerful voice for notifications and alerts
- **🐧 Kororā**: Database keeper — reliable navigation of database systems
- **🌲 Korito**: Heart of the forest — holds all environment secrets and sustains the ngahere

## 🏗️ Architecture

```mermaid
graph TD
    TaneMahuta["🌳 Tāne Mahuta — Trunk"] 
    
    %% Core Functionality
    TaneMahuta --> Kea["🦅 Kea — Search"]
    TaneMahuta --> Ruru["🦉 Ruru — Summarise"]
    TaneMahuta --> Kotare["🐦 Kōtare — Embeds"]
    TaneMahuta --> Kaka["🦜 Kākā — Carver"]
    TaneMahuta --> Karearea["🦅 Kārearea — OCR"]
    TaneMahuta --> Tui["🎶 Tūī — Voice"]
    TaneMahuta --> Piwakawaka["🐦 Pīwakawaka — Prompts"]
    
    %% Security & Protection
    TaneMahuta --> Kereru["🕊️ Kererū — Audit"]
    TaneMahuta --> Pukeko["🦆 Pūkeko — Data"]
    TaneMahuta --> Kahu["🦅 Kahu — Security"]
    TaneMahuta --> Tauhou["🐦 Tauhou — Health"]
    
    %% Coordination & Management
    TaneMahuta --> Riroriro["🐦 Riroriro — Communication"]
    TaneMahuta --> Korora["🐧 Kororā — Database"]
    TaneMahuta --> Korito["🌲 Korito — Heart"]
    
    %% Heart connections
    Korito --> TaneMahuta
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Git
- Supabase account (for vector storage)
- OpenAI API key (for AI features)
- Ollama (optional, for local LLM)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Ngahere-OS
   ```

2. **Set up Korito (the heart of the forest)**
   ```bash
   # Copy environment template to Korito's heart
   cp kaitiaki/korito/env.template kaitiaki/korito/.env
   
   # Edit Korito's .env with your API keys
   # SUPABASE_URL=your_supabase_url
   # SUPABASE_KEY=your_supabase_key
   # OPENAI_API_KEY=your_openai_key
   ```
   
   **⚠️ IMPORTANT**: Without Korito's .env file, the ngahere cannot function!

3. **Install dependencies**
   ```bash
   # For development
   ./ngahere_os.sh dev
   
   # Or manually
   pip install -r dev-requirements.txt
   ```

4. **Run the forest**
   ```bash
   ./ngahere_os.sh run
   ```

The API will be available at `http://localhost:8000`

## 📚 API Endpoints - Complete Guardian Ecosystem

### **Core Functionality**
- **Kea** (`/kea`) - Search and testing utilities
- **Ruru** (`/ruru`) - Summarization services  
- **Kākā** (`/kaka`) - Code generation and carving with Cloud Kaitiaki
- **Kōtare** (`/kotare`) - Embedding and vector storage
- **Kārearea** (`/karearea`) - OCR and image scanning
- **Tūī** (`/tui`) - Text-to-speech and voice
- **Pīwakawaka** (`/piwakawaka`) - Prompt dancing and coordination

### **Security & Protection**
- **Kererū** (`/kereru`) - Gentle audit logging and provenance
- **Pūkeko** (`/pukeko`) - Data guardian and backup management
- **Kahu** (`/kahu`) - Security monitoring and threat detection
- **Tauhou** (`/tauhou`) - Health monitoring and system alerts

### **Coordination & Management**
- **Riroriro** (`/riroriro`) - Communication coordination and notifications
- **Kororā** (`/korora`) - Database management and migrations
- **Korito** (`/korito`) - Heart of the forest (environment and secrets)

## 🛠️ Development Status

### ✅ Completed
- **Complete Guardian Ecosystem** (14 kaitiaki)
- **FastAPI application structure** with full routing
- **Korito (Heart of the Forest)** - Centralized environment management
- **Cloud Kaitiaki system** - Flexible AI model provisioning
- **Security & Protection** - Pūkeko, Kahu, Tauhou, Kererū
- **Communication & Coordination** - Riroriro, Pīwakawaka
- **Database Management** - Kororā with schema checking
- **Centralized prompts** in Pīwakawaka
- **Git repository** anchored and organized

### 🚧 In Progress
- **Supabase integration** for Kōtare (embeddings)
- **OCR implementation** for Kārearea (scanning)
- **AI integration** for Ruru (summarization)
- **TTS implementation** for Tūī (voice)
- **Database schema setup** for all kaitiaki tables

### 📋 Roadmap
- **Complete kaitiaki implementations** with full functionality
- **Production deployment** with security hardening
- **Comprehensive testing** across all kaitiaki
- **Documentation and guides** for each guardian
- **Performance optimization** and monitoring
- **Cultural framework expansion** with more Māori concepts

## 🌿 Cultural Framework

This project honors Māori concepts of kaitiakitanga (guardianship) and the interconnectedness of the natural world. Each kaitiaki embodies the characteristics and wisdom of their bird counterparts, creating a culturally-grounded AI system that respects both technology and tradition.

## 📄 License

See LICENSE file for details.
