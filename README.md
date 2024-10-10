# Food Delivery Full Stack Application
[![Docker](https://img.shields.io/badge/docker-Enabled-blue)](https://www.docker.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Enabled-316192.svg)](https://www.postgresql.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Enabled-009688.svg)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-Enabled-61DAFB.svg)](https://reactjs.org/)

## Overview

This **Full Stack Food Delivery Application** is designed to streamline the process of ordering food from restaurants. The platform uses a modern technology stack to deliver an efficient and secure experience for both customers and restaurant managers.

The project is built with the following key technologies:

- **Docker**: To containerize the application, making it easy to deploy and manage.
- **PostgreSQL**: As the database system, handling all relational data management needs.
- **FastAPI**: A high-performance backend framework, providing APIs for managing food orders, users, and restaurant data.
- **Python**: The core programming language for the backend, used alongside FastAPI for logic processing.
- **React**: A powerful frontend library, delivering a dynamic and responsive user interface.

## Features

- **JWT Authentication**: Implemented to ensure secure access to the platform, with token-based authentication protecting user data.
- **Restaurant Management**: Manage menus, orders, and customer information in real-time.
- **User-Friendly Interface**: A React-powered frontend that offers a seamless experience for both users and restaurant owners.
  
This project is designed with the aim of becoming a **complete food delivery application**, optimizing the services provided by restaurants and enhancing the user experience.

##  Future Improvements

- **Payment Integration**: Integrate with payment gateways to handle transactions.
- **Real-time Order Tracking**: Implement WebSocket functionality to track orders in real-time.

## Getting Started

### Prerequisites

To run this application locally, ensure you have the following installed:

- [Docker](https://www.docker.com/)
- [Git](https://git-scm.com/)
- [Python 3.x](https://www.python.org/)
- [Node.js](https://nodejs.org/)

### Installation

**Clone the repository**:
   ```bash
   git clone https://github.com/gbr-azv/Python-React-Docker-App.git
   cd Python-React-Docker-App
   ```

**Set up the environment variables**:

```bash
Create a .env file in the project root, configuring it with your environment-specific 
values, such as database credentials and JWT secrets.
```

**Run The Application**:
   ```bash
   docker-compose up --build
   ```
