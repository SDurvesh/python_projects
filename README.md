# python_projects

# Weather Forecasting Application

This is a simple web application that allows users to get the current weather information for a given city. The application is built using Flask and fetches weather data from the OpenWeatherMap API.

## Features

- Enter a city name to get the current temperature and weather description.
- Temperature is displayed in Celsius.
- The application is hosted on an AWS EC2 instance and served using Nginx.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have an AWS account and an EC2 instance running Ubuntu Server.
- You have SSH access to your EC2 instance.
- You have the necessary permissions to install software on the EC2 instance.
- Expose port from inbound permissions to ensure proper hosting
- generate your API_Key from openweatherMap.org

## Installation

Follow these steps to set up the project on your AWS EC2 instance:

### Step 1: Launch an EC2 Instance

1. Go to the AWS Management Console.
2. Launch a new EC2 instance using the Ubuntu Server 22.04 LTS AMI.
3. Choose an instance type (e.g., t2.micro for free tier).
4. Configure the instance details, add storage, and configure the security group to allow HTTP (port 80) and SSH (port 22).
5. Launch the instance and connect to it using SSH.

### Step 2: Install Required Software

1. Connect to your EC2 instance using SSH:
    incase of different terminal implement
    ```bash
    ssh -i your-key.pem ubuntu@your-ec2-public-ip
    ```

2. Update the package list and install necessary packages:

    ```bash
    sudo apt update
    sudo apt install python3-pip python3-venv nginx
    ```

### Step 3: Set Up Your Flask Application

1. Create a directory for your project:

    ```bash
    mkdir ~/python_project
    cd ~/python_project
    ```

2. Create a virtual environment and activate it:
    this step is necessary for flask installation

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install Flask and requests inside the virtual environment:

    ```bash
    pip install Flask requests
    ```

### Step 4: Deploy the Application

1. Create your Flask application and HTML templates (screenshots will be added in the repository to show the structure and contents).
2. Run the Flask application to verify it works:

    ```bash
    python weather.py
    ```
### Step 5: Access the Application

1. Open your web browser and go to `http://your-ec2-public-ip` to access the weather forecasting application.

## Screenshots

- **Project Structure**: A screenshot showing the directory structure of the project.
![image](https://github.com/user-attachments/assets/ff6a590d-dd65-4806-9a4e-3232be1a6b63)
- **Flask Application**: A screenshot of the Flask application code.
![image](https://github.com/user-attachments/assets/e3307a51-4317-4573-bcda-96c7145863af)
- **HTML Template**: A screenshot of the HTML template code.
![image](https://github.com/user-attachments/assets/23292e4f-e7ba-40c2-9a35-6843100bb8f0)
- **Application Running**: A screenshot of the application running in a web browser.
![image](https://github.com/user-attachments/assets/2148ddf0-cba4-4240-b3ba-f7404e734211)
![image](https://github.com/user-attachments/assets/442ad6d4-2b5b-46af-8fd8-8fabf4c3dffa)


## Conclusion

This project demonstrates a simple yet effective way to create a weather forecasting application using Flask and deploy it on an AWS EC2 instance. It showcases the use of web frameworks, API integration, and cloud deployment.

Feel free to customize this README file further based on your specific needs and the structure of your project.
