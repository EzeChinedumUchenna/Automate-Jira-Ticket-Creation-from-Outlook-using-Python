# Introduction

Hello reader! 👋

As a support engineer, you might often face situations where customers reach out to you via Outlook email instead of creating a ticket on Jira. This makes tracking and managing issues cumbersome, as you have to manually create tickets on Jira.
To streamline this process, I developed a Python script that automates the creation of Jira support tickets directly from Outlook emails. This script scans your Outlook inbox for emails containing “@jira” and generates Jira tickets, using the email subject as the ticket summary and the email body as the ticket description. This automation significantly reduces the time spent on manual ticket creation, allowing support teams to focus on resolving issues faster. Simply ensure customers include “@jira” in their email, and the script will automatically create a ticket within 45 seconds.

## Goal
The purpose of this article is to demonstrate how to create a Jira issue from an Outlook email using a Python script. I will guide you through the process of extracting information from an Outlook email and automating the creation of a corresponding issue in Jira, a popular project management tool.

## Implementation Overview
For this project, we will use the win32com.client library to interact with Outlook and the jira library to interact with Jira. Here’s a basic outline of how to implement this:

### 1. Set Up Outlook Integration
First, use win32com.client to access Outlook and read emails. Ensure you have the required libraries installed and your Jira configuration is correct. You can install the libraries using:
```pip install pypiwin32 jira```

### 2. Parse Emails
Extract necessary information from the emails, such as the sender, subject, and body.

### 3. Check for “@jira”
Determine if the email contains “@jira” to identify the emails that need to be converted into Jira tickets.

### 4. Create Jira Ticket
If “@jira” is found, use the jira library to create a ticket in Jira. This step involves setting up your Jira credentials and defining the project details where the ticket should be created.

## Getting a Jira API Token
To get an API token for Jira:

### 1. Log in to your Jira account.
### 2. Navigate to the Atlassian account settings: Click on your profile icon and select “Account settings”.
### 3. Go to the Security tab: Select “API token” from the left sidebar.
### 4. Create a new API token: Click on “Create API token”, give it a label, and click “Create”.
### 5. Copy the API token: Save it securely as you will use it in your script.

## Finding the Project Key
The project key is a unique identifier for your Jira project. You can find it:
### 1. Go to your Jira project: Navigate to the project in Jira.
### 2. Check the URL or project settings: The project key is often visible in the URL (e.g., https://your-domain.atlassian.net/projects/PROJECT_KEY). By default, the project key is “TF”
Result
### 3. To demonstrate the result, I am going to send an email to my inbox with “@jira” in the Body. This script, which runs every 2 seconds, will identify this email and immediately create a ticket on Jira. See the screenshot below:


### Conclusion
By automating the creation of Jira tickets from Outlook emails, this Python script helps support teams save valuable time and focus on resolving issues more efficiently. This article provided an overview of how to set up the integration, parse emails, check for specific keywords, and create Jira tickets automatically.

Feel free to customize the script to suit your specific needs and improve your workflow. Happy coding!
