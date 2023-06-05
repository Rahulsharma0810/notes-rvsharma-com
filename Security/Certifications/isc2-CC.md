## Chapter 1 Security Principal

The CIA Triad (Confidentiality, Integrity, and Availability) defines the core principles of security.

![](img/isc2-CC/2023-06-05-02-28-11.png)

Confidentiality: Protecting information from improper disclosure while allowing authorized access.
Integrity: Ensuring completeness, accuracy, and consistency of information and systems.
Availability: Timely and reliable access to data and information services for authorized users.
Confidentiality:

Involves regulating access to information and protecting it from unauthorized disclosure.
Personally identifiable information (PI), protected health information (PHI), and sensitive information require confidentiality.
Integrity:

Focuses on maintaining the accuracy, consistency, and completeness of data and systems.
Data integrity ensures protection against unauthorized modification, errors, or loss.
Internal consistency ensures information is correct across all related systems.
Availability:

Provides timely and reliable access to data and information services.
Critical systems must be identified and made available according to business requirements.
Availability is related to the concept of criticality, reflecting the importance of data or systems in achieving an organization's goals.
Authentication:

Validates the identity of users.
Common methods include knowledge-based (passwords), token-based (smart cards), and characteristic-based (biometrics).
Multifactor authentication (MFA) involving multiple methods is considered more secure.
Non-repudiation:

Ensures individuals cannot falsely deny their actions.
Provides evidence of who performed specific actions, such as creating, approving, or sending/receiving information.
Privacy and Data Protection:

Privacy involves an individual's right to control the distribution of their information.
Privacy laws and regulations, such as the EU's GDPR, impact organizations' handling of personal information.
Compliance with privacy regulations is essential to avoid penalties and protect sensitive data.

### Risk Management Process

1. Risk Identification: This step involves identifying and documenting potential risks that may impact an organization's operations, assets, or individuals. It requires a thorough examination of the organization's systems, processes, and external factors. Examples of risk identification include:
   - Identifying the risk of a data breach due to weak passwords and lack of user access controls.
   - Identifying the risk of a natural disaster, such as an earthquake or flood, damaging critical infrastructure.
   - Identifying the risk of a supply chain disruption impacting product delivery.
2. Risk Assessment: In this step, identified risks are analyzed and evaluated to understand their likelihood of occurrence and potential impact. Risk assessment helps prioritize risks based on their significance and guides decision-making. Examples of risk assessment include:
   - Assessing the likelihood and impact of a cyberattack on the organization's network infrastructure.
   - Assessing the risk associated with employee negligence or unintentional data leaks.
   - Assessing the potential impact of regulatory non-compliance on the organization's reputation and financial standing.
3. Risk Treatment: Once risks are assessed, organizations need to determine the appropriate response strategies to address them. There are several risk treatment options:
   - Risk Acceptance: If the likelihood or impact of a risk is low and the cost of mitigation outweighs the potential loss, the organization may choose to accept the risk. For example, accepting the risk of a minor office equipment failure that has a low impact on operations.
   - Risk Avoidance: If a risk poses a significant threat or the organization wants to eliminate the risk entirely, it may choose to avoid it. For instance, avoiding the risk of data breaches by not storing sensitive customer information.
   - Risk Mitigation: This involves implementing measures to reduce the likelihood or impact of a risk. Examples include implementing firewalls and intrusion detection systems to mitigate the risk of unauthorized access to a network or conducting regular backups to mitigate the risk of data loss.
   - Risk Transfer: Organizations can transfer risk to another party, typically through insurance policies or outsourcing certain functions. For instance, transferring the risk of property damage due to natural disasters to an insurance company.

![](img/isc2-CC/2023-06-05-02-42-33.png)

4. Risk Monitoring and Review: Risk management is an ongoing process that requires continuous monitoring and review of the effectiveness of risk mitigation measures. This step involves regular assessments, updates to risk profiles, and adjusting risk treatment strategies as needed. Examples of risk monitoring and review include:
   - Regularly reviewing security logs and conducting vulnerability assessments to identify new risks and vulnerabilities.
   - Monitoring industry trends and emerging threats to proactively address potential risks.
   - Conducting periodic audits to assess compliance with security policies and regulations.

### Security Control

