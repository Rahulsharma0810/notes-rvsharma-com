# AWS-SCS-C01

## Domain 1

### Security Basics

**CIA**

* __Confidentiality__: IAM, MFA, bucket policies, security groups, ACL's within VPC's, KMS encryption etc.
* __Integrity__: Certificate Manager (SSL), IAM, bucket policies, S3 version control, MFA for S3 deletion etc.
* __Availability__: Autoscaling, Multi-AZs, Route53 health checks etc.

**AAA**

* __Authentication__: auth into IAM entity (user/role)
* __Authorization__: IAM policies to define access
* __Accounting__: audit trail i.e. CloudTrail

**Non-repudiation**

* Not being able to deny something has happened.
* CloudTrail, CloudWatch.


### How does AWS Secure their Stuff?

Physical and Environmental Security
* AWS consist of regions, with 2+ availability zones, each made up of multiple data centres.
* Secured by fire-detection/suppression, power (2 feeds / different power sources), climate and temperature, management (ex-soldiers / physical access in-out), storage device decommissioning (zero out all data from disks and then shredding/smashing disk).

Business Continuity Management
* Monitor availability, incident response
* Perform company-wide executive reviews when an incident has occurred + communicating issues out to customers

Network Security
* Secure network architecture
* Secure access points - everything is available as a public API, so access points but be secured.
* Transmission protection e.g. TLS security on console login, S3 bucket access etc.
* Amazon corporate segregation - Amazon.com network is completely different network to AWS. Bastion is required for employee access from Amazon.com -> AWS
* Fault-tolerant design - multiple AZ's in multiple regions
* Network monitoring and protection - DDoS mitigation via. AWS shield + advanced DDoS mitigation is available (more costly)

AWS Access
* Account Review and Audit - AWS users' accounts are audited/reviewed every 90days. If account has not been used, it will be revoked and reapplying for access is required.
* Background Checks
* Credentials Policy - Amazon's password policies (very complex, changed every 90 days).

Secure Design Principles
* Formal design reviews by AWS security team, threat modelling, completion of risk assessments, static code analysis tools run as part of build process, all deployed software undergoes re-occurring penetration testing prepared by carefully selected industry experts.

Change Management
* AWS performs routine emergency and configuration changes to AWS infra.
* It is all authorized, tested, logged, approved and documented in accordance with industry norms for similar systems.
* AWS communicates to customers via. email / service health dashboard.

Why should we trust AWS?
* AWS meets a whole bunch of compliance programs / IT security standards.
* Big ones are ISO27001, PCIDSS compliant, HIPAA (medical records).
* Your own software/infrastructure requires a GAP-AUDIT.

Exam Tips
* Remember different security controls around: physical and environmental security, business continuity, network security, AWS access, secure design principles, change management.
* Remember that the corporate Amazon.com network is completely segregated from the AWS network. Permissions / reviews are required when an employee wants to access AWS. Permissions are revoked as soon as nologin for 90 days.


### Shared Responsibility Model

What is it?
* Security WITHIN the cloud is the responsibility of the customer.
* E.g. House example:
    * Landlord is responsible for installing fire alarms, fences.
    * You are responsible for locking your door, making sure windows are shut etc.

AWS Security Responsibilities
* Global infrastructure - their data centres
* Hardware, software, networking and facilities - all their hardware, software such as RDS / AWS operation systems etc.
* Managed services - S3, DynamoDB etc.

Customer Security Responsibilities
* Infrastructure as a Service
* Updates and security patches e.g. EC2 instances etc.
* Configuration of AWS-provided firewall - VPC rules, security groups, network ACLs etc.

Diagram of the Shared Responsibility Model:
https://aws.amazon.com/compliance/shared-responsibility-model/

Basically, if the customer has no access to the underlying OS/software/infrastructure, then it is AWS's responsibility.


### Shared Responsibility - AWS service types

Infrastructure services - compute services such as EC2, EBS, Auto Scaling, VPC
* You can architect and build cloud infrastructure, control the OS, configure and operate any identity management system that provides access to the user layer of the virtualization stack.
* EC2 - AMIs, OS, applications, data in transit, data at rest, data stores, credentials, policies and configuration.

Container services - services such as RDS, Elastic Map Reduce (EMR) and Elastic Beanstalk.
* RDS example - you have a DB that you can install/access but you don't manage the underlying OS. AWS is responsible for patching for the RDS instance.
* Services that are typically run on separate EC2s or other infrastructure instances. Sometimes you don't manage the OS or platform layer.
* Customer is responsible for setting up and managing network controls such as firewall rules, managing platform-level identity and access management separately from IAM.

Abstracted services - services such as S3, Glacier, DynamoDB, SQS, SES.
* Services that abstract the platform or management layer on which you can build and operate cloud applications.
* Customer can access the endpoints of these abstracted services using AWS APIs.
* AWS is responsible for managing the underlying service components or OS in which these services reside.

Exam Tips: Have a STRONG understanding of the shared responsibility model.
* The model changes for the three different service types:
1. Infrastructure services (EC2, EBS, VPC)
2. Container services (RDS, EMR, Elastic Beanstalk) - AWS responsible for the OS, container itself.
3. Abstracted services (S3, Glacier, DynamoDB, SQS, SES) - AWS responsible for almost everything, except for the application layer e.g. TLS / access controls.


### Security IN AWS

Controls that you need:
* __Visibility__: AWS Config - managed and custom rules
* __Auditability__: AWS CloudTrail - records every API call in the environment
* __Controllability__:
    * AWS KMS - multi-tenant. Underlying hardware is shared, but strict controls.
    * AWS CloudHSM (hardware security module) - dedicated. Underlying hardware is NOT shared. __Exam: Which service is required for FIPS 140-2 Compliance? - CloudHSM as KMS being multi-tenant/shared does not comply.__
* __Agility__:
    * AWS CloudFormation - deploy templates to any regions
    * AWS Elastic Beanstalk - AWS provision resources for you, rather than you doing it each service manually
* __Automation__:
    * AWS OpsWorks - operate alongside CF / EB
    * AWS CodeDeploy - operate alongside CF / EB
* __Scale__: Every customer gets the same AWS security foundations, from a startup to a Fortune 500 company.

Other services applying to all controls
* AWS IAM - creating users, password policies, MFA, groups
* AWS CloudWatch - monitor environment, see breaches, CPU runtime
* AWS Trusted Advisor - advises on security, budgeting, system performance and reliability


## Domain 2

### IAM, S3 & Security Policies

IAM provides:
* Centralised control of your AWS account
* Shared access to your AWS account
* Granular permissions
* Identity Federation (Active Directory, Facebook, Linkedin etc.)
* MFA
* Provide temporary access for users/devices and services where necessary.
* Allows you to set up your own password rotation policy
* Integrates with many AWS services
* Supports PCI DSS Compliance

Critical Terms:
* Users - end users
* Groups - a collection of users under one set of permissions (apply one policy to group, users inherit policy)
* Roles - assign roles to AWS resources (e.g. EC2, Lambdas)
* Policies - document that defines permissions

__IAM is global__ - users, groups, roles, policies are done on a global level, not region-specific.

IAM Permissions Boundary for IAM Entities (users/roles)
* A Permissions Boundary is using a managed policy to set the _maximum permissions_ that an identity-based policy can grant to an IAM entity.
* https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html
* https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_PermissionsBoundary


