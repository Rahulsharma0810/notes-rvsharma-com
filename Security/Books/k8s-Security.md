# Chapter 1. Container Security Threats

In the last few years, the use of containers has exploded. The concepts around containers existed for several years before Docker, but most observers agree that it was Docker’s easy-to-use command line tools that started to popularize containers amongst the developer community from its launch in 2013.
Containers bring many advantages: as described in Docker’s original tagline, they allow you to “build once, run anywhere”. They do this by bundling together an application and all its dependencies, and isolating the application from the rest of the machine it’s running on. The containerized application has everything it needs, and it is easy to package up as a container image that will run the same on my laptop and yours, or in a server in a data center.
A knock-on effect of this isolation is that you can run multiple different containers side by side without them interfering with each other. Before containers, you could easily end up with a dependency nightmare where two applications required different versions of the same packages. The easiest solution to this problem was simply to run the applications on separate machines. With containers, the dependencies are isolated from each other so it becomes straightforward to run multiple apps on the same server. People quickly realized that they could take advantage of containerization to run multiple applications on the same host (whether it’s a virtual machine or a bare-metal server) without having to worry about dependencies.
The next logical step was to spread containerized applications across a cluster of servers. Orchestrators such as Kubernetes automate this process so that you no longer have to manually install an app on a particular machine; you tell the orchestrator what containers you want to run, and it finds a suitable location for each one.
From a security perspective, many things are the same in a containerized environment as they are in a traditional deployment. There are attackers out in the world who want to steal data, or modify the way a system behaves, or use other people’s compute resources to mine their own cryto-currencies. This doesn’t change when you move to containers. However, containers do change a lot about the way that applications run, and there are a different set of risks as a result.

Risks, threats and mitigations

A risk is a potential problem, and the effects of that problem if it were to occur.
A threat is a path to that risk occuring.
A mitigation is a counter-measure against a threat - something you can do to prevent it or at least reduce the likelihood of its success.
For example, there is a risk that someone could steal your car keys from your house, and thus drive off in your car. The threats would be the different ways they might steal the keys: breaking a window to reach in and pick them up; putting a fishing rod through your letter box; knocking on your door and distracting you while an accomplice slips in quickly to grab the keys. A mitigation for all these threats might be to keep your car keys out of sight.
Risks vary greatly from one organization to another. For a bank holding money on behalf of customers, the biggest risk is almost certainly that money being stolen. An e-commerce organization will worry about the risks of fraudulent transactions. An individual running a personal blog site might fear that someone might break in to impersonate them and post inappropriate comments. Because privacy regulations differ, the risk of leaking customers’ personal data varies with geography - in many countries the risk is “only” reputational, while in Europe GDPR allows for fines of up to 4% of a company’s total revenue.
Because the risks vary greatly, the relative importance of different threats will also vary, as will the appropriate set of mitigations. A risk management framework is a process for thinking about risks in a systematic way, enumerating the possible threats, prioritizing their importance and defining an approach to mitigation.
Threat modelling is a process of identifying and enumerating the potential threats to a system. By systematically looking at the system’s components, and the possible modes of attack, a threat model can help you identify where your system is most vulnerable to attack.
There is no single comprehensive threat model as it depends on your risks, your particular environment, your organization, and the applications you’re running, but it is possible to list some potential threats that are common to most, if not all, container deployments.

Container threat model

One way to start thinking about the threat model is to consider the actors involved. These might include:
External attackers attempting to access a deployment from outside
Internal attackers who have managed to access some part of the deployment
Malicious internal actors such as developers and administrators who have some level of privilege to access the deployment

Inadvertant internal actors who may accidentally cause problems

Application processes which - while not sentient beings intending to compromise your system - might have programmatic access to the system

Each actor has a certain set of permissions that you need to consider.

What access do they have through credentials? For example, do they have access to user accounts on the host machines your deployment is running on?

What permissions do they have on the system? In Kubernetes, this could refer to the role-based access control settings for each user, as well as anonymous users.

What network access do they have? For example, which parts of the system are included within a Virtual Private Cloud (VPC)?

There are several possible routes to attacking a containerized deployment, and one way to map them is to think of the potential attack vectors at each stage of a container’s life cycle. These are summarized in Figure 1-1.

Figure 1-1. Container attack vectors

Vulnerable application code The life cycle starts with the application code that a developer writes. This code, and the third-party dependencies that it relies on, can include flaws known as vulnerabilities, and there are thousands of published vulnerabilities that an attacker can exploit if they are present in an application. The best way to avoid running containers with known vulnerabilities is to scan images, as you will see in Chapter 7. This isn’t a one-off activity, because new vulnerabilities are discovered in existing code all the time. The scanning process also needs to identify when containers are running with out-of-date packages that need to be updated for security patches. Some scanners can also identify malware that has been built into an image.

