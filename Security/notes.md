## Security Concepts

Well, the first step in solving a problem is recognizing that there is one. The second most effective step is ensuring that you understand what needs to be solved or, in other words, what is the problem? And if you are presented with questions for which there may be multiple answers (or multiple choices, as in your certification exam), a good starting point is to eliminate all those options that do not apply. In an attempt to summarize what the practice of security could signify, it is probably easier to begin by defining what it is not:


- **Security is neither a product nor a service**. First of all, there is no single product that can act as a “magic black box” that will automatically solve every problem. Moreover, the available capabilities of a given product will be helpful only when they are properly enabled for actual use.

- **Security is not a technology**. Technologies, including those that provide visibility and the ability to block traffic as well as respond to attack situations, may be grouped to form an important defensive system. However, the threat matrix is an ever-changing object, meaning that several techniques and tools that have been largely employed on well-known attack scenarios may prove ineffective when facing the newest challenges.

- **Security is not static**. It is not something that you do once and quickly forget. Processes must exist for dealing with the planning, implementation, testing, and updating tasks. And all of these items must involve people and discipline.

- **Security is not a check box**. You should know what you are protecting against and, once you determine that, look for resources that can demonstrate true security effectiveness.

- **Security is not made only by nominal security elements**. Despite the existence of dedicated security hardware and software products, security is not limited to them. For example, countless contributions can be given to the overall security process by well-configured network infrastructure devices such as routers.

- **Security is not a beautiful graphical user interface (GUI)**. You should always understand what is going on behind the scenes—what is in the brain of the system and not relying blindly, for instance, on reports that state “you are protected.”

 The assigned duty is to protect the relevant digital assets of a particular organization, it is highly advisable that you understand its vision, mission, objectives, and also the possible competitors. All of these items will be considered in a high-level document known as the ***organizational security policy***, which establishes the foundation for all initiatives and tasks pertaining to security.

Among the typical pieces of information that are used to guide policy creation, some deserve special mention:

- **Business Objectives** The main references for policy definition, are related to the classic “*Why we are here*?” and “*What are we trying to achieve?*” questions that are answered in mission statements or company strategies for a period.
- **Regulatory Requirements** These are specific to the industry sector to which the organization belongs and must be always considered. These requirements are normally able to give a clue to what type of data is valuable in that particular industry.
- **Risk** The acceptable level of risk, from the point of view of senior leadership, should be included in the policy. There can be various categories of risks, such as direct financial loss, improper disclosure of intellectual property, strategic information theft, or damages to the public image of the organization.
- **Cost/Benefit Analysis** This analysis should always be evaluated for the mitigation of the identified risks. The cost/benefit ratio of implementing a certain control must always be taken into consideration, and this calculation involves not only investment in products but also the cost of specialized personnel to make it possible.

A security policy is related to an organization’s business strategy and, as such, is normally written using broader terms. To have practical applicability, the general rules and principles it states need to be carefully described in a set of companion documents, which are tactical in nature. The most common of these elements are as follows:

- **Standards** These specify *mandatory* rules, regulations, or activities.

- **Guidelines** These encompass sets of recommendations, reference actions, and operational guides to be considered under circumstances in which standards are not applicable.

- **Baselines** These documents are meant to define the minimum level of security that is required for a given system type.

- **Procedures** These include step-by-step instructions for performing specific tasks. They define how policies, standards, and guidelines are implemented within the operating environment.

**Vulnerability, Threat, and Security Risk**

The concepts of vulnerabilities, threats, and security risks are distinct and yet interrelated:

A ***vulnerability*** is a weakness within a computer system that can be exploited to perform unauthorized actions.

A ***threat*** is defined by any entity (such as a person or a tool) that can exploit a vulnerability intentionally or by accident. Such an entity is also known as a *threat actor* or *threat agent*.

**Example** : An armed bank robber is an example of a threat. A bank teller is an example of a valuable resource that may be vulnerable during a bank robbery.

The concept of *security risk* relates to the probability of a certain vulnerability being exploited by a threat actor. Risk also depends on the value of the digital asset under analysis. For instance, if the same software bug (an example of vulnerability) is present on both a lab virtual machine and a production application server, a higher security risk should be associated with the latter.

**Security Countermeasures and Enforcement**

Within a computing environment, the mechanisms aimed at risk mitigation are called *security countermeasures* (or *security controls*). They can come in multiple formats, including the following:

- Software patching (to eliminate a previously detected vulnerability).

- Implementation of security capabilities that are specifically designed as defensive resources (thus avoiding vulnerability exploitation).

- Verification of user identity before granting access to critical data.

