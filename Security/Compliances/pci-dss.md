## Payment Card Industry Data Security Standard

### Requirement 1 - Firewalls

Install and maintain a firewall configuration to protect cardholder data.

| Cloud  | Category                | Plugin                                  | Description                                                                                                  |
| ------ | ----------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Oracle | Database                | DB Network Security Groups Enabled      | Ensures that all databases have network security groups enabled.                                             |
| AWS    | EC2                     | Excessive Security Groups               | Determine if there are an excessive number of security groups in the account                                 |
| AWS    | EC2                     | Detect EC2 Classic Instances            | Ensures AWS VPC is being used for instances instead of EC2 Classic                                           |
| AWS    | EC2                     | Default Security Group                  | Ensure the default security groups block all traffic by default                                              |
| AWS    | EC2                     | Open All Ports Protocols                | Determine if security group has all ports or protocols open to the public                                    |
| Azure  | Log Alerts              | SQL Server Firewall Rule Alerts Monitor | Ensures Activity Log Alerts for the create or update and delete SQL Server Firewall Rules events are enabled |
| Azure  | Log Alerts              | Virtual Network Alerts Monitor          | Ensures Activity Log Alerts for the create or update and delete Virtual Networks events are enabled          |
| Azure  | Network Security Groups | Default Security Group                  | Ensures that default security groups block all traffic by default                                            |
| Azure  | Network Security Groups | Open All Ports                          | Ensures Network Security Groups do not expose all ports to the public                                        |
| AWS    | RDS                     | RDS Publicly Accessible                 | Ensures RDS instances are not launched into the public cloud                                                 |
| AWS    | Redshift                | Redshift Publicly Accessible            | Ensures Redshift clusters are not launched into the public cloud                                             |
| Azure  | Storage Accounts        | Network Access Default Action           | Ensures that Storage Account access is restricted to trusted networks                                        |
| GCP    | VPC Network             | Excessive Firewall Rules                | Determines if there are an excessive number of firewall rules in the account                                 |
| GCP    | VPC Network             | Open All Ports                          | Determines if all ports are open to the public                                                               |

### Requirement 2 - Defaults

Do not use vendor-supplied defaults for system passwords and other security parameters.

| Cloud | Category    | Plugin                | Description                                                                 |
| ----- | ----------- | --------------------- | --------------------------------------------------------------------------- |
| AWS   | KMS         | KMS Default Key Usage | Checks AWS services to ensure the default KMS key is not being used         |
| GCP   | VPC Network | Default VPC In Use    | Determines whether the default VPC is being used for launching VM instances |

### Requirement 3 - Cardholder Data

Protect stored cardholder data.

| Cloud | Category           | Plugin                      | Description                                                             |
| ----- | ------------------ | --------------------------- | ----------------------------------------------------------------------- |
| GCP   | Compute            | CSEK Encryption Enabled     | Ensures Customer Supplied Encryption Key Encryption is enabled on disks |
| GCP   | Cryptographic Keys | Key Rotation                | Ensures cryptographic keys are set to rotate on a regular schedule      |
| AWS   | EC2                | EBS Encryption Enabled      | Ensures EBS volumes are encrypted at rest                               |
| AWS   | KMS                | KMS Key Rotation            | Ensures KMS keys are set to rotate on a regular schedule                |
| AWS   | RDS                | RDS Encryption Enabled      | Ensures at-rest encryption is setup for RDS instances                   |
| AWS   | SQS                | SQS Encrypted               | Ensures SQS encryption is enabled                                       |
| Azure | Storage Accounts   | Storage Accounts Encryption | Ensures encryption is enabled for Storage Accounts                      |
| Azure | Virtual Machines   | VM OS Disk Encryption       | Ensures that VM OS Disk Encryption is enabled for virtual machines      |
| Azure | Virtual Machines   | VM Data Disk Encryption     | Ensure that Data Disk Encryption is enabled for virtual machines        |

### Requirement 4 - Encrypted Transmission

Encrypt transmission of cardholder data across open, public networks