Badly configured container images Once the code has been written, it gets built into a container image. When configuring how a container image is going to be built, there are plenty of opportunities to introduce weaknesses that can later be used to attack the running container. These include configuring the container to run as the root user, giving it more privilege on the host than it really needs. You’ll read more about this in Chapter 6.

Build machine attacks If an attacker can modify or influence the way a container image is built, she could insert malicious code that will subsequently get run in the production environment. In addition, finding a foothold within the build environment could be a stepping stone towards breaching the production environment. This is also discussed in Chapter 6.

Supply chain attacks Once the container image is built, it gets stored in a registry, and it gets retrieved or “pulled” from the registry at the point where it’s going to be run. How do you know that the image you pull is exactly the same as what you pushed earlier? Could it have been tampered with? An actor who can replace an image or modify an image between build and deployment has the ability to run arbitrary code on your deployment. This is another topic I’ll cover in Chapter 6.

Badly configured containers As we’ll discuss in Chapter 9, it’s possible to run containers with settings that give it unnecessary, and perhaps unplanned, privileges. If you download YAML configuration files from the internet, please don’t run them without carefully checking that they do not include insecure settings!

Vulnerable hosts Containers run on host machines, and you need to ensure that those hosts are not running vulnerable code (for example, old versions of orchestration components with known vulnerabilities). It’s a good idea to minimize the amount of software installed on each host, to reduce the attack surface, and hosts also need to be configured correctly according to security best practices. This is discussed in Chapter 4

Exposed secrets Application code often needs credentials, tokens, or passwords in order to communicate with other components in a system. In a containerized deployment, you need to be able to pass these secret values into the containerized code. As you’ll see in Chapter 12 there are different approaches to this, with varying levels of security.

Insecure networking Containers generally need to communicate with other containers, or with the outside world. Chapter 10 discusses how networking works in containers, and Chapter 11 discusses setting up secure connections between components.

Container escape vulnerabilities The widely-used container runtimes including containerd and CRI-O are by now pretty battle-hardened, but it’s still within the realms of possibility that there are bugs yet to be found that would let malicious code running inside a container escape out onto the host. One such issue, sometimes referred to as Runcescape, came to light as recently as 2019. You’ll read about the isolation that is supposed to keep application code constrained within a container in Chapter 4. For some applications, the consequences of an escape could be sufficiently damaging that it’s worth considering stronger isolation mechanisms, such as those covered in Chapter 8.

There are also some attack vectors that are outside the scope of this book.

Source code is generally held in repositories, which could conceivably be attacked in order to poison the application. You will need to ensure that user access to the repository is controlled appropriately.

Hosts are networked together, often using a VPC for security, and typically connected to the internet. Exactly as in a traditional deployment, you need to protect the host machines (or virtual machines) from access by threat actors. Secure network configuration, firewalling, and identity and access management all still apply in a cloud native deployment as they do in a traditional deployment.

Containers typically run under an orchestrator - commonly Kubernetes in today’s deployments, though there are other options like Docker Swarm or Hashicorp Nomad. If the orchestrator is configured insecurely, or if administrative access is not controlled effectively, this gives attackers additional vectors to affect the deployment.

Note

For more on threat models in Kubernetes deployments, you may be interested to read the Kubernetes Threat Model commissioned by the CNCF.

In addition, the CNCF’s Financial User Group has published a Kubernetes Attack Tree created using the STRIDE methodology.

Security boundaries

A security boundary (sometimes called a trust boundary) appears between parts of the system, where you would need some different set of permissions in order to move to between those parts. Sometimes they are set up administratively - for example, in a Linux system, the sysadmin can modify the security boundary defining what files a user can access, by changing the groups that the user is a member of. If you are rusty on Linux file permissions, a refresher is coming up in Chapter 2.

A container is a security boundary. Application code is supposed to run within that container, and it should not be able to access code or data outside of the container except where it has been explicitly given permission to do so, for example through a volume mounted into the container).

The more security boundaries between an attacker and their target (your customer data, for example), the harder it is for them to reach that target.

The attack vectors described in “Container threat model” can be chained together to breach several security boundaries. For example:

An attacker may find that because of a vulnerability in an application dependency, they are able to execute code remotely within a container.

Suppose that the breached container doesn’t have direct access to any data of value. The attacker needs to find a way to move out of the container either to another container, or to the host. A container escape vulnerability would be one route out of the container; insecure configuration of that container could provide another. If the attacker finds either of these routes available, they can now access the host.