Security controls are mechanisms implemented to protect the confidentiality, integrity, and availability of an information system. They can be classified into three categories: physical controls, technical controls, and administrative controls. Here are brief explanations and examples of each:

1. Physical Controls:
   - Physical controls address security needs using physical hardware devices and actions taken by users.
   - Examples include badge readers, locks, security cameras, and access control systems.
   - For instance, visitors entering a workplace must pass through a designated entrance where they are identified and assessed before being allowed entry. Employees may use company-issued badges to assert their identity and gain access.
2. Technical Controls:
   - Technical controls are security measures implemented within computer systems and networks.
   - They provide automated protection, detect security violations, and support security requirements for applications and data.
   - Examples include firewalls, encryption, intrusion detection systems, and antivirus software.
   - For example, configuring firewalls to filter network traffic and allow only authorized connections.
3. Administrative Controls:
   - Administrative controls are directives, guidelines, and policies that govern human behavior within an organization.
   - They cover the entire scope of activities and interactions with external parties.
   - Examples include security awareness training, policies and procedures, and access management processes.
   - An example is the Human Resources department implementing onboarding procedures that ensure employees receive security training, understand acceptable resource usage, and have appropriate access based on their roles.

Administrative controls, when effectively implemented, can be powerful tools for achieving information and system security. They integrate security into business processes and ensure compliance with policies and guidelines.

It's important to note that security controls often work together in a layered approach to provide comprehensive protection against various threats and risks. Organizations should assess their specific security requirements and implement a combination of physical, technical, and administrative controls to mitigate risks and protect their information systems.

### Governance Elements and Processes

- Governance elements: Decisions, rules, practices, policies, and procedures are essential for organizations to achieve their objectives and mission.
- Relationship among governance elements:
  - Procedures: Detailed steps that support policies and guide the completion of tasks.
  - Policies: Established by organizational governance to ensure compliance with industry standards, regulations, and laws.
  - Standards: Frameworks used by governance teams to introduce policies and procedures aligned with regulations and best practices.
  - Regulations: Laws imposed by governments that carry penalties for noncompliance.
- Regulations and Laws:
  - Examples:
    - HIPAA (Health Insurance Portability and Accountability Act): Governs the use of protected health information (PHI) in the United States, with fines and imprisonment as possible penalties for violations.
    - GDPR (General Data Protection Regulation): Controls the use of personally identifiable information (PII) and applies to organizations conducting business with the European Union, imposing financial penalties for mishandling EU citizens' data.
- Standards:
  - Examples:
    - ISO (International Organization for Standardization): Develops international standards, including information systems security, information security, and encryption standards.
    - NIST (National Institute of Standards and Technology): Publishes technical standards, including information technology and information security standards, considered best practices worldwide.
- Policies:
  - Policies provide guidance and context, establish strategic direction and priorities, moderate decision-making, and ensure compliance.
  - Policies are written at various levels within an organization, including high-level governance policies, functional area policies (e.g., HR, finance, security), and specific policies for compliance.
- Procedures:
  - Procedures define explicit and repeatable activities needed to accomplish specific tasks.
  - They provide supporting data, decision criteria, and knowledge required for task execution.
  - Procedures establish measurement criteria and methods to assess task completion.
  - Proper documentation and training on procedures are essential for deriving organizational benefits.

### Summary

In this chapter, you learned about various security principles and concepts related to information assurance. The CIA Triad, consisting of confidentiality, integrity, and availability, was highlighted as the primary component of information assurance.

- Confidentiality (C): It emphasizes the need to protect data from unauthorized access.
- Integrity (I): It focuses on ensuring that data remains unaltered and trustworthy.
- Availability (A): It emphasizes making data accessible to authorized users when and where needed.

Privacy, authentication, non-repudiation, and authorization were also discussed as important aspects of information security.

You explored the importance of risk management in assessing and prioritizing risks to an organization's assets. The options for addressing risks were presented as accept, avoid, mitigate, or transfer.

The chapter introduced three types of security controls:

1. Physical controls: These involve hardware devices, architectural features, and security actions to address process-based security needs.
2. Technical controls: Also known as logical controls, these are implemented by computer systems and networks.
3. Administrative controls: These include directives, guidelines, and advisories that shape the behavior of people within the organization.