| Cloud  | Category         | Plugin                         | Description                                                                                                   |
| ------ | ---------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| Azure  | App Service      | HTTPS Only Enabled             | Ensures HTTPS Only is enabled for App Services, redirecting all HTTP traffic to HTTPS                         |
| Azure  | CDN Profiles     | Detect Insecure Custom Origin  | Ensures that HTTPS is enabled for CDN endpoints with a custom origin                                          |
| GCP    | CLB              | CLB HTTPS Only                 | Ensures CLBs are configured to only accept connections on HTTPS ports                                         |
| AWS    | CloudFront       | Insecure CloudFront Protocols  | Detects the use of insecure HTTPS SSL/TLS protocols for use with HTTPS traffic between viewers and CloudFront |
| Oracle | Compute          | Boot Volume Transit Encryption | Ensures in-transit data encryption is enabled on boot volumes.                                                |
| AWS    | ELB              | Insecure Ciphers               | Detect use of insecure ciphers on ELBs                                                                        |
| GCP    | SQL              | Database SSL Enabled           | Ensures SQL databases have SSL enabled                                                                        |
| Azure  | Storage Accounts | Storage Accounts HTTPS         | Ensures HTTPS-only traffic is allowed to storage account endpoints                                            |

### Requirement 5 - Anti-Virus and Malware

Protect all systems against malware and regularly update anti-virus software or programs.

| Cloud | Category         | Plugin                 | Description                                                             |
| ----- | ---------------- | ---------------------- | ----------------------------------------------------------------------- |
| Azure | Virtual Machines | VM Endpoint Protection | Ensures that VM Endpoint Protection is enabled for all virtual machines |

### Requirement 6 - Secure Systems

Develop and maintain secure systems and applications.

| Cloud  | Category      | Plugin                      | Description                                                                      |
| ------ | ------------- | --------------------------- | -------------------------------------------------------------------------------- |
| GCP    | Compute       | OS Login Enabled            | Ensures OS login is enabled for the project                                      |
| AWS    | ConfigService | Config Service Enabled      | Ensures the AWS Config Service is enabled to detect changes to account resources |
| Oracle | Database      | DB Private Subnet Only      | Ensures that all database systems are in private subnets only.                   |
| Oracle | Identity      | Password Requires Lowercase | Ensures password policy requires at least one lowercase letter.                  |
| Oracle | Identity      | Password Requires Numbers   | Ensures password policy requires at least one number.                            |
| Oracle | Identity      | Password Requires Symbols   | Ensures password policy requires at least one symbol.                            |
| Oracle | Identity      | Password Requires Uppercase | Ensures password policy requires at least one uppercase character.               |
| Oracle | Identity      | Minimum Password Length     | Ensures password policy requires a minimum password length.                      |

### Requirement 7 - Restrict Access

Restrict access to cardholder data by business need to know.

| Cloud  | Category                | Plugin                        | Description                                                                                                     |
| ------ | ----------------------- | ----------------------------- | --------------------------------------------------------------------------------------------------------------- |
| Azure  | App Service             | Authentication Enabled        | Ensures Authentication is enabled for App Services, redirecting unauthenticated users to the login page.        |
| Azure  | Blob Service            | Blob Container Private Access | Ensures that all blob containers do not have anonymous public access set                                        |
| GCP    | Compute                 | VM Instances Least Privilege  | Ensures that instances are not configured to use the default service account with full access to all cloud APIs |
| Azure  | File Service            | File Service All Access ACL   | Ensures file shares do not allow full write, delete, or read ACL permissions                                    |
| Oracle | File Storage            | NFS Public Access             | Ensures that all file systems do not have public access.                                                        |
| AWS    | IAM                     | Root Account In Use           | Ensures the root account is not being actively used                                                             |
| AWS    | IAM                     | IAM User Admins               | Ensures the number of IAM admins in the account are minimized                                                   |
| Oracle | Identity                | Users MFA Enabled             | Ensures a multi-factor authentication device is enabled for all users within the account.                       |
| Azure  | Network Security Groups | Open All Ports                | Ensures Network Security Groups do not expose all ports to the public                                           |
| Oracle | Object Store            | Bucket Public Access Type     | Ensures object store buckets do not allow global write, delete, or read permissions                             |
| Azure  | Queue Service           | Queue Service All Access ACL  | Ensures queues do not allow full write, delete, or read ACL permissions                                         |
| AWS    | S3                      | S3 Bucket All Users Policy    | Ensures S3 bucket policies do not allow global write, delete, or read permissions                               |
| AWS    | S3                      | S3 Bucket All Users ACL       | Ensures S3 buckets do not allow global write, delete, or read ACL permissions                                   |
| AWS    | SQS                     | SQS Cross Account Access      | Ensures SQS policies disallow cross-account access                                                              |
| Azure  | Table Service           | Table Service All Access ACL  | Ensures tables do not allow full write, delete, or read ACL permissions                                         |