The next step would be to look for ways to gain root privileges on the host. This step might be trivial if your application code is running as root inside the container, as you’ll see in Chapter 4.

With root privileges on the host machine, the attacker can get to anything that the host - or any of the containers running on that host - can reach.

Adding and strengthening the security boundaries in your deployment will make life more difficult for the attacker.

An important aspect of the threat model is to consider the possibility of attacks from within the environment in which your applications are running. In cloud deployments, you may be sharing some resources with other users and their applications. Sharing machine resources is called multi-tenancy, and it has a significant bearing on the threat model.

Multi-tenancy

In a multi-tenant environment, different users, or tenants, run their workloads on shared hardware. (You may also across the term “multi-tenancy” in a software application context, where it refers to multiple users sharing the same instance of software, but for the purposes of this discussion, only the hardware is shared.) Depending on who owns those different workloads, and how much the different tenants trust each other, you might need stronger boundaries between them to prevent them interfering with each other.

Multi-tenancy as a concept has been around since the mainframe days in the 1960s, when customers rented CPU time, memory and storage on a shared machine. This is not so very different from today’s public clouds, like Amazon AWS, Microsoft Azure and Google Cloud Platform, where customers rent CPU time, memory and storage, along with other features and managed services. Since Amazon AWS launched EC2 back in 2006, we have been able to rent virtual machine instances running on racks of servers in data centers around the world. There may be many virtual machines (VMs) running on a physical machine, and as a cloud customer operating a set of VMs you have no idea about who else is operating the VMs that neighbor yours.

Shared machines

There are situations where a single Linux machine (or virtual machine) may be shared by many users. This is very common in, for example, university settings, and this is a good example of true multi-tenancy where users don’t trust each other, and quite frankly the system administrators don’t trust the users. In this environment Linux access controls are used to stricly limit user access. Each user has their own login ID, and the access controls of Linux are used to limit access, for example to ensure that users can only modify files in their own directories. Can you imagine the chaos if university students could read, or even worse modify, their classmates’ files?

As you’ll see in Chapter 4, all the containers running on the same host share the same kernel. If the machine is running the Docker daemon, any user who can issue docker commands effectively has root access, so a system administrator won’t want to grant that to untrusted users.

In enterprise situations and more specifically in cloud native environments, you are less likely to see this kind of shared machine. Instead, users (or teams of users who trust each other) will typically use their own resources allocated to them in the form of virtual machines.

Virtualization

Generally speaking, virtual machines are considered to be pretty strongly isolated from each other, by which we mean that it’s unlikely that your neighbors can observe or interfere with the activities in your VMs. You can read more about how this isolation is achieved in Chapter 5. In fact, according to the accepted definition, virtualization doesn’t count as multi-tenancy at all: multi-tenancy is when different groups of people share a single instance of the same software, and in virtualization the users don’t have access to the hypervisor that manages their virtual machines, so they don’t share any software.

That’s not to say that the isolation between virtual machines is perfect, and historically users have complained about “noisy neighbor” issues, where the fact that your’re sharing a physical machine with other users can result in unexpected variances in performance. Netflix were early adopters of the public cloud, and in the section on “Co-tenancy is hard” in a 2010 blog post, they acknowledged that they built systems that might deliberately abandon a subtask if it proved to be operating too slowly. More recently, others have claimed that the noisy neighbor problem isn’t a real issue.

There have also been cases of software vulnerabilities that could compromise the boundary between virtual machines.

For some applications, and some organizations (especially government, financial or healthcare) the consequences of a security breach are sufficiently serious to warrant full physical separation. You can operate a private cloud, running in your own data center, or managed by a service provider on your behalf, to ensure total isolation of your workloads. Private clouds sometimes come with additional security features such as additional background checks on the personnel who have access to the data center.

Many cloud providers have VM options where you are guaranteed to be the only customer on a physical machine. It’s also possible to rent bare-metal machines operated by cloud providers. In both these scenarios, you will completely avoid the noisy neighbor issue, and you also have the advantage of the stronger security isolation between physical machines.

Whether you are renting physical or virtual machines in the cloud, or using your own servers, if you’re running containers you may need to consider the security boundaries between multiple different groups of users.

Container multi-tenancy

As you’ll see in Chapter 4, the isolation between containers is not as strong as that between VMs. While it does depend on your risk profile, it’s unlikely that you want to use containers on the same machine as a party that you don’t trust.

Even if all the containers running on your machines are run by you, or by people you absolutely trust, you might still want to mitigate against the fallibility of humans by making sure that your containers can’t interfere with each other.