Organizational security roles, governance, policies, procedures, and standards were discussed, highlighting the relationship between them. Regulations, typically issued as laws by governments, carry financial penalties for noncompliance. Standards serve as frameworks for introducing policies and procedures that support regulations. Policies, set by organizational governance, provide guidance to ensure compliance with industry standards and regulations. Procedures are the detailed steps that support policies and guide the completion of tasks.

The chapter also covered the ISC2 Code of Ethics, which outlines ethical standards for cybersecurity professionals.

In summary, the chapter emphasized the importance of adhering to legal and ethical standards in the field of cybersecurity.

### Terms and Definations

| Term                                | Definition                                                                                                                                                         | Example                                                                                                                                                   |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Adequate Security                   | The level of protection and safeguards implemented to ensure the confidentiality, integrity, and availability of information or assets.                            | Implementing firewalls, access controls, and encryption to protect sensitive data from unauthorized access.                                               |
| Administrative Controls             | Policies, procedures, guidelines, and directives implemented by an organization to manage and govern its security practices.                                       | Implementing an information security policy, conducting security awareness training, and establishing incident response procedures.                       |
| Artificial Intelligence             | The development and deployment of computer systems and algorithms that can perform tasks typically requiring human intelligence.                                   | Using machine learning algorithms to analyze large datasets and detect patterns in network traffic to identify potential security threats.                |
| Asset                               | A valuable resource, item, or component that has value to an individual, organization, or system.                                                                  | Computer systems, software applications, customer databases, intellectual property, and financial resources.                                              |
| Authentication                      | The process of verifying the identity of an individual, system, or entity to ensure that they are who they claim to be.                                            | Providing a username and password to log into a secure system or using a fingerprint scanner to unlock a smartphone.                                      |
| Authorization                       | The process of granting or denying access to specific resources, systems, or information based on the authenticated identity and assigned privileges.              | Allowing an employee with administrative privileges to access and modify sensitive files on a server, while restricting access to regular users.          |
| Availability                        | The property of a system or resource being accessible and usable when needed by authorized users.                                                                  | Ensuring that a critical business application is available 24/7 without any interruptions or downtime.                                                    |
| Baseline                            | A standard or reference point against which the security of a system or component is measured or compared.                                                         | Establishing a baseline configuration for a computer system by documenting the approved software versions, security settings, and network configurations. |
| Biometric                           | Biological characteristics or behavioral traits unique to an individual that can be used for authentication purposes.                                              | Fingerprint scans, iris recognition, and facial recognition technologies used for unlocking smartphones or accessing secure facilities.                   |
| Bot                                 | A software application or script that performs automated tasks on the internet, often without the user's knowledge or consent.                                     | Malicious bots used in distributed denial-of-service (DDoS) attacks to overwhelm a target website with traffic and make it inaccessible.                  |
| Classified or Sensitive Information | Information that is labeled or designated as confidential, restricted, or requiring special protection due to its sensitive nature.                                | Government documents marked as "Top Secret" or a company's financial records containing sensitive customer information.                                   |
| Confidentiality                     | The property of data or information being protected from unauthorized disclosure or access.                                                                        | Encrypting sensitive email communications to ensure that only the intended recipients can read the content.                                               |
| Criticality                         | The importance or significance of a system, asset, or process to the organization's operations, goals, or objectives.                                              | A server hosting a critical financial application that is essential for conducting daily transactions and generating revenue.                             |
| Data Integrity                      | The accuracy, completeness, and reliability of data throughout its lifecycle, ensuring that it is not modified or altered in an unauthorized or unintended manner. | Implementing checksums or digital signatures to verify                                                                                                    |

## Chapter 2

### Incident Response

