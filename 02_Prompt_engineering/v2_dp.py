PRODUCT_CONFIGS = {
    "saas_crm": {
        "product_name": "CRM Platform",
        "categories": ["Billing", "Technical", "Feature Request", "Spam", "Other"],
        "urgency_levels": ["High", "Medium", "Low"],
        "sla_hours": {"High": 2, "Medium": 8, "Low": 24},
        "examples": [
            {"subject": "SFDC not syncing", "body": "Salesforce stopped pulling leads",
             "output": {"category": "Technical", "urgency": "High"}}
        ]
    },
    "fintech_payments": {
        "product_name": "Payment Gateway",
        "categories": ["Transaction Failed", "Fraud Alert", "Settlement Delay", "KYC Issue", "Other"],
        "urgency_levels": ["Critical", "High", "Medium"],
        "sla_hours": {"Critical": 1, "High": 4, "Medium": 12},
        "examples": [
            {"subject": "Payment declined at checkout", "body": "Card declined even though sufficient balance",
             "output": {"category": "Transaction Failed", "urgency": "High"}}
        ]
    },
     "xyz": {
        "product_name": "CRM Platform",
        "categories": ["Billing", "Technical", "Feature Request", "Spam", "Other"],
        "urgency_levels": ["High", "Medium", "Low"],
        "sla_hours": {"High": 2, "Medium": 8, "Low": 24},
        "examples": [
            {"subject": "SFDC not syncing", "body": "Salesforce stopped pulling leads",
             "output": {"category": "Technical", "urgency": "High"}}
        ]
    }
}

import json
with open('data/test_emails.json') as f:
    emails = json.load(f)

email = emails[0]


# step 2 : lets load the prompts
with open('prompts/d_p.md') as f:
    template = f.read()

print(PRODUCT_CONFIGS["saas_crm"]["categories"])
categories = ', '.join(PRODUCT_CONFIGS["saas_crm"]["categories"])
prompt = template.format(
    PRODUCT_CONFIGS["saas_crm"]['product_name'],categories,'Tx failure',"I am not able to pay my emi"
)

from model_setup import call_llm,cleaning
output = call_llm(prompt)
print(output)