In Kubernetes, you can use namespaces to subdivide a cluster of machines for use by different individuals, teams, or applications.

Note

The word “namespace” is an overloaded term. - In Kubernetes, a namespace refers to a high-level abstraction that subdivides cluster resources that can have different Kubernetes access controls applied to them. - In Linux, a namespace is a low-level mechanism for isolating the machine resources that a process is aware of. You’ll learn about this kind of namespace in detail in Chapter 4.

Use Role Based Access Control (RBAC) to limit the people and components who can access these different Kubernetes namespaces. The details of how to do this are outside the scope of this book, but I would like to mention that Kubernetes RBAC only controls the actions you can perform through the Kubernetes API. Application containers in Kubernetes pods that happen to be running on the same host are only protected from each other by container isolation, as described in this book, even if they are in different namespaces. If an attacker can escape a container to the host, the Kubernetes namespace boundary makes not one jot of difference to their ability to affect other containers.

Container instances

Cloud services such as Amazon AWS, Microsoft Azure or Google Cloud Platform offer many managed services, where the user can rent software, storage, and other components without having to install or manage them. A classic example is Amazon’s Relational Database Service (RDS) where you can easily provision databases that use well-known software like Postgresql, and getting your data backed up is as simple as ticking a box (and paying a bill, of course).

Managed services have extended to the world of containers too. Azure Container Instances and AWS Fargate are services that allow you to run containers without having to worry about the underlying machine (or virtual machine) on which they run.

This can save you from a significant management burden, and allows you to easily scale the deployment at will. However, at least in theory, your container instances could be co-located on the same virtual machine as those from other customers. Check with your cloud provider if in doubt.

You are now aware of a good number of potential threats to your deployment. Before we dive into the rest of the book, I’d like to introduce some basic security principles that should guide your thinking when assessing what security tools and processes you need to introduce into your deployment.

Security principles

These are general guidelines that are commonly considered to be a wise approach regardless of the details of what you’re trying to secure.

Least privilege

The principle of least privilege states that you should limit access to the bare minimum that a person or component needs in order to do their job. For example, if you have a microservice that performs product search in an e-commerce application, the principle of least privilege suggests that the microservice should only have credentials that give it read-only access to the product database. It has no need to access, say, user or payment information, and it has no need to write product information.

Defence in depth

As you’ll see in this book, there are many different ways you can improve the security of your deployment and the applications running within it. The principle of Defence In Depth tells us that you should apply layers of protection. If an attacker is able to breach one defence, another layer should prevent them from harming your deployment or exfiltrating your data.

Reducing the attack surface

As a general rule, the more complex a system, the more likely it is that there is a way to attack it. Eliminating complexity can make the system harder to attack. This includes

reducing access points by keeping interfaces small and simple where possible

limiting the users and components who can access a service

minimizing the amount of code.

Limiting the blast radius

The concept of segmenting security controls into smaller sub-components or “cells” means that should the worst happen, the impact is limited. Containers are well-suited to this principle, because by dividing an architecture into many instances of a microservice, the container itself can act as a security boundary.

Segregation of duties

Related to both least privilege and limiting blast radius is the idea of segregating duties, so that as far as possible different components or people are given authority over only the smallest subset of the overall system that they need. This limits the damage a single privileged user might inflict, by ensuring that certain operations require more than one user’s authority.

Applying security principles with containers

As you’ll see in later sections of this book, the granularity of containers can help us in the application of all these security principles.

Least privilege: you can give different containers different sets of privileges, each minimized to the smallest set of permissions it needs to fulfill its function.

Defence in depth: containers give another boundary where security protections can be enforced.

Reducing the attack surface: splitting a monolith into simple microservices can create clean interfaces between them which may, if carefully designed, reduce complexity and hence limit the attack surface. There is a counter-argument that adding a complex orchestration layer to co-ordinate containers introduces another attack surface.

Limiting the blast radius: if a containerized application is compromised, security controls can help constrain the attack within the container and prevent it from affecting the rest of the system.

Segregation of duties: permissions and credentials can be passed only into the containers that need them, so that the compromise of one set of secrets does not necessarily mean that all are lost.

These benefits sound good, but they are somewhat theoretical. In practice they can easily be outweighed by poor system configuration, bad container image hygiene, or insecure practices. By the end of these book you should be well armed to avoid the security pitfalls that can appear in a containerized deployment, and take advantage of the benefits.

Summary

You’ve now got a high-level view of the kinds of attacks that can affect a container-based deployment, and an introduction to the security principles that you can apply to defend against those attacks. In the rest of the book you’ll dive into the mechanisms that underpin containers, so that you can understand how security tools and best-practice processes combine to implement those security principles.