- Incident response is a crucial role of security professionals as they act as first responders when things go wrong in terms of cyberattacks or security incidents.
- Key terms related to incident response include breach, event, exploit, incident, intrusion, threat, vulnerability, and zero day.
  - Breach: A breach refers to the loss of control or compromise of sensitive information. For example, if a hacker gains unauthorized access to a company's database containing customer information and steals personal data such as names, addresses, and credit card details, it would be considered a breach.
  - Event: An event refers to any observable occurrence in a network or system. It could be an anomaly, suspicious activity, or an indicator of a potential security incident. For instance, detecting a large number of failed login attempts or unusual network traffic patterns can be considered events that require investigation.
  - Exploit: An exploit is a specific attack that takes advantage of vulnerabilities in a system. For example, a hacker may use a known software vulnerability to deliver malware or gain unauthorized access to a system.
  - Incident: An incident is an event that actually or potentially jeopardizes the confidentiality, integrity, or availability of an information system or its data. An incident can range from a minor security issue to a significant cyberattack. For instance, if a company's website is defaced by hackers or if a malware infection disrupts critical business operations, it would be considered an incident.
  - Intrusion: Intrusion refers to a deliberate security incident in which an unauthorized individual gains or attempts to gain access to a system or resource. An example of an intrusion is when an attacker bypasses network defenses and gains unauthorized access to sensitive data by exploiting a vulnerability in a web application.
  - Threat: A threat refers to any circumstance or event that has the potential to harm organizational operations, assets, or individuals through unauthorized access, disclosure, modification, or denial of service. For instance, a threat could be a phishing email campaign that attempts to trick employees into revealing their login credentials.
  - Vulnerability: A vulnerability is a weakness in an information system, its security procedures, controls, or implementation that could be exploited by a threat actor. For example, an unpatched software vulnerability or weak password policies can create vulnerabilities that attackers can exploit to gain unauthorized access.
  - Zero Day: A zero-day vulnerability is a previously unknown vulnerability that is exploited by attackers before a patch or fix is available. Since the vulnerability is unknown, it can be exploited without detection or prevention. An example of a zero-day exploit is when a hacker discovers and exploits a vulnerability in a widely used software program before the software vendor becomes aware of it and releases a patch.
- The primary goal of incident response is to protect life, health, and safety, prioritizing the safety of people in all decision-making processes.
- Incident response planning is a subset of business continuity management, which aims to reduce the impact of an incident and resume operations as soon as possible.
- Components of an incident response plan include preparation, detection and analysis, containment, post-incident activity, and retrospective evaluation.
- **Preparation** involves developing a policy, identifying critical data and systems, training staff, forming an incident response team, and practicing incident identification and coordination of communication.
- **Detection and analysis** require monitoring attack vectors, analyzing incidents using known data and threat intelligence, prioritizing incident response, and standardizing incident documentation.
- **Containment** involves gathering evidence, choosing an appropriate containment strategy, identifying the source of the event, and isolating the source.
- **Post-incident** activities include identifying evidence for retention, documenting lessons learned, and complying with regulatory requirements if necessary.

![](img/isc2-CC/2023-06-05-03-45-12.png)

- Consulting with management involves identifying critical information, avoiding single points of failure, training staff in incident response, and coordinating communication with different stakeholders.
- An incident response team is a cross-functional group of individuals who investigate and respond to security incidents, including representatives from senior management, information security, legal, public affairs/communications, and engineering.
- Incident response teams are responsible for investigating incidents, assessing damage, collecting evidence, reporting incidents, initiating recovery procedures, participating in remediation and lessons learned stages, and conducting root cause analysis.
- Dedicated incident response teams, such as computer incident response teams (CIRTs) or computer security incident response teams (CSIRTs), are common in organizations and have primary responsibilities to determine the damage, assess data compromise, implement recovery procedures, and improve security measures to prevent recurrence.

### Bussiness Continuity

The importance of business continuity cannot be overstated. Here are some key points and examples that highlight its significance:

1. Sustaining Operations: Business continuity plans are essential for organizations to continue their critical operations and minimize the impact of disruptions. For instance, in the event of a natural disaster such as a hurricane or earthquake, a business continuity plan ensures that key business functions can be carried out at alternate locations or through remote work arrangements. This enables the organization to maintain its services, meet customer needs, and minimize financial losses.

2. Communication and Coordination: Effective communication is a crucial aspect of business continuity. Establishing multiple contact methodologies and backup numbers ensures that key personnel can be reached during a disruption, even if regular communication channels are compromised. A phone tree, which outlines a hierarchical calling sequence, helps ensure that the right individuals are contacted promptly. This enables efficient coordination and decision-making during an incident.

3. Procedures and Checklists: Business continuity plans should include well-defined procedures and comprehensive checklists to guide personnel during a disruption. Similar to pilots going through a pre-flight checklist, organizations must have established procedures and checklists to ensure that critical elements of business continuity are not overlooked. These procedures and checklists help maintain consistency and ensure that all necessary actions are taken to recover operations.