The mere process of defining access policies and their component rules is not sufficient for effective security. You must have the means to ensure that those rules are implemented and obeyed—or, in other words, there must be *enforcement*.

**Confidentiality, Integrity, and Availability**

The following are foundational attributes that you should consider not only for policy definition but also for evaluation of security effectiveness:

**Confidentiality** This principle is concerned with preventing unauthorized disclosure of sensitive information and ensuring that a suitable level of privacy is ensured at all stages of data processing. Encryption is a typical example of a technology designed with confidentiality in mind.

**Integrity** This principle deals with the prevention of unauthorized modification of data and with ensuring information accuracy. Hash message authentication codes, such as HMAC-MD5 and HMAC-SHA (largely employed by the Internet Protocol Security [IPsec] framework), are mathematical functions conceived to provide integrity for the data transmitted in Internet Protocol (IP) packets.

**Availability** This principle focuses on ensuring reliability and an acceptable level of performance for legitimate users of computing resources. Provisions must be made against eventual failures in the operating environment, which includes the existence of well-designed recovery plans at both the physical and logical levels.

To understand how the CIA triad works in practice, consider the example of a bank ATM, which can offer users access to bank balances and other information. An ATM has tools that cover all three principles of the triad:

- It provides **confidentiality** by requiring [two-factor authentication](https://www.csoonline.com/article/3239144/2fa-explained-how-to-enable-it-and-how-it-works.html) (both a physical card and a PIN code) before allowing access to data
- The ATM and bank software enforce data **integrity** by ensuring that any transfers or withdrawals made via the machine are reflected in the accounting for the user's bank account
- The machine provides **availability** because it's in a public place and is accessible even when the bank branch is closed

But there's more to the three principles than just what's on the surface. Here are some examples of how they operate in everyday IT environments.

** Best practices for implementing the CIA triad **

In implementing the CIA triad, an organization should follow a general set of best practices. Some best practices, divided by each of the three subjects, include:

**Confidentiality**

- Data should be handled based on the organization's required privacy.
- Data should be encrypted using 2FA.
- Keep access control lists and other file permissions up to date.

**Integrity**

- Ensure employees are knowledgeable about compliance and regulatory requirements to minimize human error.
- Use backup and recovery software.
- To ensure integrity, use version control, access control, security control, data logs, and checksums.

**Availability**

- Use preventive measures such as redundancy, failover, and RAID. Ensure systems and applications stay updated.
- Use network or server monitoring systems.
- Ensure a data recovery and business continuity (BC) plan is in place in case of data loss.

**Accountability and Nonrepudiation**

*Accountability* is an attribute related to a certain individual or organization being held responsible for its actions. The idea is to ensure that all operations performed by systems or processes can be identified and precisely associated with their author.

*Nonrepudiation* is the property of ensuring that someone cannot deny that they have performed an action in an effort to avoid being held accountable. In the IT security world, repudiation examples are someone denying that a certain system transaction has been carried out or a user denying the authenticity of its own signature.

**Authentication, Authorization, and Accounting**

Authentication, authorization, and accounting are three security functions that are usually combined to deliver access control services. This interaction inspired the creation of the *AAA architecture*, in which the meaning of each “A” is more easily grasped when associated with the question it was designed to answer:

**Authentication** Deals with the question “*Who is the user?*” The process to find this answer basically involves extracting user-related information (such as a username and its corresponding password) from an access request to a system and comparing it to a database of previously defined valid users. Certain environments may treat non-registered users as *guests* or *generic users*, thus granting a basic level of access.

**Authorization** Addresses the question “*What is the user allowed to do?*” This user should have been authenticated before authorization occurs in order to differentiate the access privileges, or *authorization attributes*. The authorization failures that appear on an AAA service report can help characterize improper access attempts.

**Accounting** Answers the question “*What did the user do?*” Through this pro-
 cess, an accounting client—for instance, a networking device—collects user activity information and sends it to an accounting server (or service in the case of the AWS Cloud). This function serves not only to provide statistics about legitimate use but also to spot unexpected user behavior (in terms of traffic volume or abnormal access hours, for instance).


## Cloud Security


### Cloud Comparison

| Key  | AWS                                                    | GCP                     |
| ---- | ------------------------------------------------------ | ----------------------- |
|      | [AWS SecurityHub](https://aws.amazon.com/security-hub) | Security Command Center |
|      | [Amazon Inspector](https://aws.amazon.com/inspector/)  |                         |
|      | [AWS Guarduty](https://aws.amazon.com/guardduty/)      |                         |
|      | [Amazon Macie](https://aws.amazon.com/macie/)          | Cloud Data Loss Prevenntion|
|      | [Amazon Web ACLs](https://aws.amazon.com/waf/)          | Cloud Armor |


## AWS

### Perform Log Analysis with Amazon GuardDuty

[Amazon GuardDuty](https://aws.amazon.com/guardduty/) helps you analyze and process data from different data sources such as CloudTrail event logs, [VPC Flow Logs](https://blog.runpanther.io/aws-security-logging-vpc-flow-logs/), and DNS Logs. GuardDuty uses sophisticated machine learning, anomaly detection, and integrated threat intelligence to identify and prioritize potential threats. Additionally, GuardDuty monitors your AWS account for signs of compromised access such as unusual API calls or deployments in a region not used before.

GuardDuty extracts the relevant fields from logs to help you profile and identify anomalies. You can review these findings through your AWS management console, integrate them into event management or workflow systems, or trigger AWS Lambda for automated remediation or prevention. Here is how GuardDuty displays its findings:

![img](https://lh3.googleusercontent.com/N7xU6-oBXaojtYbS9Bi28gm6Dn1omDkpDIBg5Lh-uE8cHYipX5Exh2LY03LiOF13IZ4kK0Fc7d8lMwRxtO3pRuilMGQ0nP0liEifGRVA258lKVilHhNxI6BFaqdn2fSaRwPzWpCL)

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

SecurityHub also lets you create insights into Security Hub. Insights are a collection of findings that are grouped together to identify common security issues that may require remediation action. The following screenshot shows how SecurityHub brings various AWS security services under a single hood:

![img](https://lh3.googleusercontent.com/ziCdXhASDAT-A9WJqWJXJmQdEAToeOO6h__ZYCygKPILoJL75-R0SXuetPYQum7ZCkb-kC8yFVpbD1OT3jNjvbYCap55ZBMb3PxX1VzkZYpHmJkLc-0skjlNuqPbnL1toAeChYXU)

Security Hub is accessible through the [Security Hub console](https://console.aws.amazon.com/securityhub/) when you sign in to the AWS Management Console. You can also use the Security Hub API, which lets you issue HTTPS requests directly to the service. As of June 2019, AWS Security Hub is [generally available](https://aws.amazon.com/about-aws/whats-new/2019/06/aws-security-hub-now-generally-available/).

### Follow Best Practices with AWS TrustedAdvisor

[TrustedAdvisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) is a real-time guidance solution that monitors your AWS infrastructure and compares it to AWS best practices such as identifying security gaps, fault tolerance, and service limits. Post this comparison, it provides recommendations and action links.

The Trusted Advisor notification feature notifies you about your AWS resource deployment. You can track recent changes or check status on the console dashboard. You can also use [AWS Identity and Access Management](https://blog.runpanther.io/serverless-app-repo-intro/) (IAM) to control access to specific checks or check categories. You can also create alerts and automate actions with Amazon CloudWatch. The following screenshot shows how TrustedAdvisor details AWS best practices recommended for your AWS infrastructure:

![img](https://lh5.googleusercontent.com/_nZkcUWdqor04kOuZtzBvdpp1XXY9m7v5KYChxtdDhtIFixc8_23gALVwERG7E5NptsrhZsOSxmm-NkIxi2qpq0wAzKAt4KsCaE_woxExUCrn3ao59-GivwtNqAYfHLv5YPZRzRK)

Trusted Advisor is available in the AWS Management Console. All AWS users have access to the data for the [seven core checks](https://aws.amazon.com/premiumsupport/trustedadvisor/). Users with business or enterprise-level support can access [all checks](https://aws.amazon.com/premiumsupport/trustedadvisor/best-practices/).

### Know Your Configurations with AWS Config

[AWS Config](https://aws.amazon.com/config/) allows you to assess, audit, and evaluate the configurations of your AWS resources. It provides you with an AWS resource inventory, configuration history, and configuration change. Config records details of changes to your AWS resources to provide you with a configuration history. It also records software configuration changes within your Amazon EC2 instances and servers running on-premises and those provided by other cloud providers.

Rules in Config are configureable and customizable so you can either use pre-built rules for evaluating provisioning and configuring your AWS resources or you can customize pre-built rules to evaluate your AWS resource configurations. You can also create your own custom rules in AWS Lambda that define your internal best practices and guidelines for resource configurations.

AWS Config also provides Conformance packs where you can package a collection of AWS Config rules and remediation actions into a single entity and deploy it across an entire organization. With conformance packs, you can establish a common baseline for resource configuration policies and best practices across multiple accounts in your organization.

AWS Config integrates with AWS CloudTrail, AWS Systems Manager, Amazon EC2 Dedicated Host, Application Load Balancers and AWS Organizations.
