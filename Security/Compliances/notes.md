## PCI-DSS

### Requirement 1 - Firewalls
Install and maintain a firewall configuration to protect cardholder data.

| Cloud                                                             | Category                | Plugin                                  | Description                                                                                                  |
| ----------------------------------------------------------------- | ----------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| ![](https://cloud.aquasec.com/assets/img/clouds/oracle-small.png) | Database                | DB Network Security Groups Enabled      | Ensures that all databases have network security groups enabled.                                             |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | EC2                     | Excessive Security Groups               | Determine if there are an excessive number of security groups in the account                                 |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | EC2                     | Detect EC2 Classic Instances            | Ensures AWS VPC is being used for instances instead of EC2 Classic                                           |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | EC2                     | Default Security Group                  | Ensure the default security groups block all traffic by default                                              |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | EC2                     | Open All Ports Protocols                | Determine if security group has all ports or protocols open to the public                                    |
| ![](https://cloud.aquasec.com/assets/img/clouds/azure-small.png)  | Log Alerts              | SQL Server Firewall Rule Alerts Monitor | Ensures Activity Log Alerts for the create or update and delete SQL Server Firewall Rules events are enabled |
| ![](https://cloud.aquasec.com/assets/img/clouds/azure-small.png)  | Log Alerts              | Virtual Network Alerts Monitor          | Ensures Activity Log Alerts for the create or update and delete Virtual Networks events are enabled          |
| ![](https://cloud.aquasec.com/assets/img/clouds/azure-small.png)  | Network Security Groups | Default Security Group                  | Ensures that default security groups block all traffic by default                                            |
| ![](https://cloud.aquasec.com/assets/img/clouds/azure-small.png)  | Network Security Groups | Open All Ports                          | Ensures Network Security Groups do not expose all ports to the public                                        |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | RDS                     | RDS Publicly Accessible                 | Ensures RDS instances are not launched into the public cloud                                                 |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | Redshift                | Redshift Publicly Accessible            | Ensures Redshift clusters are not launched into the public cloud                                             |
| ![](https://cloud.aquasec.com/assets/img/clouds/azure-small.png)  | Storage Accounts        | Network Access Default Action           | Ensures that Storage Account access is restricted to trusted networks                                        |
| ![](https://cloud.aquasec.com/assets/img/clouds/google-small.png) | VPC Network             | Excessive Firewall Rules                | Determines if there are an excessive number of firewall rules in the account                                 |
| ![](https://cloud.aquasec.com/assets/img/clouds/google-small.png) | VPC Network             | Open All Ports                          | Determines if all ports are open to the public                                                               |

### Requirement 2 - Defaults
Do not use vendor-supplied defaults for system passwords and other security parameters.


| Cloud                                                             | Category    | Plugin                | Description                                                                 |
| ----------------------------------------------------------------- | ----------- | --------------------- | --------------------------------------------------------------------------- |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | KMS         | KMS Default Key Usage | Checks AWS services to ensure the default KMS key is not being used         |
| ![](https://cloud.aquasec.com/assets/img/clouds/google-small.png) | VPC Network | Default VPC In Use    | Determines whether the default VPC is being used for launching VM instances |


### Requirement 3 - Cardholder Data
Protect stored cardholder data.

| Cloud                                                             | Category           | Plugin                      | Description                                                             |
| ----------------------------------------------------------------- | ------------------ | --------------------------- | ----------------------------------------------------------------------- |
| ![](https://cloud.aquasec.com/assets/img/clouds/google-small.png) | Compute            | CSEK Encryption Enabled     | Ensures Customer Supplied Encryption Key Encryption is enabled on disks |
| ![](https://cloud.aquasec.com/assets/img/clouds/google-small.png) | Cryptographic Keys | Key Rotation                | Ensures cryptographic keys are set to rotate on a regular schedule      |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | EC2                | EBS Encryption Enabled      | Ensures EBS volumes are encrypted at rest                               |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | KMS                | KMS Key Rotation            | Ensures KMS keys are set to rotate on a regular schedule                |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | RDS                | RDS Encryption Enabled      | Ensures at-rest encryption is setup for RDS instances                   |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | SQS                | SQS Encrypted               | Ensures SQS encryption is enabled                                       |
| ![](https://cloud.aquasec.com/assets/img/clouds/azure-small.png)  | Storage Accounts   | Storage Accounts Encryption | Ensures encryption is enabled for Storage Accounts                      |
| ![](https://cloud.aquasec.com/assets/img/clouds/azure-small.png)  | Virtual Machines   | VM OS Disk Encryption       | Ensures that VM OS Disk Encryption is enabled for virtual machines      |
| ![](https://cloud.aquasec.com/assets/img/clouds/azure-small.png)  | Virtual Machines   | VM Data Disk Encryption     | Ensure that Data Disk Encryption is enabled for virtual machines        |

### Requirement 4 - Encrypted Transmission
Encrypt transmission of cardholder data across open, public networks

| Cloud                                                             | Category         | Plugin                         | Description                                                                                                   |
| ----------------------------------------------------------------- | ---------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| ![](https://cloud.aquasec.com/assets/img/clouds/azure-small.png)  | App Service      | HTTPS Only Enabled             | Ensures HTTPS Only is enabled for App Services, redirecting all HTTP traffic to HTTPS                         |
| ![](https://cloud.aquasec.com/assets/img/clouds/azure-small.png)  | CDN Profiles     | Detect Insecure Custom Origin  | Ensures that HTTPS is enabled for CDN endpoints with a custom origin                                          |
| ![](https://cloud.aquasec.com/assets/img/clouds/google-small.png) | CLB              | CLB HTTPS Only                 | Ensures CLBs are configured to only accept connections on HTTPS ports                                         |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | CloudFront       | Insecure CloudFront Protocols  | Detects the use of insecure HTTPS SSL/TLS protocols for use with HTTPS traffic between viewers and CloudFront |
| ![](https://cloud.aquasec.com/assets/img/clouds/oracle-small.png) | Compute          | Boot Volume Transit Encryption | Ensures in-transit data encryption is enabled on boot volumes.                                                |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | ELB              | Insecure Ciphers               | Detect use of insecure ciphers on ELBs                                                                        |
| ![](https://cloud.aquasec.com/assets/img/clouds/google-small.png) | SQL              | Database SSL Enabled           | Ensures SQL databases have SSL enabled                                                                        |
| ![](https://cloud.aquasec.com/assets/img/clouds/azure-small.png)  | Storage Accounts | Storage Accounts HTTPS         | Ensures HTTPS-only traffic is allowed to storage account endpoints                                            |

### Requirement 5 - Anti-Virus and Malware
Protect all systems against malware and regularly update anti-virus software or programs.

| Cloud                                                            | Category         | Plugin                 | Description                                                             |
| ---------------------------------------------------------------- | ---------------- | ---------------------- | ----------------------------------------------------------------------- |
| ![](https://cloud.aquasec.com/assets/img/clouds/azure-small.png) | Virtual Machines | VM Endpoint Protection | Ensures that VM Endpoint Protection is enabled for all virtual machines |

### Requirement 6 - Secure Systems
Develop and maintain secure systems and applications.

| Cloud                                                             | Category      | Plugin                      | Description                                                                      |
| ----------------------------------------------------------------- | ------------- | --------------------------- | -------------------------------------------------------------------------------- |
| ![](https://cloud.aquasec.com/assets/img/clouds/google-small.png) | Compute       | OS Login Enabled            | Ensures OS login is enabled for the project                                      |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | ConfigService | Config Service Enabled      | Ensures the AWS Config Service is enabled to detect changes to account resources |
| ![](https://cloud.aquasec.com/assets/img/clouds/oracle-small.png) | Database      | DB Private Subnet Only      | Ensures that all database systems are in private subnets only.                   |
| ![](https://cloud.aquasec.com/assets/img/clouds/oracle-small.png) | Identity      | Password Requires Lowercase | Ensures password policy requires at least one lowercase letter.                  |
| ![](https://cloud.aquasec.com/assets/img/clouds/oracle-small.png) | Identity      | Password Requires Numbers   | Ensures password policy requires at least one number.                            |
| ![](https://cloud.aquasec.com/assets/img/clouds/oracle-small.png) | Identity      | Password Requires Symbols   | Ensures password policy requires at least one symbol.                            |
| ![](https://cloud.aquasec.com/assets/img/clouds/oracle-small.png) | Identity      | Password Requires Uppercase | Ensures password policy requires at least one uppercase character.               |
| ![](https://cloud.aquasec.com/assets/img/clouds/oracle-small.png) | Identity      | Minimum Password Length     | Ensures password policy requires a minimum password length.                      |

### Requirement 7 - Restrict Access
Restrict access to cardholder data by business need to know.

| Cloud                                                             | Category                | Plugin                        | Description                                                                                                     |
| ----------------------------------------------------------------- | ----------------------- | ----------------------------- | --------------------------------------------------------------------------------------------------------------- |
| ![](https://cloud.aquasec.com/assets/img/clouds/azure-small.png)  | App Service             | Authentication Enabled        | Ensures Authentication is enabled for App Services, redirecting unauthenticated users to the login page.        |
| ![](https://cloud.aquasec.com/assets/img/clouds/azure-small.png)  | Blob Service            | Blob Container Private Access | Ensures that all blob containers do not have anonymous public access set                                        |
| ![](https://cloud.aquasec.com/assets/img/clouds/google-small.png) | Compute                 | VM Instances Least Privilege  | Ensures that instances are not configured to use the default service account with full access to all cloud APIs |
| ![](https://cloud.aquasec.com/assets/img/clouds/azure-small.png)  | File Service            | File Service All Access ACL   | Ensures file shares do not allow full write, delete, or read ACL permissions                                    |
| ![](https://cloud.aquasec.com/assets/img/clouds/oracle-small.png) | File Storage            | NFS Public Access             | Ensures that all file systems do not have public access.                                                        |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | IAM                     | Root Account In Use           | Ensures the root account is not being actively used                                                             |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | IAM                     | IAM User Admins               | Ensures the number of IAM admins in the account are minimized                                                   |
| ![](https://cloud.aquasec.com/assets/img/clouds/oracle-small.png) | Identity                | Users MFA Enabled             | Ensures a multi-factor authentication device is enabled for all users within the account.                       |
| ![](https://cloud.aquasec.com/assets/img/clouds/azure-small.png)  | Network Security Groups | Open All Ports                | Ensures Network Security Groups do not expose all ports to the public                                           |
| ![](https://cloud.aquasec.com/assets/img/clouds/oracle-small.png) | Object Store            | Bucket Public Access Type     | Ensures object store buckets do not allow global write, delete, or read permissions                             |
| ![](https://cloud.aquasec.com/assets/img/clouds/azure-small.png)  | Queue Service           | Queue Service All Access ACL  | Ensures queues do not allow full write, delete, or read ACL permissions                                         |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | S3                      | S3 Bucket All Users Policy    | Ensures S3 bucket policies do not allow global write, delete, or read permissions                               |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | S3                      | S3 Bucket All Users ACL       | Ensures S3 buckets do not allow global write, delete, or read ACL permissions                                   |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | SQS                     | SQS Cross Account Access      | Ensures SQS policies disallow cross-account access                                                              |
| ![](https://cloud.aquasec.com/assets/img/clouds/azure-small.png)  | Table Service           | Table Service All Access ACL  | Ensures tables do not allow full write, delete, or read ACL permissions                                         |

### Requirement 8 - Identify Access
Identify and authenticate access to system components.

| Cloud                                                             | Category     | Plugin                        | Description                                                                                                       |
| ----------------------------------------------------------------- | ------------ | ----------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| ![](https://cloud.aquasec.com/assets/img/clouds/azure-small.png)  | App Service  | Authentication Enabled        | Ensures Authentication is enabled for App Services, redirecting unauthenticated users to the login page.          |
| ![](https://cloud.aquasec.com/assets/img/clouds/azure-small.png)  | Blob Service | Blob Container Private Access | Ensures that all blob containers do not have anonymous public access set                                          |
| ![](https://cloud.aquasec.com/assets/img/clouds/oracle-small.png) | File Storage | NFS Public Access             | Ensures that all file systems do not have public access.                                                          |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | IAM          | Minimum Password Length       | Ensures password policy requires a password of at least a minimum number of characters                            |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | IAM          | Password Requires Symbols     | Ensures password policy requires the use of symbols                                                               |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | IAM          | Maximum Password Age          | Ensures password policy requires passwords to be reset every 180 days                                             |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | IAM          | Password Reuse Prevention     | Ensures password policy prevents previous password reuse                                                          |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | IAM          | Root MFA Enabled              | Ensures a multi-factor authentication device is enabled for the root account                                      |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | IAM          | Users MFA Enabled             | Ensures a multi-factor authentication device is enabled for all users within the account                          |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | IAM          | Access Keys Rotated           | Ensures access keys are not older than 180 days in order to reduce accidental exposures                           |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | IAM          | Access Keys Last Used         | Detects access keys that have not been used for a period of time and that should be decommissioned                |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | IAM          | Password Expiration           | Ensures password policy enforces a password expiration                                                            |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | IAM          | Password Requires Lowercase   | Ensures password policy requires at least one lowercase letter                                                    |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | IAM          | Password Requires Numbers     | Ensures password policy requires the use of numbers                                                               |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | IAM          | Password Requires Uppercase   | Ensures password policy requires at least one uppercase letter                                                    |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | IAM          | Users Password Last Used      | Detects users with password logins that have not been used for a period of time and that should be decommissioned |

## Requirement 9 - Physical Access
Restrict physical access to cardholder data.

No plugins have been mapped to this control.


### Requirement 10 - Track Access
Track and monitor all access to network resources and cardholder data.


| Cloud                                                             | Category   | Plugin                           | Description                                                                                   |
| ----------------------------------------------------------------- | ---------- | -------------------------------- | --------------------------------------------------------------------------------------------- |
| ![](https://cloud.aquasec.com/assets/img/clouds/oracle-small.png) | Audit      | Log Retention Period             | Ensures that the audit log retention period is configured correctly.                          |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | CloudFront | CloudFront Logging Enabled       | Ensures CloudFront distributions have request logging enabled.                                |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | CloudTrail | CloudTrail Enabled               | Ensures CloudTrail is enabled for all regions within an account                               |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | CloudTrail | CloudTrail Bucket Access Logging | Ensures CloudTrail logging bucket has access logging enabled to detect tampering of log files |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | EC2        | VPC Flow Logs Enabled            | Ensures VPC flow logs are enabled for traffic logging                                         |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | ELB        | ELB Logging Enabled              | Ensures load balancers have request logging enabled.                                          |
| ![](https://cloud.aquasec.com/assets/img/clouds/google-small.png) | Logging    | Project Ownership Logging        | Ensures that logging and log alerts exist for project ownership assignments and changes       |
| ![](https://cloud.aquasec.com/assets/img/clouds/google-small.png) | Logging    | Storage Permissions Logging      | Ensures that logging and log alerts exist for storage permission changes                      |
| ![](https://cloud.aquasec.com/assets/img/clouds/google-small.png) | Logging    | VPC Network Logging              | Ensures that logging and log alerts exist for VPC network changes                             |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | S3         | S3 Bucket Logging                | Ensures S3 bucket logging is enabled for S3 buckets                                           |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | Transfer   | Transfer Logging Enabled         | Ensures AWS Transfer servers have CloudWatch logging enabled.                                 |

### Requirement 11 - Test Systems
Regularly test security systems and processes.

| Cloud                                                             | Category | Plugin         | Description                                             |
| ----------------------------------------------------------------- | -------- | -------------- | ------------------------------------------------------- |
| ![](https://cloud.aquasec.com/assets/img/clouds/aws-small.png)    | RDS      | RDS Restorable | Ensures RDS instances can be restored to a recent point |
| ![](https://cloud.aquasec.com/assets/img/clouds/google-small.png) | SQL      | DB Restorable  | Ensures SQL instances can be restored to a recent point |

### Requirement 12 - Policy
Maintain a policy that addresses information security for all personnel.

No plugins have been mapped to this control.


## CIS 1.2 | Google Cloud Platform


| Version |  Date  |
| ------- | ------ |
| 1.2 | 04/06/2021 |


| ID   | Services                     | Policies                                                     |
| ---- | ---------------------------- | ------------------------------------------------------------ |
| 1    | Identity & Access Management | 1.1 Ensure that corporate login credentials are used.<br>1.2 Ensure that multi-factor authentication is enabled for all non-service accounts.<br>1.3 Ensure that Security Key Enforcement is enabled for all admin accounts.<br>1.4 Ensure that there are only GCP-managed service account keys for each service account.<br>1.5 Ensure that Service Account has no Admin privileges.<br>1.6 Ensure that IAM users are not assigned the Service Account User or Service Account Token Creator roles at the project level.<br>1.7 Ensure user-managed/external keys for service accounts are rotated every 90 days or less.<br>1.8 Ensure that Separation of duties is enforced while assigning service account-related roles to users.<br>1.9 Ensure that Cloud KMS crypto keys are not anonymously or publicly accessible.<br>1.10 Ensure KMS encryption keys are rotated within a period of 90 days.<br>1.11 Ensure that Separation of duties is enforced while assigning KMS related roles to users.<br>1.12 Ensure API keys are not created for a project.<br>1.13 Ensure API keys are restricted to use by only specified Hosts and Apps.<br>1.14 Ensure API keys are restricted to the only APIs that the application needs access to.<br>1.15 Ensure API keys are rotated every 90 days. |
| 2    | VPC & Networking             | 3.1 Ensure that the default network does not exist in a project.<br>3.2 Ensure legacy networks do not exist for a project.<br>3.3 Ensure that DNSSEC is enabled for Cloud DNS.<br>3.4 Ensure that RSASHA1 is not used for the key-signing key in Cloud DNS DNSSEC.<br>3.5 Ensure that RSASHA1 is not used for the zone-signing key in Cloud DNS DNSSEC.<br>3.6 Ensure that SSH access is restricted from the internet.<br>3.7 Ensure that RDP access is restricted from the Internet.<br>3.8 Ensure that VPC Flow Logs are enabled for every subnet in a VPC Network.<br>3.9 Ensure no HTTPS or SSL proxy load balancers permit SSL policies with weak cipher suites.<br>3.10 Ensure Firewall Rules for instances behind Identity Aware Proxy (IAP) only allow the traffic from Google Cloud Loadbalancer (GCLB) Health Check and Proxy Addresses. |
| 3    | Compute Instances            | 4.1 Ensure that instances are not configured to use the default service account.<br>4.2 Ensure that instances are not configured to use the default service account with full access to all Cloud APIs.<br>4.3 Ensure “Block Project-wide SSH keys” is enabled for VM instances.<br>4.4 Ensure OSLOGIN is enabled for a Project.<br>4.5 Ensure ‘Enable connecting to serial ports’ is not enabled for VM Instance.<br>4.6 Ensure that IP forwarding is not enabled on Instances.<br>4.7 Ensure VM disks for critical VMs are encrypted with Customer-Supplied Encryption Keys (CSEK).<br>4.8 Ensure Compute instances are launched with Shielded VM enabled.<br>4.9 Ensure that Compute instances do not have public IP addresses.<br>4.10 Ensure that App Engine applications enforce HTTPS connections.<br>4.11 Ensure that Compute instances have Confidential Computing enabled. |
| 4    | Storage                      | 5.1 Ensure that Cloud Storage bucket is not anonymously or publicly accessible.<br>5.2 Ensure that Cloud Storage buckets have uniform bucket-level access enabled () |
| 5    | Cloud SQL                    | 6.1 MySQL Database<br>6.1.1 Ensure that a MySQL database instance does not allow anyone to connect with administrative privileges<br>6.1.2 Ensure ‘skip\_show\_database’ database flag for Cloud SQL Mysql instance is set to ‘on’<br>6.1.3 Ensure that the ‘local\_infile’ database flag for a Cloud SQL Mysql instance is set to ‘off’<br>6.2 PostgreSQL Database 179<br>6.2.1 Ensure that the ‘log\_checkpoints’ database flag for Cloud SQL PostgreSQL instance is set to ‘on’<br>6.2.2 Ensure ‘log\_error\_verbosity’ database flag for Cloud SQL PostgreSQL instance is set to ‘DEFAULT’ or stricter (Manual)<br>6.2.3 Ensure that the ‘log\_connections’ database flag for Cloud SQL PostgreSQL instance is set to ‘on’<br>6.2.4 Ensure that the ‘log\_disconnections’ database flag for Cloud SQL PostgreSQL instance is set to ‘on’<br>6.2.5 Ensure ‘log\_duration’ database flag for Cloud SQL PostgreSQL instance is set to ‘on’ (Manual)<br>6.2.6 Ensure that the ‘log\_lock\_waits’ database flag for Cloud SQL PostgreSQL instance is set to ‘on’<br>6.2.7 Ensure ‘log\_statement’ database flag for Cloud SQL PostgreSQL instance is set appropriately (Manual)<br>6.2.8 Ensure ‘log\_hostname’ database flag for Cloud SQL PostgreSQL instance is set appropriately<br>6.2.9 Ensure ‘log\_parser\_stats’ database flag for Cloud SQL PostgreSQL instance is set to ‘off’<br>6.2.10 Ensure ‘log\_planner\_stats’ database flag for Cloud SQL PostgreSQL instance is set to ‘off’<br>6.2.11 Ensure ‘log\_executor\_stats’ database flag for Cloud SQL PostgreSQL instance is set to ‘off’<br>6.2.12 Ensure ‘log\_statement\_stats’ database flag for Cloud SQL PostgreSQL instance is set to ‘off’<br>6.2.13 Ensure that the ‘log\_min\_messages’ database flag for Cloud SQL PostgreSQL instance is set appropriately (Manual).<br>6.2.14 Ensure ‘log\_min\_error\_statement’ database flag for Cloud SQL PostgreSQL instance is set to ‘Error’ or stricter<br>6.2.15 Ensure that the ‘log\_temp\_files’ database flag for Cloud SQL PostgreSQL instance is set to ‘0’ (on)<br>6.2.16 Ensure that the ‘log\_min\_duration\_statement’ database flag for Cloud SQL PostgreSQL instance is set to ‘-1’ (disabled)<br>6.3 SQL Server 228<br>6.3.1 Ensure ‘external scripts enabled’ database flag for Cloud SQL SQL Server instance is set to ‘off’<br>6.3.2 Ensure that the ‘cross DB ownership chaining’ database flag for Cloud SQL SQL Server instance is set to ‘off’<br>6.3.3 Ensure ‘user connections’ database flag for Cloud SQL SQL Server instance is set as appropriate<br>6.3.4 Ensure ‘user options’ database flag for Cloud SQL SQL Server instance is not configured<br>6.3.5 Ensure ‘remote access’ database flag for Cloud SQL SQL Server instance is set to ‘off’<br>6.3.6 Ensure ‘3625 (trace flag)’ database flag for Cloud SQL SQL Server instance is set to ‘off’<br>6.3.7 Ensure that the ‘contained database authentication’ database flag for Cloud SQL on the SQL Server instance is set to ‘off’<br>6.4 Ensure that the Cloud SQL database instance requires all incoming connections to use SSL<br>6.5 Ensure that Cloud SQL database instances are not open to the world<br>6.6 Ensure that Cloud SQL database instances do not have public IPs<br>6.7 Ensure that Cloud SQL database instances are configured with automated backups |
| 6    | Logging & Monitoring         | 2.1 Ensure that Cloud Audit Logging is configured properly across all services and all users from a project.<br>2.2 Ensure that sinks are configured for all log entries.<br>2.3 Ensure that retention policies on log buckets are configured using Bucket Lock.<br>2.4 Ensure log metric filter and alerts exist for project ownership assignments/changes.<br>2.5 Ensure that the log metric filter and alerts exist for Audit Configuration changes.<br>2.6 Ensure that the log metric filter and alerts exist for Custom Role changes.<br>2.7 Ensure that the log metric filter and alerts exist for VPC Network Firewall rule changes.<br>2.8 Ensure that the log metric filter and alerts exist for VPC network route changes.<br>2.9 Ensure that the log metric filter and alerts exist for VPC network changes.<br>2.10 Ensure that the log metric filter and alerts exist for Cloud Storage IAM permission changes.<br>2.11 Ensure that the log metric filter and alerts exist for SQL instance configuration changes.<br>2.12 Ensure that Cloud DNS logging is enabled for all VPC networks. |