### IAM Root User Scenario

_Scenario: You have have started as a sysadmin at a cloud-based company. Previous admin used only the root-user._

First thing to do = rotate everything
* Change password
* De-activate then re-activate MFA
* Delete Access Key ID / Secret Access Key (don't create new access keys via. root user)
* Verify and delete IAM users that are not-legitimate.

### IAM Policies

**Policy contains PARC**

  - **Principal**
    - WHO/WHAT is Allowed/Denied access, indicated by ARN.
    - If IAM Policy, this is implicit based on what you attach it too
    - Can be Everyone (AWS:*.*), Specific account/s, IAM user, Federated user, Specific role, Specific service
  - **Action**
    - Action or NotAction (everything but)
    - ec2:StartInstances
    - iam:ChangePassword
    - s3:getObject
    - sqs:SendMessage, sqs:ReceiveMessage
    - iam:*AccessKey*
  - **Resource**
    - Object(s) being requested
    - Resource or NotResource (everything but)
    - Resource: `arn:aws:s3:::mybucket/*`
    - NotResource: `arn:aws:s3:::securityloggingbucket/*`
    - Resource: `aws:sqs:us-west-2:12312312312312:queue1`
    - Resource: `arn:aws:dynamodb:us-west-2:1231232:table/books_table`
    - Resource: `arn:aws:ec2:us-east-1:1:12312312312312:instance/*`
  - **Condition**
    - DateGreaterThan : `aws:CurrentTime : "2018-12-25T00:00:00Z"`
    - DateLessThan: `aws:CurrentTime : "2018-12-26T08:00:00Z"`
    - IPAddress: aws:SourceIP : [192.0.2.0/24, 10.0.0.0/8]
    - The above is AND, the OR is in the values (e.g. see IP address)
    - All conditions must be true for condition to be met

IAM policies specify what you are allowed to do with any AWS resource. You attach IAM policies to users, groups or roles.

- Policy types (all use PARC model)
  - **Service Control Policies (SCPs)** -> AWS Organizations / OU
    - Use case: Disable access to services
  - **Inline policies &  Managed policies** -> IAM
    - Use case: Set granular permissions based on functions that users or application need to perform
  - **Scoped-down policies** -> AWS Security Token Service (STS)
    - Use case: Reduce general shared permissions further
  - **Resource-based policies** (e.g. S3 bucket policies / Queues/ Vaults) -> AWS Service
    - Use case: Control access at the resource
    - Use case: Cross-Account access
 - How these policies work together....
   - **Same AWS account:**
   **SCP** -> Union(Intersect(Union(IAM Managed Policy, IAM Inline policy), Scoped-Down policy), Resource-based policies)
   - Cross account:
   **SCP** -> Intersect(Intersect(Union(IAM Managed Policy, IAM Inline policy), Scoped-Down policy), Resource-based policies)
 - Cross Account access:
    - To establish cross-account access, in the trusting account (Account A), you create an IAM policy that grants the trusted account (Account B) access to specificresources. Account B can then delegate this access to its IAM users. Account B cannot delegate more access to its IAM users than the permissions that it has been granted by Account A.


### S3 Bucket Policies

S3 bucket policies specify what actions are allowed or denied on the bucket.
* They are attached only to S3 buckets.
* They are BUCKET-LEVEL only (not bucket object-level).

Why use S3 policy instead of IAM policy
* You want to grant cross-account access to your S3 environment, without using IAM roles.
* Your IAM policies reach the size limit (2kb for users, 5kb for groups, 10kb for roles). S3 supports bucket policies of up to 20kb.
* You prefer to keep access control policies in the S3 environment.

__Management of individual S3 buckets__ = best use case of S3 bucket policies.
* Having a deny policy for a specific bucket is easier than creating an IAM policy that denies access to a specific bucket, then rolling that out to every user in your organisation.
* Example scenario: bucket could contain everyone's performance reviews in it.

Use the __AWS Policy Generator__ to generate a S3 bucket policy.

In any AWS policy (IAM, S3, Key), a __DENY will always override an ALLOW__.


### S3 Object Access Control Lists (ACLs)

S3 ACLs are a legacy access control mechanism. AWS recommends sticking to IAM policies and S3 bucket policies.
However, S3 ACLs can be applied to individual objects/files as opposed to S3 bucket policies.

S3 ACL use cases:
* If you need __fine grained permissions__ on individual files/objects.
* Reaching __size limit of 20kb__ for S3 bucket policies.

Managing S3 object permissions
* Click on object itself -> permissions
* Applying S3 object policies to individual IAM users - possible but can only be done via. CLI or AWS API (not console).
* Add S3 object access for other AWS Accounts by adding Account ID.

__Conflict policy example__: IAM user policy denying all S3 read vs. S3 bucket with object open to the public.
* Even though an explicit DENY overrides all ALLOW policies... the user would still be able to access the object. WHY??? =>
* The user CAN access objects in the public bucket via. the public bucket link (as an anonymous user).
* The user CANNOT access objects in the public bucket via. opening the object within AWS console/CLI/API (as an AWS user).

EXAM: Best exam practise is by creating your own S3 Bucket Policies, S3 Object ACLs, IAM User Policies etc.

### Policy Conflicts (EXAM ESSENTIAL TOPIC)

What happens if an IAM policy conflicts with an S3 policy which conflicts with an S3 ACL?

Whenever an AWS principal (user, group or role) issues a request to S3, the authorization decision depends on the union of all the IAM policies, S3 bucket policies and S3 ACLs that apply.

Least-privilege:
* Decisions ALWAYS default to DENY.
* An explicit DENY ALWAYS trumps an ALLOW.
* So if you DENY access to something somewhere and then something else allows access the DENY will override the ALLOW.

ACCESS DENIED EXAMPLES:
* IAM policy grants access to an object + S3 bucket policy denies access to object + no S3 ACL exists.
* No method specifies an ALLOW, request is denied by default.

ACCESS ALLOWED EXAMPLE:
* No method specifies a DENY + one or more methods specify an ALLOW.

__Policy Conflict flow__:
1. Decision starts at DENY by default.
2. Any applicable policies? ( YES = CONTINUE | NO = DENY )
3. Does a policy have an EXPLICIT DENY? ( YES = DENY | NO = CONTINUE )
4. Does a policy have an ALLOW? ( YES = ALLOW | NO = DENY)

This flow will be examined heavily with scenarios containing 2-3 different policies.


### Forcing Encryption on S3

Use S3 bucket policy to enforce encryption - prevent read without SSL enabled:
```javascript
// If secure transport is false, DENY read.
// Alternative policy, if secure transport is true, ALLOW read.
"Sid":"PublicReadGetObject",
"Effect":"Deny",
"Principal":{
    "AWS":"*"
}
"Action":"s3:GetObject",
"Resource":"arn:aws:s3:::bucketname/*",
"Condition":{
    "Bool":{
        "aws:SecureTransport":false
    }
}
```

### Cross-Region Replication

Cross-region replication replicates objects from one region to another. By default, this is done using SSL. You don't need to enable encryption.

You can replicate objects from a source bucket to only one destination bucket (1-1 relationship).
After S3 replicates an object, the object can't be replicated again.

Cross-Region Replication (CRR) requirements:
* Src/dest buckets must have __versioning enabled__.
* Src/dest buckets must be in __different AWS regions__.
* Amazon S3 must have permissions to replicate objects from src/dest bucket on your behalf. When you enable CRR for the first time, a __role will be created__ for you + a __customer-managed policy__ will be assigned.
* If src bucket owner also owns the object, the bucket owner has full permissions to replicate the object. If not, object owner must grant the bucket owner `READ`/`READ_ACP` permissions via. the object ACL.

CRR + Cross Accounts:
* The IAM role must have permissions to replicate objects in the destination bucket.
* In CRR config, you can optionally direct AWS S3 to change ownership of object replicas to the AWS account that owns the destination bucket.
* __AUDIT account Cross-Region Replication use case__:
1. CloudTrail logs AWS accounts XYZ.
2. Turn on CRR to replicate logs to AUDIT account.
3. AWS accounts XYZ can only replicate logs, but not read/write logs in AUDIT account.

What is replicated?
* New objects created after you add a replication config.
* S3 replicates objects encrypted using S3 managed keys (SSE-S3) or KMS managed keys (SSE-KMS) + unencrypted objects.
* Object metadata
* Object ACL updates
* Object tags
* S3 replicates only objects in the src bucket for which the bucket owner has permissions to read objects and read access control lists.

DELETE marker replication
* Delete markers on an object are replicated. Deletion of versions of objects are NOT replicated.
* A delete marker only hides an object via. versioning, not actually delete it.

What is NOT replicated
* Anything created __BEFORE CRR is turned on__.
* Objects created with SSE using __customer-provided (SSE-C)__ encryption keys.
* Objects created with SSE using __AWS KMS-managed encryption (SSE-KMS)__ keys, unless you explicitly enable this option.
* Objects in the src bucket for which the __bucket owner does NOT have permissions__ (happens when the obj owner is different from the bucket owner).
* Delete replication of a particular VERSION of an object. Source bucket deletion != dest bucket deletion. This is to stop malicious deletion of a specific version on an object.

Resources:
* Cross-Region Replication: https://docs.aws.amazon.com/AmazonS3/latest/dev/replication.html
* What does S3 replicate: https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-what-is-isnot-replicated.html


### Securing S3 Using CloudFront

Force users to only access S3 via. CloudFront instead of direct access via. S3 URL.

Steps to create a new CF distribution:
1. CloudFront service
2. Create a new distribution -> Web Distribution
3. Origin Domain Name: the source S3 bucket URL
4. Restrict Bucket Access -> NO (exam will test how to restrict AFTER a distribution has already been created)
5. Everything as default

Steps to secure S3 bucket via. CF:
1. Goto CloudFront -> __Origins and Origin Groups__
2. Turn on __Restrict Bucket Access__ -> Create an __Origin Access Identity__
3. Turn on __Grant Read Permissions on Bucket__ to allow CloudFront OAI to perform `s3:GetObject`

S3 bucket policy to restrict access via. CloudFront:
```javascript
{
	"Sid": "1",
	"Effect": "Allow",
	"Principal": {
		"AWS": "arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity EAF5XXXXXXXXX"
		},
	"Action": "s3:GetObject",
	"Resource": "arn:aws:s3:::AWSDOC-EXAMPLE-BUCKET/*"
}
```

### Using SSL Certificates using CloudFront

DEFAULT SSL CERTIFICATE: If you are happy for users to access your content using *.cloudfront.net domain name.

CUSTOM SSL CERTIFICATE: If you want to use a domain name that you own example.com.

You must store your custom SSL Certificate using:
* IAM API
* AWS Certificate Manager (ACM)
* Only in the `us-east-1` region = US East (N. Virginia)

### Secure S3 Using Pre-Signed URLs

Another method of accessing objects inside S3 - done via. SDKs (Python, Java, Go) or CLI.

```bash
$ aws s3 mb s3://acloudgurupresigned                # Make bucket
$ echo "Hello Cloud Gurus" > hello.txt
$ aws s3 cp hello.txt s3://acloudgurupresigned      # Upload object to bucket
$ aws s3 ls s3://acloudgurupresigned                # Check object is in bucket
$ aws s3 presign s3://acloudgurupresigned/hello.txt --expires-in 300 # presign URL with 300 sec expiration (default expiry = 1 hr)
https://acloudgurupresigned.s3.amazonaws.com/hello.txt?AWSACcessKeyId=XXX&Expires=XXX&x-amz-security-token=XXX&Signature=XXX
```

### Security Token Service (STS) (IMPORTANT EXAM TOPIC)

STS grants users limited and temporary access to AWS resources.

These users can come from:
* Federation (typically Active Directory)
  * Uses SAML
  * Grants temp access based off user's AD credentials. Does not need to be a user in IAM.
  * SSO allows users to log into AWS console without assigning IAM credentials.
* Federation with Mobile Apps
  * Facebook / Amazon / Google or other OpenID providers.
* Cross Account Access
  * Lets users from one AWS account access resources in another.

Key Terms:
* Federation - combining or joining a list of users in one domain (such as IAM) with a list of users in another domain (such as AD, Facebook etc.)
* Identity Broker -  service that allows you to take an identity from point A and join it (federate it) to point B.
* Identity Store - services like AD, Facebook, Google etc.
* Identities - a user of a service like Facebook etc.

An Identity is a user, that is stored in an Identity Store (like Active Directory/Facebook). You create an Identity broker that allows you take those Identities in your Identity Store and join them up to IAM -> This is essentially the federation/joining of IAM with AD/Facebook. The service that allows this is the Security Token Service.

Scenario: _You are hosting a company website on EC2 web servers in your VPC. Users of the site must login to the site, which authenticates against the company's AD servers which are based on-site at the company HQ. Your VPC is connected to the company HQ via. a secure IPSEC VPN. Once logged in, the user can only have access to their own S3 bucket._

How to set this up:
1. Develop an Identity Broker (join AD -> IAM).
2. Identity Broker will authenticate (using client/appid, secret) against AD:
    * Authenticate to obtain an AD token.
    * Pass AD token to STS.
    * STS will provide us with another token.
3. Pass STS to the web application to authenticate against S3.
4. S3 uses IAM to check if user has access to S3.
5. User is able to access S3.

Scenario:
1. Employee enters username / password
2. Application calls Identity Broker. Broker captures username/password.
3. Identity Broker uses the organisation's LDAP directory to validate the employee's identity.
4. Identity Broker calls the `sts:GetFederationToken` API using IAM credentials.
    * GetFederationToken(DurationSeconds, Name, Policy, PolicyArn) where:
    * _DurationSeconds_: duration of the STS token (1 to 36 hours).
    * _Name_: name of the federated user.
    * _Policy_: inline IAM policy.
    * _PolicyArn_: ARN referencing an IAM policy.
5. STS confirms that the policy of the IAM user making the call to GetFederationToken gives permission to create new tokens.
6. STS returns the temp STS token to the Identity Broker.
7. Identity Broker returns the STS token to the application.
8. Application uses the STS token to make requests to S3.
9. S3 uses IAM to verify STS token and to allow requested operation on the given S3 bucket.
10. IAM provides S3 with go-ahead to perform requested operation.

High-Level Summary:
1. Authenticate (as Identity/User) against 3rd-party (Identity Store: AD/Facebook/Google).
2. Authenticate (as Identity Broker) against STS.
3. Authenticate (as Application) against AWS service to obtain access to resource.

### Web Identity Federation / Amazon Cognito

Web Identity Federation lets you give users access to AWS resources after they have successfully authenticated with a web-based identity provider like Amazon/Facebook/Google. User trades authentication code from Web ID provider for an AWS STS token.

Suggested use case: mobile app which you want to make available to Facebook users. (recommended for social accounts)

Amazon Cognito
* Sign-up / Sign-in to your apps
* Provides guest access
* Acts as identity broker between your app / Web ID provider
* Synchronises user data across multiple devices (mobile, desktop data sync)
* Recommended for mobile apps running on AWS.

Amazon Cognito scenario:
* Mobile shopping app: S3 for product data, DynamoDB for customer data.
* User logs into Facebook, Facebook provides web token.
* Cognito takes web token and exchanges it for STS token.
* Cognito passes STS token to mobile app.
* Mobile app uses STS token to get access to resources for user.

Amazon Cognito benefits:
* No need for mobile app to embed or store AWS credentials locally on the device = increased security.
* Provides users a seamless experience across all devices.

Cognito User Pools: user directories used to manage sign-up and sign-in functionality for mobile/web apps.
* User sign-in directly via. User Pool or indirectly via. identity provider (Amazon/Facebook/Google)
* Cognito acts as identity broker between ID provider and AWS.

### Glacier Vault Lock

Glacier is a low-cost storage service for data archiving and long-term backup.
* _Archives_: a single file or multiple files stored in a .tar or .zip.
* _Vault_: containers which store one or more Archives
* _Vault Lock Policy_: similar to an IAM policy to configure and enforce compliance controls - configure write-once-read-many archives / create data retention policies

Example Vault Lock Policy: Enforce archive retention for 1 year (deny archive delete for all archives <365 days old)
```javascript
"Version":"2012-10-17",
"Statement":[
    {
        "Sid":"deny-based-on-archive-age",
        "Principal":"*",
        "Effect":"Deny",
        "Action":"glacier:DeleteArchive",
        "Resource":[
            "arn:aws:glacier:us-west-2:XXXaccountidXXX:vaults/examplevault"
        ],
        "Condition":{
            "NumericLessThan":{
                "glacier:ArchiveAgeInDays":"365",
            }
        }
    }
]
```

Steps to configuring Vault Locks:
* Create Vault Lock policy.
* Initiate lock by attaching Vault Lock policy to your vault = in-progress state.
* You have 24 hours to validate the lock policy. You can abort within 24 hours.
* Once validated, Vault Lock policies are immutable.

Vault Lock Policy vs. Vault Access Policy:
* https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock.html

### AWS Organisations

AWS Organisations is an account management service that lets you consolidate multiple AWS accounts into an organisation so that you can consolidate billing, group your AWS accounts into logical groupings for access control and attach Service Control Policies.

SCPs enable you to restrict, at the account level of granularity, what services and actions the users, groups, and roles in those accounts can do. However, an SCP never grants permissions. The SCP limits permissions for entities in member accounts, including each AWS account root user. SCPs are available only in an AWS organization that has all features enabled, SCPs aren't available if your organization has enabled only the consolidated billing features.

https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html


### IAM Credential Report

IAM Credential Report is a CSV-formatted report which lists all users in the accounts + status of their various credentials, including
* Passwords: enabled, last used, last rotated, next rotation.
* Access Keys: similar to above + last used.
* MFA devices: similar to above.

CLI commands for IAM Credential Reports
```bash
# generate a credential report
aws iam generate-credential-report
# download a credential report / same API call but base64 decode
aws iam get-credential-report
aws iam get-credential-report --output text --query Content | base64 -D
```

Required permissions to generate IAM Credential Reports
* `GenerateCredentialReport`: create report
* `GetCredentialReport`: download report

An IAM Policy with permissions to generate IAM Credential Reports
```javascript
{
    "Version": "2012-10-17",
    "Statement": [{
        "Sid": "VisualEditor0",
        "Effect": "Allow",
        "Action": [
            "iam:GenerateCredentialReport"
        ],
        "Resource": "*"
    }]
}
```


### Summary / Exam Tips

Resetting Root Users
* Create new root user password / strong password policy.
* Delete 2FA / re-create.
* Delete Access Key ID / Secret Access Key.
* Check existing user accounts, delete if not legit.

IAM policies
* IAM is Global.
* Three different types: (1) Managed Policies (2) Customer Managed Policies (3) Inline Policies

S3 policies
* S3 policies are attached only to S3 buckets (NOT objects). They specify what is ALLOWED/DENIED on the bucket.
* Broken down to the user-level.
* _EXPLICIT DENY ALWAYS OVERRIDES AN ALLOW_.
* S3 ACL's: Legacy access control for enforcing access to S3 OBJECTS.
* S3 policy conflicts: see _policy conflict diagram_ above (IMPORTANT).
* `aws:SecureTransport:` restrict S3 bucket access to only HTTPS.
* Cross-Region-Replication (CRR):
    * Delete markers are replicated, deleted versions of files are NOT replicated.
    * Versioning must be enabled.
    * Possible to use CRR from one AWS account to another
    * SSL is enabled by default when you configure CRR
    * IAM role must have permissions to replicate objects in destination bucket.
    * Scenario: replicate CloudTrail logs to separate AWS audit account (can only send data there, not read/write).

Pre-signed URLs (CLI/SDK only):
* Access objects using pre-signed URL's
* Exist only for a certain length of time.
* Change TTL by using `expires-in`

STS / Identity Provider
* User provides credentials to Identity Provider (AD/FB/Google) -> AWS STS -> User accesses AWS resource -> AWS resource checks IAM -> access is provided to user.


## Domain 3

### Logging and Monitoring

### AWS CloudTrail

AWS CloudTrail is a web service that records AWS API calls for your account and delivers log files to you.
* User interacts with AWS platform via. Console or API Call.
* CloudTrail logs all these interactions with AWS services (only API calls).
* CloudTrail will NOT log actions such as SSH/RDP into an EC2.

Enables:
* After-the-fact incident investigation
* Near-realtime intrusion detection
* Industry and regulatory compliance

Provides:
* Logs API call details (for supported services)

Supported services: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html
Un-supported services: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-unsupported-aws-services.html
CloudTrail limits: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html

Log info:
* Metadata around API calls
* Identity of API caller
* Time of API call
* Source IP of API caller
* Request params
* Response returned by the service

Where? CloudTrail Event Logs:
* Sent to an S3 bucket
* You manage retention in S3
* Delivered every 5 minutes to S3 with up to 15 minute delay
* SNS notifications available - e.g. notify you if something happens
* Can aggregate across multiple regions
* Can aggregate across multiple accounts - good for non-repudiation. Bad actor can only destroy within account, not audit account.

Setup:
* CT enabled by default (only keeps 7-day audit trail), you will need to provision to have it for longer.
* Management Events: ALL READ/WRITE
* Data Events (s3 object activity): leave as default = not enabled
* Storage Location: create a new S3 bucket

Validating CT log file integrity:
* SHA-256 hash
* SHA-256 with RSA for digital signing
* Log files are delivered with a 'digest' file
* Digest files can be used to validate the integrity of the log file
* You can use the AWS CLI to perform validation.

### CloudTrail Log Protection

Log files are encrypted by default (AES-256) even if the bucket itself doesn't show encryption turned on.

CT logs must be secured because they contain valuable info to an attacker such as:
* Personally identifiable info such as usernames / team membership.
* Config information such as a DynamoDB table and key names may be stored.

How to stop unauthorised access?
* Use IAM policies
* Use S3 bucket policies to restrict access
* Use SSE-S3 or SSE-KMS to encrypt logs

How do we restrict access to only employees with a security responsibility?
* Place employees who have a security role into an IAM group with attached policies
* Two AWS-managed policies: AWSCloudTrailFullAccess (security role) and AWSCloudTrailReadOnly (auditor role)

How can we be notified that a log file has been created / validate integrity?
* Configure SNS notifications and log file validation.
* Develop a solution to execute log validation using the digest file.

How to prevent CT log files from being deleted?
* Using IAM and bucket policies
* Configure S3 MFA delete
* Validate that logs have not been deleted using log file validation

How to ensure that logs are retained for X years?
* By default, logs are kept indefinitely
* Can use S3 Object Lifecycle Management to delete files after required period of time.
    * Go to S3 bucket -> Management Tab -> "Add lifecycle rule" button -> Configure bucket expiration
* OR move files to AWS Glacier for long-term storage.

### AWS CloudWatch

AWS CloudWatch is a monitoring service for AWS cloud resources and the applications you run on AWS.

Enables:
* Resource utilisation,. operational performance monitoring
* Log aggregation and basic analysis

Provides:
* Real-time monitoring within AWS for resources and applications
* Hooks to event triggers

Key components:
1. CloudWatch
2. CloudWatch Logs
3. CloudWatch Events

CloudWatch:
* Real-time monitoring: standard monitoring (every 5 min) / detailed monitoring (every 1 min)
* Metrics: CPU utilisation, network utilisation
* Alarms: CPU > 80%, trigger alarm
* Notifications: SNS notifications etc.
* Custom Metrics: pass / program custom metrics via. AWS API.

CloudWatch Logs:
* Pushed from some AWS services, including CloudTrail
* Pushed from your application/systems - kernel logs, application logs, web-server logs etc.
* Metrics from log entry matches
* Stored indefinitely (not user S3)

CloudWatch Events | scenario: user creating EC2 instance, resulting in auto-deletion via. CloudWatch Events
1. User performs API call (create EC2)
2. API call logged in CloudTrail S3 bucket
3. CloudTrail is configured as a CloudWatch Event Source, so API call is pushed to CloudWatch Events
4. CloudWatch Events pushes details of API call to an Event Target, such as an AWS Lambda
5. AWS Lambda deletes EC2 instance.

CloudWatch Events:
* Near real-time stream of system events
* Events:
    * AWS Resources state change
    * AWS CloudTrail (API Calls)
    * Custom events (e.g. HTTP 403 status in Apache web-server logs)
    * Scheduled events
* Rules: match incoming events and route them to one or more targets
* Targets: Lambda, SNS topics. SQS queues, Kinesis Streams and more

### AWS Config

AWS Config is a fully managed service that provides you with an AWS resource inventory, configuration history and configuration change notifications to enable security and governance.

Enables: Compliance auditing, security analysis, resource tracking (what resource we're using where)
Provides: Configuration snapshots and log config changes of AWS resources, automated compliance checking

AWS Config needs to be deployed in each individual region. It doesn't automatically deploy in every region in your account.

How does it work:
1. AWS resource configuration change -> event fires off
2. AWS Config picks up event -> AWS Config logs event in S3 bucket
3. Event target = Lambda is triggered -> Managed or Custom rules (Lambda functions)
4. AWS Config will evaluate if configuration change has broken a rule
5. If rule is broken, AWS Config will trigger SNS notification and is sent to user

Terminology:
* _Configuration Items_: point-in-time attributes of resource
* _Configuration Snapshots_: collection of config items
* _Configuration Stream_: stream of changed items
* _Configuration History_: collection of config items for a resource over time
* _Configuration Recorder_: the configuration of AWS Config that records and stores config items (Config Recorder Role)


Recorder Setup:
* Logs config for account in region (per-region-basis)
* Stores in S3
* Notified of issues via. SNS


What we see:
* Resources Type, Resource ID
* Compliance checks:
    * Trigger:
        * periodic
        * configuration snapshot delivery (change in resource config -> trigger check)
    * Managed Rules: ~40 rules
* Timeline: configuration details, relationships, changes, CloudTrail events


Permissions needed for AWS Config - requires and IAM role with:
* ReadOnly permissions to the recorded resources
* Write access to S3 logging bucket
* Publish access to SNS


Restrict access to AWS Config:
* Users need to be authenticated with AWS and have appropriate permissions set via. IAM policies to gain access.
* Only Admins/Security needing to set up and manage Config require full access.
* Provide ReadOnly for Config day-to-day use e.g. analyse misconfigurations etc.


Monitoring Config:
* Use CloudTrail with Config to provide deeper insight into resources.
* Use CloudTrail to monitor access to Config - e.g. someone stopping Config Recorder would be monitored in CloudTrail.


AWS Config is a big part of the exam, so read the Config FAQ: https://aws.amazon.com/config/faq/

### Set up an alert if Root user logs in / pro-active alerting (will be tested in exam)

Set up an alert if the Root user logs in and makes API calls
1. Turn on CloudTrail-CloudWatch logs integration
    * A role is required for CT to perform CloudWatch API calls. Two calls are performed:
    * `CreateLogStream`: Create a CloudWatch Logs log stream in the CloudWatch Logs log group you specify.
    * `PutLogEvents`: Deliver CloudTrail events to the CloudWatch Logs log stream.
2. Create a CloudWatch Metric Filter
3. Assign a metric
4. Create a Metric Alarm `{ $.userIdentity.type = "Root" && $.userIdentity.invokedBy NOT EXISTS && $.eventType != "AwsServiceEvent" }`
5. Test the alarm and receive an SNS notification
6. Look up the event and take corrective actions

### AWS Cloud Hardware Security Module (CloudHSM)

_This topic is not really examined - can mostly skip it._


AWS CloudHSM service helps meet corporate, contractual and regulatory compliance requirements for data security by using dedicated Hardware Security Module appliances within the AWS Cloud.


Enables: Control of data, evidence of control, meet tough compliance controls
Provides: Secure key storage (generate, store public/private keys), cryptographic operations, tamper-resistant Hardware Security Module

### AWS Inspector and AWS Trusted Advisor - examined

AWS Inspector
* Automated security assessment service that helps improve security/compliance of applications on AWS.
* After performing an assessment, AWS Inspector produces a detailed list of security findings prioritised by level of security.
* Findings can be reviewed directly or as part of a report available via. AWS Inspector or API.
* How does it work (scenario: assessment target is an EC2/prod-webserver)
    1. Create an assessment target
    2. Install agents on EC2 instances
    3. Create "Assessment Template"
    4. Perform an "Assessment Run"
    5. Review "Findings" against "Rules"
* Master template: Testing all rules - multiple rules packages over a 24 hour period
* Rule Packages: CVE's, CIS OS Config Benchmarks, Security Best Practices, Runtime Behaviour Analysis

AWS Trusted Advisor
* A service to advise you on Cost Optimisation, Performance, Security, Fault Tolerance.
    * _Basic Trusted Advisor_: Core checks and recommendations
    * _Full Trusted Advisor_: Business and Enterprise Companies only
* Some recommendations available to basic plan:
    * Security Groups (unrestricted ports), IAM use, MFA on Root, Service Limits (usage limits), exposed EBS snapshots etc.

### Logging

Understand the 4 logging services and their differences: _CloudTrail, CloudWatch, Config, VPC Flow Logs_

Resources: White-paper _Security at Scale: Logging in AWS_ https://d1.awsstatic.com/whitepapers/compliance/AWS_Security_at_Scale_Logging_in_AWS_Whitepaper.pdf

Control access to log files:
* Prevent unauthorised access (Authentication):
    * IAM users, groups, roles and policies
    * S3 bucket policies
    * MFA (IAM and S3 bucket policy level)
* Ensure role-based access (Authorization):
    * IAM users, groups, roles and policies
    * S3 bucket policies
* Alerts when logs are created or fail:
    * CloudTrail notifications
    * AWS Config rules
* Alerts are specific, but don't divulge detail:
    * CloudTrail SNS notifications only point to log file location, not show actual details.
* Log changes to system components:
    * AWS Config rules
    * CloudTrail
* Controls to prevent modification to logs:
    * IAM and S3 controls and policies
    * CloudTrail log file validation
    * CloudTrail log file encryption

Storage of log files:
* Logs are stored for at least 1 year
    * Store logs for an organisational-defined period of time
    * Store logs in real-time for resiliency
* S3
    * S3 Object Lifecycle Management
    * 99.99999% durability and 99.99% availability of objects over a given year


## Domain 4

### Infrastructure Security

### AWS Key Management Service (KMS)

KMS is a managed service that makes it easy for you to create and control the encryption keys used to encrypt your data + uses Hardware Security Modules (HSMs) to protect the security of your keys.

*KMS is region-specific.*

Customer-Master-Keys (CMK)
* Is a logical representation of a master key, typically used to generate/encrypt/decrypt *Data Keys* used to encrypt your actual data - this practice is known as *Envelope Encryption*.
* CMKs consist of:
    * Alias
    * Creation date
    * Description
    * Key state
    * Key material (either customer provided or AWS provided)
* CMKs can NEVER be exported.
* You cannot delete CMKs immediately, only disable them with a 7-30 day waiting period before deletion.
* There are three types of CMKs:
    1. Customer managed CMKs - customer owned / imported keys in your account (full control)
    2. AWS managed CMKs - AWS managed keys in your account that are associated with an AWS service
    3. AWS owned CMKs - AWS owned keys that are NOT in your account for securing data in multiple AWS accounts (no control)

Customer-managed CMK: Importing your own Key Material into KMS
1. Create a customer-managed CMK with no key material by selecting "External" for the key material origin (not usable yet).
2. Import key material - select Wrapping Algorithm SHA1.
3. Import key material - download Wrapping Key (public key) as `PublicKey.bin` and Import Token `ImportTokenxxx`.
4. Use `openssl` and follow instructions here to generate key material and encrypt it with the Wrapping Key: https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-encrypt-key-material.html.
    * Generate a 256-bit symmetric key and save it in a file named `PlaintextKeyMaterial.bin`:
    `$ openssl rand -out PlaintextKeyMaterial.bin 32`
    * Encrypt the key material with the public Wrapping Key you downloaded earlier
    ```
    $ openssl rsautl -encrypt \
                 -in PlaintextKeyMaterial.bin \
                 -oaep \
                 -inkey PublicKey.bin \
                 -keyform DER \
                 -pubin \
                 -out EncryptedKeyMaterial.bin
    ```
5. Upload `EncryptedKeyMaterial.bin` and `ImportTokenxxx`.
6. The key is now available for use.

Why import your own Key Material:
* Compliance - prove that randomness meets your requirements.
* Extend your existing processes to AWS.
* Deletion of key-material without a 7-30 days wait.
* To be resilient to AWS failure by storing keys outside AWS.

Considerations of importing your own Key Material:
* You CANNOT use the same `EncryptedKeyMaterial` and `ImportToken` files twice - it is SINGLE USE only.
* You CANNOT *enable automatic key rotation* for a CMK with imported key material.
* You CAN *manually rotate* a CMK with imported key material - do this by creating a NEW CMK then import the new key material into that CMK (i.e. repeat the same process as creating a new key)
* You can delete imported keys immediately by deleting the Key Material.

Scenario #1: User disables a KMS key - event-driven security.
* User makes API call -> CloudTrail logs call -> CloudTrail sends Event Source to CloudWatch
* CloudWatch Event Rules is invoked -> Event Target for rule is a Lambda -> Lambda detects that user has disabled a key in KMS
* Lambda responds by auto re-enables key in KMS and/or fire off an SNS notification to security team.

Scenario #2: User disables a KMS key - AWS Config monitoring KMS events.
* AWS Config monitors and stores the KMS event into the Config S3 Bucket.
* Standard or Custom Rule (Lambda) is triggered which detects the KMS-disable.
* Rule will notify AWS Config -> AWS Config fires off SNS notification to security team.

Read the AWS KMS FAQ: https://aws.amazon.com/kms/faqs/

### KMS Key Rotation Options

Extensive re-use of encryption keys is not recommended.
Best practice is to rotate keys on a regular basis.
Frequency of key rotation is dependant on local laws, regulations and corporate policies.
Method of rotation depends on the type of key you are using.
1. AWS Managed Key
2. Customer Managed Key
3. Customer Managed w/ imported key material.

Key Rotation: AWS Managed Keys
* Automatic rotation every 3 years.
* No automatic rotation
* AWS manages everything and saves old backing key (key material)

Key Rotation: Customer Managed Keys
* Automatic rotation every 1 year (disabled by default)
* Manual rotation is possible
* Create a new CMK -> update apps / key-alias to use the new CMK (be careful of old-key deletion)

Key Rotation: Customer Managed Keys w/ Imported Key Material
* NO automatic rotation (key material is not generated in AWS)
* Manual rotation is the only option
* Create a new CMK -> update apps / key-alias to use the new CMK (be careful of old-key deletion)


### Using KMS with EBS

Using KMS to encrypt Elastic Block Storage (EBS) volumes.

Creating an EBS encrypted volume w/ AWS-managed key:
1. Create a new EC2
2. Provision EBS storage (not encrypted by default)
3. Turn on encryption for the attached EBS volume.
4. This will generate an AWS-managed key for EBS in KMS.
* You cannot modify/delete this AWS-managed key.

How to encrypt an existing EBS volume / the Root Device volume (default vol when launching an EC2):
1. Create an EBS volume.
2. Create a snapshot of the EBS volume.
3. Create an Amazon Machine Image (AMI) from the EBS snapshot (actions -> create image).
4. Copy the AMI to a new image -> turn on encryption -> select either AWS-managed or your own CMK.
5. Launch the AMI. Your Root Device volume will now be encrypted.


### EC2 and importing a Customer Managed Key Pair (for SSH access) - MAC USERS ONLY

1. Generate a private-key using RSA 2048 bits:
`$ openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048`

2. Generate a public-key:
`$ openssl rsa -pubout -in private_key.pem  -out public_key.pem`

3. Change permissions of private-key:
`$ chmod 400 private_key.pem`

4. Go to EC2 -> Key Pairs -> Import a Key Pair -> choose your public-key. Now you can provision an EC2 instance and select your public-key.

You CANNOT take your private/public-key pair and import it into KMS.
You must follow the external Key Material import process to generate a CMK.


### EC2 and Key Pairs (SSH access)

Creating additional/multiple key pairs for an EC2 instance.
1. Provision EC2 with an original key pair + SSH into instance `$ ssh ec2-user@public-ec2-ip -i KeyPairOriginal.pem`
2. Elevate to root `$ sudo su`
3. View your public keys by:
    * `$ cat ~/.ssh/authorized_keys` where authorized_keys contains all public keys.
    * OR by calling `$ curl http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key/`
4. Go to IAM -> create a new EC2 role -> provision `AmazonS3FullAccess` policy.
5. Go to EC2 -> attach new IAM role to instance.
6. Within the EC2, create a new S3 bucket: `$ aws s3 mb s3://brianec2keypairs`
7. Generate a new asymmetric key pair: `$ ssh-keygen -t rsa`
8. Add the new public key to authorized_keys `$ cat mynewkey.pub >> ~/.ssh/authorized_keys`.
9. Add the new private key to S3 bucket: `$ aws s3 cp mynewkey s3://brianec2keypairs`.
10. Go to S3 -> download new private key `mynewkey` -> `$ chmod 400 mynewkey`
11. Access the EC2 instance using the new private key `$ ssh ec2-user@ec2-public-ip -i mynewkey`

Notes about deleting Key Pairs:
* Deleting your key pair via. AWS Console will NOT prevent accessing EC2 with the private key, since the public key inside your EC2 in `~/.ssh/authorized_keys` still exists.
* If you delete an EC2 key pair via. AWS Console, you can generate a new key pair for the instance by:
    1. Go to the EC2 -> Actions -> Create an AMI.
    2. Go to AMIs -> launch the EC2 clone -> create a new key pair.
    3. Your new public key will be added to the existing list in `~/.ssh/authorized_keys`.
* Prevent access with old key pairs by removing the public keys in `~/.ssh/authorized_keys`.

Additional notes:
* You cannot use KMS with SSH for EC2 because Amazon is involved in generation of KMS keys.
* You can use CloudHSM with SSH for EC2 because you can export CloudHSM keys.

### AWS Marketplace Security Products

You can purchase security products from 3rd-party vendors on the AWS Marketplace.
* Includes: firewalls, hardened OS's, WAF's, Antivirus, Security Monitoring etc.
* Billed: free, hourly, monthly, annually, BYOL etc.
* Recommended reading: steps on CIS OS Hardening

### AWS Web Application Firewall (WAF) & AWS Shield

AWS Web Application Firewall (WAF): monitors/controls HTTP/HTTPS requests that are forwarded to CloudFront or an Application Load Balancer.
* Config includes: access based on IP, query string params.
* Offers 3 behaviours: (1) `ALLOW` (2) `BLOCK` (3) `COUNT`
* Additional protections based off: IP, Country, request header values, strings/regex in requests, request length, SQLi, XSS.

WAF deployment: done manually or via. CloudFormation template.
* Deploy WAF to CloudFront Distributions: global
* Deploy WAF to Application Load Balancer: region-specific

WebACL configuration example
* `CommonAttackProtectionManualIPBlockRule`: manually specify IPs to block
* `CommonAttackProtectionLargeBodyRule`: block requests w/ body size > limit
* `CommonAttackProtectionSqliRule`: block requests that indicate SQLi
* `CommonAttackProtectionXssRule`: block requests that indicate XSS

AWS Shield
* Basic-level turned on by default - $3,000/month for advanced-level.
* Advanced gives you an incident-response team + in-depth reporting.
* You won't pay if you are a victim of an attack.


### EC2 Dedicated Instances vs. EC2 Dedicated Hosts

EC2 Dedicated Instances
* Run in a VPC on dedicated physical hardware separate from other AWS accounts, for a single customer.
* Dedicated instances may share hardware with other non-dedicated instances in the same AWS account.
* Billing: per-instance basis
    * On-demand.
    * Reserved Instances - save up to 70%.
    * Spot Instances - save up to 90%.

EC2 Dedicated Hosts
* Also runs on dedicated physical hardware from other AWS accounts, for a single customer.
* Provides additional visibility and control over how instances are placed on a physical server.
* Consistently deploy instances to the same physical server each time.
* Enable you to use your existing server-bound software licenses (e.g. VMWare, Oracle licenses which might require dedicated hosts).
* Enable you to address corporate and regulatory compliance.
* Billing: per-host billing

Provision Dedicated Instances / Dedicated Hosts via. EC2 service when launching an instance.


### AWS Hypervisors, Isolation of AWS Resources, AWS Firewalls

AWS Hypervisor
* Hypervisor or virtual machine monitor (VMM) is software, firmware, hardware that creates an runs virtual machines.
    * Host machine: a computer on which a hypervisor runs 1+ virtual machines
    * Guest machine: each virtual machine
* EC2 runs on __Xen Hypervisors__: they can have guest OSs' running Paravirtualisation (PV) or using Hardware Virtual Machine (HVM).
    * HVM guests are fully virtualized: VMs on top of hypervisors are not aware that they are sharing processing time with other VMs.
    * PV is a lighter form of virtualisation and it used to be quicker.
    * Performance gap between HVM/PV is closed and AWS recommends using HVM over PV.
    * Windows EC2 instances can only be HVM where Linux can be HVM/PV.
* Paravirtualised guests
    * Relies on the hypervisor to provide support for operations that normally require privileged access.
    * Guest OS has no elevated access to the CPU.
    * CPU provides 4 separate privilege modes: 0-3 __"rings"__.
    * Host OS executes in __Ring 0__
    * Guest OS runs in lesser-privileged __Ring 1__ and applications in least-privileged __Ring 3__
    * E.g. `R0: Xen Hypervisor` | `R1: Linux instance` | `R3: Applications`

What happens when we interact with EC2:
1. Physical Interface
2. Firewall splits traffic (runs at Hypervisor-layer - AWS managed)
3. Traffic is split and isolated through our security groups, our virtual interface, the hypervisor back to our resources.

Hypervisor Access (by AWS employees)
* Administrators with a business need to access the management plane requires MFA to access the administration hosts.
* The administration hosts are systems that are specifically designed, built, configured and hardened to protect the management plane of the cloud.
* All access is logged and audited.
* When an employee no longer has business need to access the management plane, privileges and access to these hosts can be revoked.

Guest OS (EC2) Access (by customers)
* These virtual instances are controlled completely by customers.
* Full root access over accounts, services and applications running on the EC2.
* AWS have no access rights to our Guest OS in EC2.

Memory Scrubbing:
* EBS automatically resets every block of storage used by the customer, so one customer's data is never unintentionally exposed to another customer. (all storage and RAM memory)
* Memory allocated to guests is scrubbed/zeroed by the Hypervisor when it is unallocated to a guest.
* Memory is not returned to the pool of free memory available for new allocations until scrubbing is complete.
* I.e. disk-recovery tools to find other customer's data won't work.

### KMS Grants

KMS Grants are an alternate access control mechanism to a Key Policy
* Programmatically delegate use of KMS CMKs to other AWS principals (another user in your account / another account)
* Provide temp granular permissions (encrypt, decrypt, re-encrypt, describekey etc.)]
* Only grants ALLOWs, not DENYs
* Use Key Policies for static permissions, Grants for temp permissions.
* _Analogy: I give house keys to a friend to take care of my plants while I'm on holidays._

KMS Grants are configure programmatically via CLI
* _create-grant_: adds new grant to CMK, specifies who can use it and list of operations the grantee can perform. A grant token is generated and can be passed as an argument to a KMS API.
* _list-grants_: lists grants
* _revoke-grant_: remove a grant

Example: Providing "Encrypt" operation as grant to IAM user
```bash
#Create a new key and make a note of the region you are working in
aws kms create-key

#Test encrypting plain text using my new key:
aws kms encrypt --plaintext "hello" --key-id <key_arn>

#Create a new user called Dave and generate access key / secret access key
aws iam create-user --user-name dave
aws iam create-access-key --user-name dave

#Run aws configure using Dave's credentials creating a CLI profile for him
aws configure --profile dave
aws kms encrypt --plaintext "hello" --key-id <key_arn> --profile dave

#Create a grant for user called Dave
aws iam get-user --user-name dave
aws kms create-grant --key-id <key_arn> --grantee-principal <Dave\'s_arn> --operations "Encrypt"

#Encrypt plain text as user Dave:
aws kms encrypt --plaintext "hello" --key-id <key_arn> --grant-tokens <grant_token_from_previous_command> --profile dave

#Revoke the grant:
aws kms list-grants --key-id <key_arn>
aws kms revoke-grant --key-id <key_arn> --grant-id <grant_id>

#Check that the revoke was successful:
aws kms encrypt --plaintext "hello" --key-id <key_arn> --profile dave

https://docs.aws.amazon.com/cli/latest/reference/kms/create-grant.html
```

### KMS Policy Conditions - ViaService

Policy Conditions can be used to specify a condition within a Key Policy or IAM Policy

KMS provides a set of predefined __Condition Keys__.
* See https://docs.aws.amazon.com/kms/latest/developerguide/policy-conditions.html.

Use __kms:ViaService__ to allow or deny access to your CMK according to which service the request originated from.
* Only for services that are integrated with KMS e.g. S3, EBS, RDS, Systems Manager, SQS, Lambda

ViaService example: CMK may be used for "Encrypt" action ONLY if request comes from EC2/RDS from the specified regions
```json
"Effect": "Allow",
"Principal": {
    "AWS": "arn:xxx:xxx:xxx/ExampleUser"
},
"Action":[
    "kms:Encrypt",
]
"Resource":"*",
"Condition":{
    "StringEquals":{
        "kms:ViaService":[
            "ec2.us-west-2.amazonaws.com",
            "rds.us-west-2.amazonaws.com",
        ]
    }
}
```

### KMS Cross Account Access for CMKs

2 steps to provide cross-account access.

* Example: Users in account HELLO need to use a CMK in account WORLD
1. Change the Key Policy for the CMK in account WORLD to allow ROOT USER in HELLO to have access. (doesn't have to be root account, can specify a specific user/role ARN instead)
2. Set up an IAM user/role in HELLO with explicit permission to use the CMK in WORD.

Example IAM policy in account HELLO for cross account access to CMK in WORLD
```json
{
    "Statement":[
        {
            "Sid": "AllowUseOfCMKInAccountWORLD",
            "Effect": "Allow",
            "Action":[
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:ReEncrypt*"
            ],
            "Resource": "arn:aws:kms:us-west-2:WORLD:key/guid"
        }
    ]
}
```


### Microservices

Monolithic applications
* Difficult to change.
* Can't make it bigger.
* One small mistake affects entire application.

Microservices
* Software is composed of small, independent services that communicate over well-defined APIs.
* Modern apps are usually made up of containers - a standardised unit which includes everything that your software needs to run e.g. libraries, system tools, runtime environment.

(ADVANTAGE #1) Serviceability: Easy to fix problems
* if one component breaks... Not A Disaster: the rest of the application keeps running.
* if one component breaks... Quick To Fix: deploy a new instance of your microservice/container to replace the broken one.

(ADVANTAGE #2) Flexibility: Easy to make changes
* to upgrade a Shopping Cart feature... you only need to replace the shopping cart microservice / deploy new containers.
* to add new features... e.g. add a product search feature, just add it as a new microservice. No need to redeploy the entire application.

(ADVANTAGE #2) Scalability: Easy to scale
* to scale the Shopping Cart microservice due to increased customer demand... just add more containers running Shopping Carts.
* Scale only components you need to = highly flexible and cost efficient applications.


### Containers in AWS

Containers are a virtual operating environment.
* A standardised unit with everything that the software needs to run e.g. libraries, system code and runtime.
* Used to support microservices architecture.
* Use Docker to create Linux containers.
* Use Windows Containers for Windows workloads.

Architecture of a Docker container
*  Container components:
    * (1) Code (2) Libraries (3) Virtual Kernel.
    * Runs on Docker.
    * Installed on host Operating System.
* Scaling application or building new features for the application = add more containers.

Where to run containers in AWS
* __Elastic Container Service (ECS)__
    * Fargate is the preferred option - Serverless.
    * Or managed clusters of EC2 instances.
    * Deep integration with AWS services e.g. IAM, VPC, Route53.
    * Used internally e.g. amazon.com, Sagemaker, Amazon Lex.
* __Elastic Kubernetes Service (EKS)__
    * Fargate is the preferred option - Serverless.
    * Or managed clusters of EC2 instances.
    * Certified Kubernetes conformant.
    * Benefit of open-source tooling from the community.
* Both above services are used for running and orchestrating containers and are a fully-managed Platform-As-A-Service (PaaS) service offering e.g. no need to install Docker, configure clusters, managing shared storing etc.
* Both provide a managed environment to run your containers.
* ECS has deep integration with AWS services vs. EKS benefits from the open-source community.

Elastic Container Service (ECS)
1. Container definition: choose a container image.
2. Task definition: describes your container attributes.
    * VPC, task execution role, Fargate/EC2, task memory, task CPU.
    * You can group multiple containers under a single task.
3. Service definition: a services allows you to run and maintain a specified number of simultaneous instances of a desk definition in an ECS cluster.
    * This makes sure an application remains up and running if something fails, as another instance of the task will be launched.
4. Configure cluster.


### Container Security

1. Don't store secrets
* Use IAM roles instead of hardcoding user credentials.
* Use Secrets Manager for RDS credentials, API keys.
* Use Amazon Certificate Manager (ACM) if you have TLS certificates to store and manage.

2. Don't run as root
* Don't run containers using your AWS Root account.
* Don't run containers in EC2 as Root.

3. Less is more
* Minimise your attack surface: only run one service in your container.
* Avoid unnecessary libraries: remove code/libraries you don't need in your container image.

4. Use trusted images only
* Avoid public repositories, where you don't know the origin of the code.
* Use images from a trusted source or ones created in-house.
* Scan for CVE's using Amazon Inspector or external tools.
* __AWS Elastic Container Registry (ECR)__: a container registry where you can store your own container images e.g. Docker or Windows Container images and make them available to ECS.
    * AWS provides image scanning for container images stored in ECR and reports on any CVEs.

5. Infrastructure security
* Avoid the public internet use ECS Interface Endpoints (similar to VPC endpoints).
* If you must use public internet, Use TLS to secure end-to-end communication between end-users and your applications running in containers.
* If you are using TLS certificates, best-practice is to use __Amazon Certificate Manager (ACM)__ as it provides a single, central interface for storing and managing certificates and it integrates well with many AWS services.
* Read https://aws.amazon.com/blogs/compute/maintaining-transport-layer-security-all-the-way-to-your-container-part-2-using-aws-certificate-manager-private-certificate-authority/.