### Requirement 8 - Identify Access

Identify and authenticate access to system components.

| Cloud  | Category     | Plugin                        | Description                                                                                                       |
| ------ | ------------ | ----------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Azure  | App Service  | Authentication Enabled        | Ensures Authentication is enabled for App Services, redirecting unauthenticated users to the login page.          |
| Azure  | Blob Service | Blob Container Private Access | Ensures that all blob containers do not have anonymous public access set                                          |
| Oracle | File Storage | NFS Public Access             | Ensures that all file systems do not have public access.                                                          |
| AWS    | IAM          | Minimum Password Length       | Ensures password policy requires a password of at least a minimum number of characters                            |
| AWS    | IAM          | Password Requires Symbols     | Ensures password policy requires the use of symbols                                                               |
| AWS    | IAM          | Maximum Password Age          | Ensures password policy requires passwords to be reset every 180 days                                             |
| AWS    | IAM          | Password Reuse Prevention     | Ensures password policy prevents previous password reuse                                                          |
| AWS    | IAM          | Root MFA Enabled              | Ensures a multi-factor authentication device is enabled for the root account                                      |
| AWS    | IAM          | Users MFA Enabled             | Ensures a multi-factor authentication device is enabled for all users within the account                          |
| AWS    | IAM          | Access Keys Rotated           | Ensures access keys are not older than 180 days in order to reduce accidental exposures                           |
| AWS    | IAM          | Access Keys Last Used         | Detects access keys that have not been used for a period of time and that should be decommissioned                |
| AWS    | IAM          | Password Expiration           | Ensures password policy enforces a password expiration                                                            |
| AWS    | IAM          | Password Requires Lowercase   | Ensures password policy requires at least one lowercase letter                                                    |
| AWS    | IAM          | Password Requires Numbers     | Ensures password policy requires the use of numbers                                                               |
| AWS    | IAM          | Password Requires Uppercase   | Ensures password policy requires at least one uppercase letter                                                    |
| AWS    | IAM          | Users Password Last Used      | Detects users with password logins that have not been used for a period of time and that should be decommissioned |

### Requirement 9 - Physical Access

Restrict physical access to cardholder data.

No plugins have been mapped to this control.

### Requirement 10 - Track Access

Track and monitor all access to network resources and cardholder data.

| Cloud  | Category   | Plugin                           | Description                                                                                   |
| ------ | ---------- | -------------------------------- | --------------------------------------------------------------------------------------------- |
| Oracle | Audit      | Log Retention Period             | Ensures that the audit log retention period is configured correctly.                          |
| AWS    | CloudFront | CloudFront Logging Enabled       | Ensures CloudFront distributions have request logging enabled.                                |
| AWS    | CloudTrail | CloudTrail Enabled               | Ensures CloudTrail is enabled for all regions within an account                               |
| AWS    | CloudTrail | CloudTrail Bucket Access Logging | Ensures CloudTrail logging bucket has access logging enabled to detect tampering of log files |
| AWS    | EC2        | VPC Flow Logs Enabled            | Ensures VPC flow logs are enabled for traffic logging                                         |
| AWS    | ELB        | ELB Logging Enabled              | Ensures load balancers have request logging enabled.                                          |
| GCP    | Logging    | Project Ownership Logging        | Ensures that logging and log alerts exist for project ownership assignments and changes       |
| GCP    | Logging    | Storage Permissions Logging      | Ensures that logging and log alerts exist for storage permission changes                      |
| GCP    | Logging    | VPC Network Logging              | Ensures that logging and log alerts exist for VPC network changes                             |
| AWS    | S3         | S3 Bucket Logging                | Ensures S3 bucket logging is enabled for S3 buckets                                           |
| AWS    | Transfer   | Transfer Logging Enabled         | Ensures AWS Transfer servers have CloudWatch logging enabled.                                 |

### Requirement 11 - Test Systems

Regularly test security systems and processes.

| Cloud | Category | Plugin         | Description                                             |
| ----- | -------- | -------------- | ------------------------------------------------------- |
| AWS   | RDS      | RDS Restorable | Ensures RDS instances can be restored to a recent point |
| GCP   | SQL      | DB Restorable  | Ensures SQL instances can be restored to a recent point |

### Requirement 12 - Policy

Maintain a policy that addresses information security for all personnel.

No plugins have been mapped to this control.
