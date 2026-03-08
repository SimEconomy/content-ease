# Installation

## Prerequisites

- Node.js v14 or later
- Git

## Instructions

1. Clone the ContentEase repository from GitHub:
   ```bash
   git clone https://github.com/SimEconomy/content-ease.git
   cd content-ease
   ```

2. Install the required Node.js packages:
   ```bash
   npm install
   ```

3. Set up environment variables in the `.env` file based on the `.env.example`:
   ```bash
   cp .env.example .env
   ```

4. Start the development environment using Docker Compose:
   ```bash
   docker-compose up -d
   ```

5. Verify that the environment is set up correctly by running a basic command, e.g., the server:
   ```bash
   npm run start:dev
   ```
