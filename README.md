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
