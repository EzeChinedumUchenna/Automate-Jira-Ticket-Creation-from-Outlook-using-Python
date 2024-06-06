import win32com.client
from jira import JIRA

# Jira server URL and credentials
jira_url = 'https://XXXXXXXXXXX.atlassian.net'
username = 'XXXXXXXXXXXXXXXXx'
api_token = 'XXXXXXXXXXXXXXXXXXXX'

# Initialize the JIRA client
jira = JIRA(server=jira_url, basic_auth=(username, api_token))

# Initialize Outlook and get the namespace
outlook = win32com.client.Dispatch("Outlook.Application")
namespace = outlook.GetNamespace("MAPI")
inbox = namespace.GetDefaultFolder(6)  # "6" refers to the Inbox folder


seen_entry_ids = set()

# Load seen EntryIDs from a file (optional, if you want persistence across runs)
try:
    with open('seen_emails.txt', 'r') as file:
        seen_entry_ids = set(file.read().splitlines())
except FileNotFoundError:
    pass

messages = inbox.Items
messages.Sort("[ReceivedTime]", True)  # to sort messages by ReceivedTime in descending order

for message in messages:
    if "@jira" in message.body.lower():
        if message.EntryID not in seen_entry_ids:
            
            seen_entry_ids.add(message.EntryID)
            
            
            print(f"Subject: {message.Subject}")
            print(f"Body: {message.body}")
            print(f"Creation Time: {message.CreationTime}")
            print(f"sender: {message.SenderEmailAddress}")
            
            # to save the updated seen EntryIDs to a file (optional, for persistence)
            with open('seen_emails.txt', 'a') as file:
                file.write(f"{message.EntryID}\n")
            subject = message.Subject
            body = message.body
            sender = message.SenderEmailAddress
            
            issue_dict = {
                'project': {'key': 'YOUR_PROJCT_KEY'},  # Replace with your project key
                'summary': subject,
                'description': body,
                'issuetype': {'name': 'Task'},
                'assignee': {'name': sender} 
           
            
            }
            new_issue = jira.create_issue(fields=issue_dict)
            print(f"Issue {new_issue.key} created successfully!")
                
            break  
