## AWS - Security Tools

### Perform Log Analysis with Amazon GuardDuty

[Amazon GuardDuty](https://aws.amazon.com/guardduty/) helps you analyze and process data from different data sources such as CloudTrail event logs, [VPC Flow Logs](https://blog.runpanther.io/aws-security-logging-vpc-flow-logs/), and DNS Logs. GuardDuty uses sophisticated machine learning, anomaly detection, and integrated threat intelligence to identify and prioritize potential threats. Additionally, GuardDuty monitors your AWS account for signs of compromised access such as unusual API calls or deployments in a region not used before.

GuardDuty extracts the relevant fields from logs to help you profile and identify anomalies. You can review these findings through your AWS management console, integrate them into event management or workflow systems, or trigger AWS Lambda for automated remediation or prevention.

GuardDuty findings can be aggregated into a single account (controlled by your security team) by issuing invites to all of your member accounts. This approach gives higher visibility into all accounts owned by an organization. [This walkthrough](https://aws.amazon.com/blogs/security/how-to-manage-amazon-guardduty-security-findings-across-multiple-accounts/) demonstrates how to set up this configuration.

GuardDuty findings can be delivered either to an S3 Bucket or CloudWatch Events. Using AWS Lambda Functions, teams can then automate the analysis and notification of any findings from the GuardDuty service.

You can access GuardDuty either via [GuardDuty Console](https://console.aws.amazon.com/guardduty), [AWS SDKs](https://aws.amazon.com/tools/), or [AWS CLI](https://docs.aws.amazon.com/cli/latest/reference/guardduty/index.html).

### Classify and Protect Sensitive Data with Amazon Macie

[Amazon Macie](https://aws.amazon.com/macie/) uses machine learning and user behavior analytics to classify and protect your sensitive data stored in Amazon S3, including PII, PHI, regulatory documents, API keys, and secret keys. It provides dashboards and alerts on what is found and how it is being protected. When alerts are generated, you can use Amazon Macie for incident response using Amazon CloudWatch Events to swiftly take action to safeguard your data. You can also create automated policies to protect your data when suspicious activity is detected.

Amazon Macie works by accessing and identifying a customer’s data in their Amazon S3 bucket. Then, it streams the object contents into memory for analysis. For complex file formats that require deeper analysis, Macie downloads the full copy of the object, but only keeps it till the time required for analysis. Post analysis, Macie deletes the stored content and only retains the metadata required for future analysis.

You can work with Amazon Macie by logging in to the Macie console, running the provided CloudFormation templates to configure the necessary IAM roles and policies in your account, and selecting which S3 buckets to protect.

### Stay Up-To-Date with Amazon Inspector

[Amazon Inspector](https://aws.amazon.com/inspector/) allows you to test and address publicly known software vulnerabilities on EC2 instances in a timely manner, removing them as a potential entry point for unauthorized users. You can basically automate security assessments throughout your development and deployment pipeline or against static production systems.

Inspector offers a pre-defined rules package (host assessment and/or the network reachability) that check for unintended network accessibility and vulnerabilities of your **Amazon EC2 instances**. However, you cannot define your own rules for assessment templates. Amazon Inspector can be fully automated through an API and uses an optional agent. The agent monitors the behavior of the EC2 instances, including network, file system, and process activity. The service generates two types of reports for your assessment- a findings report and a full report.

You can work with the Amazon Inspector service using either the [Amazon Inspector Console](https://console.aws.amazon.com/inspector/) or [AWS SDKs](https://aws.amazon.com/tools/). Inspector integrates with Amazon SNS that notifies for events such as monitoring milestones, failures, or expiration of exceptions. You can also integrate Inspector with AWS CloudTrail for logging calls.

### Get a Single Unified View with AWS SecurityHub

[AWS SecurityHub](https://aws.amazon.com/security-hub) offers a unified view of the severity and sensitivity of findings across the other AWS security services you’re using. These include but are not limited to Amazon GuardDuty, Inspector, Macie, AWS Firewall Manager, and IAM Access Analyzer.

This service takes security findings and normalizes them into Amazon Security Findings Format (or ASFF). After normalizing, it sends them all back out through Amazon CloudWatch events to many AWS partners that are capable of consuming them. With the ASFF format, you can, for instance, write a [Splunk Phantom](https://www.splunk.com/en_us/software/splunk-security-orchestration-and-automation.html) runbook, a [Demisto](https://www.demisto.com/) runbook, a Lambda function, send it to [Rapid7](https://www.rapid7.com/), or cut a ticket in [Jira](https://www.atlassian.com/software/jira).

SecurityHub also lets you create insights into Security Hub. Insights are a collection of findings that are grouped together to identify common security issues that may require remediation action. The following screenshot shows how SecurityHub brings various AWS security services under a single hood

Security Hub is accessible through the [Security Hub console](https://console.aws.amazon.com/securityhub/) when you sign in to the AWS Management Console. You can also use the Security Hub API, which lets you issue HTTPS requests directly to the service. As of June 2019, AWS Security Hub is [generally available](https://aws.amazon.com/about-aws/whats-new/2019/06/aws-security-hub-now-generally-available/).

### Follow Best Practices with AWS TrustedAdvisor

[TrustedAdvisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) is a real-time guidance solution that monitors your AWS infrastructure and compares it to AWS best practices such as identifying security gaps, fault tolerance, and service limits. Post this comparison, it provides recommendations and action links.

The Trusted Advisor notification feature notifies you about your AWS resource deployment. You can track recent changes or check status on the console dashboard. You can also use [AWS Identity and Access Management](https://blog.runpanther.io/serverless-app-repo-intro/) (IAM) to control access to specific checks or check categories. You can also create alerts and automate actions with Amazon CloudWatch. The following screenshot shows how TrustedAdvisor details AWS best practices recommended for your AWS infrastructure

Trusted Advisor is available in the AWS Management Console. All AWS users have access to the data for the [seven core checks](https://aws.amazon.com/premiumsupport/trustedadvisor/). Users with business or enterprise-level support can access [all checks](https://aws.amazon.com/premiumsupport/trustedadvisor/best-practices/).

### Know Your Configurations with AWS Config

[AWS Config](https://aws.amazon.com/config/) allows you to assess, audit, and evaluate the configurations of your AWS resources. It provides you with an AWS resource inventory, configuration history, and configuration change. Config records details of changes to your AWS resources to provide you with a configuration history. It also records software configuration changes within your Amazon EC2 instances and servers running on-premises and those provided by other cloud providers.

Rules in Config are configureable and customizable so you can either use pre-built rules for evaluating provisioning and configuring your AWS resources or you can customize pre-built rules to evaluate your AWS resource configurations. You can also create your own custom rules in AWS Lambda that define your internal best practices and guidelines for resource configurations.

AWS Config also provides Conformance packs where you can package a collection of AWS Config rules and remediation actions into a single entity and deploy it across an entire organization. With conformance packs, you can establish a common baseline for resource configuration policies and best practices across multiple accounts in your organization.

AWS Config integrates with AWS CloudTrail, AWS Systems Manager, Amazon EC2 Dedicated Host, Application Load Balancers and AWS Organizations.