4. Adaptability and Management Involvement: Business continuity plans should be flexible and adaptable to different scenarios. Management must be involved in the planning process to address changing priorities and make crucial decisions during a disruption. This ensures that the plan can be adjusted as per the specific situation and that the organization can respond effectively to unexpected challenges.

5. External Communication and Support: Business continuity plans should include contact numbers for critical stakeholders outside the organization, such as suppliers, customers, law enforcement, and emergency response agencies. These contacts are essential for coordinating efforts, obtaining assistance, and maintaining essential activities during a major disruption. For example, in the case of a severe cyberattack impacting communication systems, having access to alternative networks or military-grade networks can help hospitals or other critical infrastructures maintain essential operations.

6. Focus on Critical Functions: Business continuity planning focuses on ensuring the continuity of critical products and services provided by the organization. It may involve operating at a reduced capacity but ensures that key functions can continue until normal business operations can be restored. Identifying and prioritizing critical areas through business impact analysis helps allocate resources effectively and ensures that the most essential aspects of the business are protected.

7. Organizational Commitment: Developing and implementing a business continuity plan requires a significant commitment of personnel and financial resources. Executive management or an executive sponsor must provide support and champion business continuity planning efforts. Without proper support and commitment from the organization's leadership, business continuity planning is unlikely to succeed.

Business continuity planning encompasses various components, such as the business continuity plan team, immediate response procedures, notification systems, management guidance, contact numbers, and more. These components work together to create a comprehensive plan that addresses all systems, processes, and operations necessary for maintaining critical business functions.

It is crucial to store the business continuity plan in a location accessible to key personnel. While digital storage is common, having a hard copy, often referred to as the Red Book, can serve as a backup in case electronic systems are unavailable. Regular updates and consistency between electronic and hard copies are essential to ensure accuracy and relevance.

In a real-life scenario, if a company's billing department experiences a complete loss due to a fire, a business continuity plan can help mitigate the impact. The plan may involve relocating the billing department to an alternative site within a week, with customer service staff temporarily handling billing inquiries. This ensures that billing processes continue, customer needs are addressed, and business operations remain uninterrupted.

Overall, business continuity planning is crucial for organizations to be resilient in the face of disruptions, protect their reputation.

### Disaster Recovery

In order to identify the components of disaster recovery, let's break down the information provided in the text:

1. Goal of Disaster Recovery: The goal of disaster recovery is to restore the information technology (IT) and communication services and systems needed by an organization during a disruption and during the restoration of normal services. While business continuity planning focuses on maintaining critical business functions, disaster recovery planning specifically deals with restoring IT and communication systems.

2. Examples of Disaster Recovery: The text provides two examples to illustrate the importance of disaster recovery planning:

   a. **Hospital Compromise**: In a hospital in Los Angeles, a compromise went undetected for 260 days. The hospital couldn't rely on the last backup because it was infected with time-based malware that would corrupt the system upon restoration. To recover, the hospital had to go back nearly a year to restore the entire system and then restore the remaining data piece-by-piece to prevent reinfection. This example emphasizes the need for multiple levels of backups and different retention periods to address organization-specific needs.

   b. **Complex System Dependencies**: The text highlights the importance of understanding the flow of data and dependencies between systems. For example, in another hospital scenario, the radiology department used a different system than the laboratory. Separate routines copied patient data from the registration system to the laboratory and radiology systems, which technically use separate databases. It's crucial to document and implement a disaster recovery plan that considers the intricate dependencies between systems.

3. Components of a Disaster Recovery Plan: The text suggests several types of documents that organizations should consider when developing a disaster recovery plan:

   a. **Executive Summary**: Provides a high-level overview of the plan.

   b. **Department-Specific Plans**: Tailored plans for different departments within the organization.

   c. **Technical Guides**: Detailed guides for IT personnel responsible for implementing and maintaining critical backup systems.

   d. Full Copies of the Plan: Distributed to critical disaster recovery team members.

   e. Checklists: Provided to individuals involved in the recovery efforts, such as the disaster recovery team members, IT personnel, managers, and public relations personnel. Checklists help guide their actions, facilitate effective communication, and ensure necessary steps are taken during the recovery process.

