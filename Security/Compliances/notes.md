## PCI-DSS

### Checklist
1. Install and maintain a firewall configuration to protect cardholder data.
2. Do not use vendor-supplied defaults for system passwords and other security parameters.
3. Protect stored cardholder data.
4. Encrypt transmission of cardholder data across open, public networks.
5. Use and regularly update anti-virus software.
6. Develop and maintain secure systems and applications.
7. Restrict access to cardholder data by business need-to-know. Assign a unique ID to each person with computer
8. access. Restrict physical access to cardholder data.
9. Track and monitor all access to network resources and cardholder data.
10. Regularly test security systems and processes.
11. Maintain a policy that addresses information security.


| Version |  Date    |
| ------- | ---- |
| 1.2 | 04/06/2021 |

## 1 Identity and Access Management

1.1 Ensure that corporate login credentials are used (Automated)

1.2 Ensure that multi-factor authentication is enabled for all non-service accounts (Manual)

1.3 Ensure that Security Key Enforcement is enabled for all admin accounts (Manual)

1.4 Ensure that there are only GCP-managed service account keys for each service account (Automated)

1.5 Ensure that Service Account has no Admin privileges (Automated)

1.6 Ensure that IAM users are not assigned the Service Account User or Service Account Token Creator roles at project level (Automated)

1.7 Ensure user-managed/external keys for service accounts are rotated every 90 days or less (Automated)

1.8 Ensure that Separation of duties is enforced while assigning service account related roles to users (Manual)

1.9 Ensure that Cloud KMS cryptokeys are not anonymously or publicly accessible (Automated)

1.10 Ensure KMS encryption keys are rotated within a period of 90 days (Automated)

1.11 Ensure that Separation of duties is enforced while assigning KMS related roles to users (Automated)

1.12 Ensure API keys are not created for a project (Manual)

1.13 Ensure API keys are restricted to use by only specified Hosts and Apps (Manual)

1.14 Ensure API keys are restricted to only APIs that application needs access (Manual)

1.15 Ensure API keys are rotated every 90 days (Manual)

## 2 Logging and Monitoring

2.1 Ensure that Cloud Audit Logging is configured properly across all services and all users from a project (Automated)

2.2 Ensure that sinks are configured for all log entries (Automated)

2.3 Ensure that retention policies on log buckets are configured using Bucket Lock (Automated)

2.4 Ensure log metric filter and alerts exist for project ownership assignments/changes (Automated)

2.5 Ensure that the log metric filter and alerts exist for Audit Configuration changes (Automated)

2.6 Ensure that the log metric filter and alerts exist for Custom Role changes (Automated)

2.7 Ensure that the log metric filter and alerts exist for VPC Network Firewall rule changes (Automated)

2.8 Ensure that the log metric filter and alerts exist for VPC network route changes (Automated)

2.9 Ensure that the log metric filter and alerts exist for VPC network changes (Automated)

2.10 Ensure that the log metric filter and alerts exist for Cloud Storage IAM permission changes (Automated)

2.11 Ensure that the log metric filter and alerts exist for SQL instance configuration changes (Automated)

2.12 Ensure that Cloud DNS logging is enabled for all VPC networks (Automated)

## 3 Networking

3.1 Ensure that the default network does not exist in a project (Automated).

3.2 Ensure legacy networks do not exist for a project (Automated)

3.3 Ensure that DNSSEC is enabled for Cloud DNS (Automated)

3.4 Ensure that RSASHA1 is not used for the key-signing key in Cloud DNS DNSSEC (Manual).

3.5 Ensure that RSASHA1 is not used for the zone-signing key in Cloud DNS DNSSEC (Manual).

3.6 Ensure that SSH access is restricted from the internet (Automated)

3.7 Ensure that RDP access is restricted from the Internet (Automated)

3.8 Ensure that VPC Flow Logs is enabled for every subnet in a VPC Network (Automated)

3.9 Ensure no HTTPS or SSL proxy load balancers permit SSL policies with weak cipher suites (Manual)

3.10 Ensure Firewall Rules for instances behind Identity Aware Proxy (IAP) only allow the traffic from Google Cloud Loadbalancer (GCLB) Health Check and Proxy Addresses (Manual)

## 4 Virtual Machines

4.1 Ensure that instances are not configured to use the default service account (Automated)

4.2 Ensure that instances are not configured to use the default service account with full access to all Cloud APIs (Automated)

4.3 Ensure "Block Project-wide SSH keys" is enabled for VM instances (Automated)5

4.4 Ensure oslogin is enabled for a Project (Automated)

4.5 Ensure 'Enable connecting to serial ports' is not enabled for VM Instance (Automated)

4.6 Ensure that IP forwarding is not enabled on Instances (Automated)

4.7 Ensure VM disks for critical VMs are encrypted with Customer-Supplied Encryption Keys (CSEK) (Automated)