4. Work Lost during the Incident: The text includes a timeline illustration demonstrating the potential work lost during an incident. It shows different events, backups, and transactions along the timeline, indicating the level of integrity, authenticity, and security of the data. The timeline distinguishes work that was fully processed prior to the incident, work that may be compromised or in doubt, and work lost since the incident occurred.

Overall, disaster recovery planning involves identifying critical systems, maintaining backups, understanding system dependencies, and developing comprehensive plans and documentation. By having a well-designed disaster recovery plan in place, organizations can minimize downtime, recover critical systems effectively, and mitigate the impact of disruptions on their operations.

### Summary

Certainly! Here are the key points from this chapter:

1. Incident response plans are designed to keep the business operating during abnormal conditions. They consist of preparation, detection and analysis, containment, eradication and recovery, and post-incident activities.
2. Incident response teams comprise cross-functional members responsible for managing and resolving security incidents.
3. Business continuity plans focus on sustaining business operations during a crisis. They include the steps to enact the plan, notification systems, call trees, and contact information for key stakeholders.
4. Business continuity plans provide immediate response procedures, checklists, and guidance for management.
5. Disaster recovery plans are activated when incident response and business continuity plans fail. They aim to restore operations to normal as quickly as possible.
6. Components of a disaster recovery plan may include an executive summary, department-specific plans, technical guides for IT personnel, full copies of the plan for critical team members, and checklists for specific individuals.
7. Incident response, business continuity, and disaster recovery plans work together to ensure the availability of critical systems and minimize the impact of disruptions.
8. These plans require cross-functional collaboration, training, and regular testing to ensure their effectiveness.
9. The incident response team assesses the extent of damage, implements recovery procedures, and improves security measures to prevent future incidents.
10. Business continuity plans include contact information for third-party partners, vendors, customers, and external emergency providers.
11. The ultimate goal of these plans is to maintain business operations and minimize downtime during and after incidents, crises, or disasters.

By implementing these plans, organizations can effectively respond to incidents, maintain operations, and recover from disruptions, ensuring the continuity and resilience of their business.

### Terms and Definations

| Term                       | Definition                                                                       | Example                                                        |
| -------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| Adverse Events             | Unfavorable incidents or occurrences                                             | Power outage, natural disaster, cyber-attack                   |
| Breach                     | Unauthorized access or disclosure of sensitive information                       | Data breach resulting in customer data being compromised       |
| Business Continuity        | Ability to maintain essential functions during a crisis                          | Implementing remote work arrangements during a pandemic        |
| Business Continuity Plan   | Documented procedures to ensure business continuity                              | Detailed instructions for employees during a disruptive event  |
| Business Impact Analysis   | Assessment of the potential effects of a disruption                              | Identifying critical systems and their impact on operations    |
| Disaster Recovery          | Restoration of IT and communication services                                     | Recovering servers and databases after a hardware failure      |
| Disaster Recovery Plan     | Strategies and procedures to recover from a disaster                             | Backup and recovery processes for critical systems             |
| Event                      | Occurrence that may disrupt operations                                           | System outage, equipment failure                               |
| Exploit                    | Taking advantage of vulnerabilities to gain unauthorized access                  | Utilizing a software vulnerability to hack into a system       |
| Incident                   | Security event that violates policies or threatens security                      | Unauthorized access attempt or malware infection               |
| Incident Handling          | Process of responding to and managing security incidents                         | Identifying, containing, and resolving a data breach           |
| Incident Response          | Immediate actions taken in response to a security incident                       | Blocking a suspicious IP address after a hacking attempt       |
| Incident Response Plan     | Documented procedures for responding to security incidents                       | Contacting the incident response team and escalating the issue |
| Intrusion                  | Unauthorized access or presence in a system or network                           | Hacking into a company's server without permission             |
| Security Operations Center | Centralized team responsible for monitoring and responding to security incidents | Monitoring network traffic for potential threats               |
| Threat                     | Potential event or action that can exploit vulnerabilities                       | Malware, phishing attacks, social engineering                  |
| Vulnerability              | Weakness or flaw in a system's security defenses                                 | Unpatched software vulnerability that allows remote access     |
| Zero Day                   | Previously unknown software vulnerability                                        | Exploiting a newly discovered flaw before it is patched        |