4.8 Ensure Compute instances are launched with Shielded VM enabled (Automated)

4.9 Ensure that Compute instances do not have public IP addresses (Automated)

4.10 Ensure that App Engine applications enforce HTTPS connections (Manual)

4.11 Ensure that Compute instances have Confidential Computing enabled (Automated)

## 5 Storage

5.1 Ensure that Cloud Storage bucket is not anonymously or publicly accessible (Automated)

5.2 Ensure that Cloud Storage buckets have uniform bucket-level access enabled (Automated)

## 6 Cloud SQL Database Services

### 6.1 MySQL Database

6.1.1 Ensure that a MySQL database instance does not allow anyone to connect with administrative privileges (Automated)

6.1.2 Ensure 'skip_show_database' database flag for Cloud SQL Mysql instance is set to 'on' (Automated)

6.1.3 Ensure that the 'local_infile' database flag for a Cloud SQL Mysql instance is set to 'off' (Automated)

### 6.2 PostgreSQL Database 179

6.2.1 Ensure that the 'log_checkpoints' database flag for Cloud SQL PostgreSQL instance is set to 'on' (Automated)

6.2.2 Ensure 'log_error_verbosity' database flag for Cloud SQL PostgreSQL instance is set to 'DEFAULT' or stricter (Manual)

6.2.3 Ensure that the 'log_connections' database flag for Cloud SQL PostgreSQL instance is set to 'on' (Automated)

6.2.4 Ensure that the 'log_disconnections' database flag for Cloud SQL PostgreSQL instance is set to 'on' (Automated)

6.2.5 Ensure 'log_duration' database flag for Cloud SQL PostgreSQL instance is set to 'on' (Manual)

6.2.6 Ensure that the 'log_lock_waits' database flag for Cloud SQL PostgreSQL instance is set to 'on' (Automated)

6.2.7 Ensure 'log_statement' database flag for Cloud SQL PostgreSQL instance is set appropriately (Manual)

6.2.8 Ensure 'log_hostname' database flag for Cloud SQL PostgreSQL instance is set appropriately (Automated)

6.2.9 Ensure 'log_parser_stats' database flag for Cloud SQL PostgreSQL instance is set to 'off' (Automated)

6.2.10 Ensure 'log_planner_stats' database flag for Cloud SQL PostgreSQL instance is set to 'off' (Automated)

6.2.11 Ensure 'log_executor_stats' database flag for Cloud SQL PostgreSQL instance is set to 'off' (Automated)

6.2.12 Ensure 'log_statement_stats' database flag for Cloud SQL PostgreSQL instance is set to 'off' (Automated)

6.2.13 Ensure that the 'log_min_messages' database flag for Cloud SQL PostgreSQL instance is set appropriately (Manual).

6.2.14 Ensure 'log_min_error_statement' database flag for Cloud SQL PostgreSQL instance is set to 'Error' or stricter (Automated)

6.2.15 Ensure that the 'log_temp_files' database flag for Cloud SQL PostgreSQL instance is set to '0' (on) (Automated)

6.2.16 Ensure that the 'log_min_duration_statement' database flag for Cloud SQL PostgreSQL instance is set to '-1' (disabled) (Automated)

### 6.3 SQL Server 228

6.3.1 Ensure 'external scripts enabled' database flag for Cloud SQL SQL Server instance is set to 'off' (Automated)

6.3.2 Ensure that the 'cross db ownership chaining' database flag for Cloud SQL SQL Server instance is set to 'off' (Automated)

6.3.3 Ensure 'user connections' database flag for Cloud SQL SQL Server instance is set as appropriate (Automated)

6.3.4 Ensure 'user options' database flag for Cloud SQL SQL Server instance is not configured (Automated)

6.3.5 Ensure 'remote access' database flag for Cloud SQL SQL Server instance is set to 'off' (Automated)

6.3.6 Ensure '3625 (trace flag)' database flag for Cloud SQL SQL Server instance is set to 'off' (Automated)

6.3.7 Ensure that the 'contained database authentication' database flag for Cloud SQL on the SQL Server instance is set to 'off' (Automated)

6.4 Ensure that the Cloud SQL database instance requires all incoming connections to use SSL (Automated)

6.5 Ensure that Cloud SQL database instances are not open to the world (Automated)

6.6 Ensure that Cloud SQL database instances do not have public IPs (Automated)

6.7 Ensure that Cloud SQL database instances are configured with automated backups (Automated)

## 7 BigQuery

7.1 Ensure that BigQuery datasets are not anonymously or publicly accessible (Automated)

7.2 Ensure that all BigQuery Tables are encrypted with Customer-managed encryption key (CMEK) (Automated)

7.3 Ensure that a Default Customer-managed encryption key (CMEK) is specified for all BigQuery Data Sets (Automated)