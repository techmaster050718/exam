# ☁️ CLOUD COMPUTING — COMPLETE REVISION GUIDE
> Government Exam Oriented | Covers AWS, Azure, DevOps, Security, Cost
> Last Updated: 2026-11-15

---

## Cloud command map
| Domain | Core recall points |
| :--- | :--- |
| Service models | IaaS, PaaS, SaaS, FaaS and responsibility split |
| Deployment models | Public, private, hybrid, multi-cloud |
| Virtualization | Hypervisors, VMs, containers, isolation trade-offs |
| Orchestration | Docker, Kubernetes pods, deployments, services |
| Exam focus | Cloud responsibility, deployment choices, architecture memory |

---

## 1. Cloud Service Models (IaaS / PaaS / SaaS / FaaS)

### Concept
Cloud computing delivers IT resources over the internet on a pay-as-you-go basis.
The four service models differ by **who manages what**.

### Who Manages What — Comparison Table

| Layer               | On-Premise | IaaS | PaaS | SaaS | FaaS |
|---------------------|-----------|------|------|------|------|
| Applications        | You       | You  | You  | Provider | Provider |
| Data                | You       | You  | You  | Provider | Provider |
| Runtime             | You       | You  | Provider | Provider | Provider |
| Middleware          | You       | You  | Provider | Provider | Provider |
| OS                  | You       | You  | Provider | Provider | Provider |
| Virtualization      | You       | Provider | Provider | Provider | Provider |
| Servers             | You       | Provider | Provider | Provider | Provider |
| Storage             | You       | Provider | Provider | Provider | Provider |
| Networking          | You       | Provider | Provider | Provider | Provider |

```
Responsibility Pyramid:
                  ┌─────────────┐
                  │    SaaS     │  ← Provider manages everything
                  ├─────────────┤
                  │    PaaS     │  ← You manage app + data
                  ├─────────────┤
                  │    IaaS     │  ← You manage OS upward
                  ├─────────────┤
                  │  On-Prem    │  ← You manage everything
                  └─────────────┘
```

### Model Details & Examples

| Model | Full Form | What You Get | Examples | Use Case |
|-------|-----------|-------------|----------|----------|
| **IaaS** | Infrastructure as a Service | VMs, Storage, Networking | AWS EC2, Azure VM, GCP Compute Engine | Full control, custom OS |
| **PaaS** | Platform as a Service | Runtime + Middleware + OS | AWS Elastic Beanstalk, Azure App Service, Heroku | App dev without infra mgmt |
| **SaaS** | Software as a Service | Ready-to-use software | Gmail, Office 365, Salesforce, Zoom | End-user applications |
| **FaaS** | Function as a Service | Execute code per event | AWS Lambda, Azure Functions, GCP Cloud Functions | Event-driven, serverless |

### Key Exam Points
- **IaaS** → Most flexible, most control, most responsibility
- **SaaS** → Least control, least responsibility, fastest deployment
- **PaaS** → Middle ground; ideal for developers
- **FaaS** = Serverless; billed per millisecond of execution (not per VM hour)

> **⚠️ Common Trap:** "Serverless" doesn't mean no servers — it means YOU don't manage servers. Provider handles all infra.

---

## 2. Cloud Deployment Models

### Public Cloud
- Infrastructure owned and operated by third-party provider
- Shared with other tenants (multi-tenant)
- **Pros:** Low cost, high scalability, no capex, global reach
- **Cons:** Less control, compliance concerns, shared environment
- **Examples:** AWS, Azure, GCP, Oracle Cloud

### Private Cloud
- Dedicated infrastructure for single organization
- On-premise OR hosted by provider (but isolated)
- **Pros:** Maximum control, compliance-friendly, security
- **Cons:** High capex, needs IT team, limited scalability
- **Examples:** OpenStack, VMware vSphere, AWS GovCloud

### Hybrid Cloud
- Combination of public + private cloud, interconnected
- **Pros:** Flexibility, sensitive data on-prem, burst to public
- **Cons:** Complex networking, latency, management overhead
- **Examples:** Azure Arc, AWS Outposts, Google Anthos

### Multi-Cloud
- Using multiple public cloud providers simultaneously
- **Pros:** No vendor lock-in, best-of-breed services, redundancy
- **Cons:** Complex management, different APIs, skill requirements
- **Examples:** AWS + Azure + GCP simultaneously

### Comparison Table

| Feature | Public | Private | Hybrid | Multi-Cloud |
|---------|--------|---------|--------|-------------|
| Cost | Low (OpEx) | High (CapEx) | Medium | Medium-High |
| Control | Low | High | Medium | Medium |
| Security | Shared | Dedicated | Mixed | Mixed |
| Scalability | Very High | Limited | High | Very High |
| Compliance | Harder | Easier | Flexible | Complex |
| Setup Time | Minutes | Months | Weeks | Weeks |

> **⚠️ Common Trap:** Hybrid ≠ Multi-cloud. Hybrid = public+private integration. Multi-cloud = multiple public providers.

---

## 3. Virtualization

### What is Virtualization?
Creating virtual (software-based) versions of hardware resources, allowing multiple OS instances on one physical machine.

### Type-1 vs Type-2 Hypervisor

```
TYPE-1 (Bare Metal):              TYPE-2 (Hosted):
┌─────────────────────┐           ┌─────────────────────┐
│  VM1   │  VM2  │VM3 │           │  VM1  │  VM2  │  VM3 │
├─────────────────────┤           ├─────────────────────┤
│    Hypervisor       │           │   Hypervisor        │
├─────────────────────┤           ├─────────────────────┤
│   Hardware          │           │      Host OS        │
└─────────────────────┘           ├─────────────────────┤
                                  │      Hardware       │
                                  └─────────────────────┘
```

| Feature | Type-1 (Bare Metal) | Type-2 (Hosted) |
|---------|--------------------|-----------------| 
| Runs on | Directly on hardware | On host OS |
| Performance | High | Lower (extra layer) |
| Security | More secure | Less secure |
| Examples | VMware ESXi, Microsoft Hyper-V, Xen, KVM | VMware Workstation, VirtualBox, Parallels |
| Use Case | Production, Data Centers | Development, Testing |

### Containers vs Virtual Machines

```
VIRTUAL MACHINES:                  CONTAINERS:
┌──────┬──────┬──────┐             ┌──────┬──────┬──────┐
│App A │App B │App C │             │App A │App B │App C │
├──────┼──────┼──────┤             ├──────┴──────┴──────┤
│Guest │Guest │Guest │             │   Container Engine  │
│ OS   │  OS  │  OS  │             │   (Docker/containerd)│
├──────┴──────┴──────┤             ├────────────────────┤
│    Hypervisor      │             │      Host OS        │
├────────────────────┤             ├────────────────────┤
│     Hardware       │             │      Hardware       │
└────────────────────┘             └────────────────────┘
```

| Feature | Virtual Machines | Containers |
|---------|-----------------|------------|
| OS | Full OS per VM | Shared host OS kernel |
| Size | GBs | MBs |
| Boot time | Minutes | Seconds |
| Isolation | Strong (hardware-level) | Process-level |
| Portability | Low | High |
| Performance | Lower | Near-native |
| Use Case | Full isolation needed | Microservices, CI/CD |
| Example | VMware, Hyper-V, KVM | Docker, Podman, LXC |

> **⚠️ Common Trap:** Containers share the HOST OS kernel — they are NOT fully isolated. VMs have their own kernel.

---

## 4. Linux Containers (Docker & Kubernetes)

### Linux Primitives Enabling Containers

| Feature | Purpose | Example |
|---------|---------|---------|
| **cgroups** (Control Groups) | Limit/isolate resource usage (CPU, memory, I/O) | Container can't use >512MB RAM |
| **namespaces** | Isolate system resources (PID, network, mount, user) | Container sees its own process tree |
| **Union FS** | Layered filesystem (overlayFS) | Docker image layers |
| **seccomp** | Restrict syscalls | Security hardening |

### Docker Lifecycle

```
Dockerfile → docker build → IMAGE → docker run → CONTAINER
                                 ↑                    ↓
                           docker pull           docker stop
                           (from Registry)       docker rm
```

| Docker Command | Action |
|---------------|--------|
| `docker build -t name .` | Build image from Dockerfile |
| `docker pull image:tag` | Download image from registry |
| `docker run -d -p 8080:80 image` | Run container (detached, port map) |
| `docker ps` | List running containers |
| `docker stop <id>` | Stop container |
| `docker exec -it <id> bash` | Shell into running container |
| `docker images` | List local images |
| `docker rmi <image>` | Remove image |
| `docker-compose up` | Start multi-container app |

### Kubernetes (K8s) Core Concepts

```
CLUSTER
├── Control Plane (Master)
│   ├── API Server     → entry point for all operations
│   ├── Scheduler      → assigns pods to nodes
│   ├── Controller Mgr → maintains desired state
│   └── etcd           → distributed key-value store (cluster state)
└── Worker Nodes
    ├── kubelet        → node agent, runs pods
    ├── kube-proxy     → network proxy
    └── Container Runtime (containerd/Docker)
```

| K8s Object | Description | Exam Key Point |
|-----------|-------------|----------------|
| **Pod** | Smallest deployable unit; 1+ containers | Ephemeral, gets new IP on restart |
| **Service** | Stable network endpoint for pods | Types: ClusterIP, NodePort, LoadBalancer |
| **Deployment** | Manages pod replicas + rolling updates | Declarative desired state |
| **ReplicaSet** | Ensures N pod replicas running | Usually managed by Deployment |
| **Ingress** | HTTP/HTTPS routing rules to services | Needs Ingress Controller (nginx, traefik) |
| **ConfigMap** | Store non-secret config data | Environment variables or mounted files |
| **Secret** | Store sensitive data (base64 encoded) | NOT encrypted by default |
| **PersistentVolume** | Storage resource in cluster | Decoupled from pod lifecycle |
| **Namespace** | Virtual cluster partitioning | Default, kube-system, kube-public |
| **DaemonSet** | Run pod on every node | Log collectors, monitoring agents |

> **⚠️ Common Trap:** K8s Secrets are base64 encoded, NOT encrypted. Use external vault (HashiCorp Vault / AWS Secrets Manager) for real security.

---

## 5. AWS Core Services

### Compute

| Service | Purpose | Key Facts |
|---------|---------|-----------|
| **EC2** | Virtual machines in cloud | Instance types: t3, m5, c5, r5, p3 (GPU). AMI = image |
| **Lambda** | Serverless functions | Max 15 min timeout, 10GB memory, event-driven |
| **ECS** | Container orchestration (AWS-native) | Fargate = serverless containers |
| **EKS** | Managed Kubernetes | AWS-managed K8s control plane |
| **Auto Scaling** | Automatic EC2 scaling | Based on CloudWatch metrics |

### Storage

| Service | Type | Key Facts |
|---------|------|-----------|
| **S3** | Object storage | 11 nines durability, buckets globally unique, classes: Standard/IA/Glacier |
| **EBS** | Block storage | Attached to EC2, AZ-bound, SSD/HDD types |
| **EFS** | File storage (NFS) | Shared across EC2 instances, auto-scales |
| **Glacier** | Archive storage | Retrieval: Expedited(1-5min), Standard(3-5hr), Bulk(5-12hr) |
| **Storage Gateway** | Hybrid cloud storage | On-prem to AWS bridge |

### Database

| Service | Type | Key Facts |
|---------|------|-----------|
| **RDS** | Managed relational DB | MySQL, PostgreSQL, Oracle, SQL Server, MariaDB |
| **Aurora** | Cloud-native relational | 5x MySQL speed, 3x PostgreSQL, multi-AZ by default |
| **DynamoDB** | NoSQL key-value | Single-digit ms latency, DAX = in-memory cache |
| **ElastiCache** | In-memory cache | Redis or Memcached |
| **Redshift** | Data warehouse | Columnar, petabyte-scale analytics |

### Networking & Security

| Service | Purpose | Key Facts |
|---------|---------|-----------|
| **VPC** | Virtual private cloud | Your isolated network in AWS |
| **Security Groups** | Instance-level firewall | Stateful, allow rules only |
| **NACL** | Subnet-level firewall | Stateless, allow + deny rules |
| **IAM** | Identity & Access Management | Users, Groups, Roles, Policies |
| **CloudFront** | CDN | 450+ edge locations, integrates with S3, ALB |
| **Route 53** | DNS service | Routing: Simple, Weighted, Latency, Failover, Geolocation |
| **ELB** | Load Balancer | ALB (HTTP/layer7), NLB (TCP/layer4), CLB (legacy) |
| **CloudTrail** | API audit logging | Who did what, when, from where |
| **CloudWatch** | Monitoring & alerting | Metrics, Logs, Alarms, Events |
| **KMS** | Key Management Service | Encryption key management, CMKs |
| **WAF** | Web Application Firewall | Protects against SQL injection, XSS |

> **⚠️ Common Trap:** S3 bucket names are globally unique across ALL AWS accounts. EBS volumes are AZ-scoped (cannot attach to EC2 in different AZ).

---

## 6. Azure Core Services

### Compute

| Service | AWS Equivalent | Key Facts |
|---------|---------------|-----------|
| **Azure VM** | EC2 | Sizes: B-series (burstable), D-series (general), N-series (GPU) |
| **Azure Functions** | Lambda | Serverless, consumption/premium plan |
| **AKS** | EKS | Azure Kubernetes Service, managed K8s |
| **Azure App Service** | Elastic Beanstalk | PaaS web hosting |
| **Azure Container Instances** | ECS Fargate | Serverless containers |

### Storage

| Service | AWS Equivalent | Key Facts |
|---------|---------------|-----------|
| **Blob Storage** | S3 | Hot/Cool/Archive tiers; Block/Append/Page blobs |
| **Azure Disk** | EBS | Managed disk attached to VM |
| **Azure Files** | EFS | SMB/NFS file shares |
| **Azure Data Lake Storage** | S3 + analytics | ADLS Gen2 on top of Blob |

### Networking & Identity

| Service | AWS Equivalent | Key Facts |
|---------|---------------|-----------|
| **VNet** | VPC | Virtual Network, subnets, NSGs |
| **NSG** | Security Group | Network Security Group, stateful |
| **Azure CDN** | CloudFront | Content delivery network |
| **Azure DNS** | Route 53 | DNS hosting |
| **Azure AD (Entra ID)** | IAM + Cognito | Cloud identity: SSO, MFA, B2B/B2C |
| **Azure Monitor** | CloudWatch | Logs, Metrics, Alerts, Dashboards |
| **Azure SQL Database** | RDS | Managed SQL Server, PaaS |
| **Azure Cosmos DB** | DynamoDB | Multi-model NoSQL, global distribution |

> **⚠️ Common Trap:** Azure AD (now Microsoft Entra ID) is NOT traditional Active Directory — it's cloud-based identity. For on-prem AD in cloud, use Azure AD DS.

---

## 7. Cloud Storage Types

| Type | Description | Access Pattern | Examples | When to Use |
|------|-------------|---------------|----------|-------------|
| **Block** | Raw storage volumes, like hard disks | Low-latency random read/write | AWS EBS, Azure Disk, GCP Persistent Disk | Databases, OS boot volumes |
| **Object** | Files stored as objects with metadata | High-throughput, parallel | AWS S3, Azure Blob, GCP GCS | Backups, media, static websites, data lakes |
| **File** | Shared filesystem (NFS/SMB) | Multiple concurrent clients | AWS EFS, Azure Files, GCP Filestore | Shared app data, home directories, CMS |
| **Archive** | Long-term cold storage | Infrequent, slow retrieval | AWS Glacier, Azure Archive, GCP Coldline | Compliance archives, old backups |

```
Block:   [  512B block ][  512B block ][  512B block ]  ← raw I/O
Object:  { key: "file.jpg", data: ..., metadata: {...} } ← HTTP API
File:    /shared/dir/file.txt  ← POSIX filesystem
Archive: Tape-like, retrieval hours/days
```

| Feature | Block | Object | File | Archive |
|---------|-------|--------|------|---------|
| Latency | ms | ms-s | ms-s | Hours |
| Scalability | Limited | Unlimited | High | Unlimited |
| Access | Direct I/O | HTTP REST | NFS/SMB | Retrieval jobs |
| Cost | Highest | Medium | Medium | Lowest |
| Shareable | No | Yes | Yes | No |

---

## 8. Cloud Networking

### VPC / VNet Architecture

```
VPC / VNet (e.g., 10.0.0.0/16)
├── Public Subnet (10.0.1.0/24)
│   ├── EC2 / VM (with public IP)
│   ├── Load Balancer
│   └── Internet Gateway ──→ Internet
├── Private Subnet (10.0.2.0/24)
│   ├── Database
│   ├── App servers
│   └── NAT Gateway (outbound only)
└── Management Subnet (10.0.3.0/24)
    └── Bastion Host (jump server)
```

### Key Networking Concepts

| Concept | Description | Exam Point |
|---------|-------------|------------|
| **Internet Gateway** | Allows VPC ↔ Internet | Required for public subnets |
| **NAT Gateway** | Private subnet → Internet (outbound only) | Prevents inbound from internet |
| **Security Group** | Instance-level stateful firewall | Only ALLOW rules; tracks connection state |
| **NACL** | Subnet-level stateless firewall | Allow + DENY rules; evaluate in order |
| **VPC Peering** | Direct connection between 2 VPCs | Not transitive (A↔B, B↔C ≠ A↔C) |
| **Transit Gateway** | Hub for connecting multiple VPCs | Transitive routing supported |
| **VPN Gateway** | Encrypted tunnel to on-prem | IPSec over internet |
| **Direct Connect** | Dedicated physical line to AWS | Low latency, consistent bandwidth |
| **CDN** | Cache content at edge locations | CloudFront, Azure CDN, Akamai |
| **Load Balancer** | Distribute traffic across targets | Layer 4 (TCP) or Layer 7 (HTTP) |

### Security Groups vs NACLs

| Feature | Security Group | NACL |
|---------|---------------|------|
| Level | Instance (ENI) | Subnet |
| State | Stateful | Stateless |
| Rules | Allow only | Allow + Deny |
| Rule Evaluation | All rules evaluated | In order (lowest # first) |
| Default | Deny all in, allow all out | Allow all in and out |
| Return Traffic | Auto-allowed | Must explicitly allow |

---

## 9. Cloud Security

### Shared Responsibility Model

```
AWS SHARED RESPONSIBILITY MODEL:

CUSTOMER RESPONSIBILITY ("Security IN the cloud"):
  ├── Customer data
  ├── Platform, applications, identity & access mgmt
  ├── OS, network, firewall configuration
  ├── Client-side data encryption
  └── Server-side encryption

AWS RESPONSIBILITY ("Security OF the cloud"):
  ├── Hardware / Global Infrastructure
  ├── Regions, AZs, Edge Locations
  ├── Compute, Storage, Database, Networking
  └── Software (hypervisor, managed service software)
```

| Service Type | Customer Manages | AWS Manages |
|-------------|-----------------|-------------|
| IaaS (EC2) | OS, apps, data, firewall | Hardware, hypervisor |
| PaaS (RDS) | Data, access, encryption | OS, DB patches, hardware |
| SaaS (S3) | Data, IAM policies | Everything else |

### IAM Key Concepts

| Component | Description | Example |
|-----------|-------------|---------|
| **User** | Individual identity | john@company.com |
| **Group** | Collection of users | Developers, Admins |
| **Role** | Assumed identity (temp credentials) | EC2 role to access S3 |
| **Policy** | JSON document defining permissions | Allow s3:PutObject |
| **MFA** | Multi-factor authentication | Mandatory for root account |

### IAM Best Practices
1. **Never use root account** for daily tasks
2. Apply **least privilege** principle
3. Enable **MFA** for all privileged users
4. Use **roles** instead of access keys for EC2
5. Rotate credentials regularly
6. Use **CloudTrail** to audit all API calls

### Key Security Services

| Service | Purpose |
|---------|---------|
| **KMS** | Create and manage encryption keys |
| **WAF** | Block SQLi, XSS, bad bots |
| **Shield** | DDoS protection (Standard free, Advanced paid) |
| **GuardDuty** | Threat detection using ML |
| **Inspector** | Vulnerability assessment for EC2/containers |
| **Macie** | Discover sensitive data in S3 |
| **CloudTrail** | Log all API activity |
| **Config** | Track resource configuration changes |
| **SSM** | Systems Manager — patch, session manager |

> **⚠️ Common Trap:** CloudWatch monitors PERFORMANCE (CPU, memory). CloudTrail monitors API CALLS (who did what). Different purposes!

---

## 10. Cloud Cost Optimization

### EC2 Pricing Models

| Model | Description | Discount | Use Case |
|-------|-------------|----------|----------|
| **On-Demand** | Pay per hour/second, no commitment | Baseline (0%) | Dev/test, unpredictable workloads |
| **Reserved (1yr)** | 1-year commitment | Up to 40% | Steady-state production |
| **Reserved (3yr)** | 3-year commitment | Up to 60% | Long-running stable workloads |
| **Spot** | Bid for unused capacity | Up to 90% | Fault-tolerant, batch, CI/CD |
| **Savings Plans** | Flexible commitment by $ amount | Up to 66% | Mixed instance usage |
| **Dedicated Host** | Physical server dedicated to you | Premium | Compliance, licensing |

### Cost Optimization Strategies

```
COST OPTIMIZATION PILLARS:
┌─────────────────────────────────────────────┐
│ 1. RIGHT-SIZING                             │
│    Monitor → Downsize oversized instances   │
│    Tools: AWS Compute Optimizer             │
├─────────────────────────────────────────────┤
│ 2. PURCHASE OPTIMIZATION                    │
│    Reserved/Savings Plans for steady state  │
│    Spot for fault-tolerant workloads        │
├─────────────────────────────────────────────┤
│ 3. AUTO SCALING                             │
│    Scale out during peak, in during off-peak│
│    Eliminate idle resources                 │
├─────────────────────────────────────────────┤
│ 4. STORAGE OPTIMIZATION                     │
│    S3 lifecycle rules (Hot→Cool→Archive)   │
│    Delete unattached EBS volumes            │
├─────────────────────────────────────────────┤
│ 5. TAGGING & VISIBILITY                     │
│    Tag all resources with cost centers      │
│    Use Cost Explorer, Budgets, Anomaly Det. │
└─────────────────────────────────────────────┘
```

| Tool | Purpose |
|------|---------|
| AWS Cost Explorer | Visualize and analyze costs |
| AWS Budgets | Set spending alerts |
| Compute Optimizer | Right-size recommendations |
| Trusted Advisor | Best practice checks (cost, security, performance) |
| Spot Advisor | View Spot interruption rates |

> **⚠️ Common Trap:** Spot instances CAN be terminated with 2-minute warning by AWS when capacity is needed. Never use for databases or non-fault-tolerant apps.

---

## 11. High Availability & Disaster Recovery

### Key Metrics

| Metric | Full Form | Definition | Formula |
|--------|-----------|------------|---------|
| **RTO** | Recovery Time Objective | Max acceptable downtime | Time to restore service |
| **RPO** | Recovery Point Objective | Max acceptable data loss | Time since last backup |
| **MTTR** | Mean Time To Recovery | Average time to recover | — |
| **MTBF** | Mean Time Between Failures | Average uptime between failures | — |

```
TIMELINE:
Disaster        RPO          RTO       Service Restored
   │◄───────────►│◄───────────►│
   │  Data loss  │  Downtime   │
   │  (acceptable)│(acceptable) │
```

### Availability Zones & Regions

```
AWS REGION (e.g., us-east-1)
├── Availability Zone A (us-east-1a)
│   ├── Data Center 1
│   └── Data Center 2
├── Availability Zone B (us-east-1b)
│   └── Data Center 3
└── Availability Zone C (us-east-1c)
    └── Data Center 4

AZs: physically separate, low-latency fiber interconnects
Regions: geographically separated (for DR)
```

### DR Strategies (Cost vs RTO/RPO)

| Strategy | Description | RTO | RPO | Cost |
|----------|-------------|-----|-----|------|
| **Backup & Restore** | Backups only, restore from scratch | Hours | Hours | $ |
| **Pilot Light** | Core infra running (DB only), scale up on disaster | 10s min | Minutes | $$ |
| **Warm Standby** | Scaled-down version running | Minutes | Seconds | $$$ |
| **Active-Active** | Full capacity in multiple regions simultaneously | Seconds | Near-zero | $$$$ |
| **Active-Passive** | Primary active, secondary on standby | Minutes | Seconds | $$$ |

```
PILOT LIGHT:
Normal:   [Primary DB (live)] ←→ [Backup DB (synced)]
Disaster: [Start app servers in DR region] → [Redirect traffic]

WARM STANDBY:
Normal:   [Primary Full] ←→ [DR Scaled-Down (always running)]
Disaster: [Scale up DR] → [DNS failover]
```

> **⚠️ Common Trap:** RTO = Recovery TIME (downtime). RPO = Recovery POINT (data loss). Lower = better but costs more.

---

## 12. DevOps on Cloud

### CI/CD Pipeline

```
Developer → Git Push → [CI Pipeline]
                            ↓
                       Code Build
                            ↓
                       Unit Tests
                            ↓
                       Integration Tests
                            ↓
                       Security Scan
                            ↓
                       Build Artifact
                            ↓
                       [CD Pipeline]
                            ↓
                   Deploy to Staging
                            ↓
                   Automated Tests
                            ↓
                   Deploy to Production (Blue/Green or Canary)
```

| Tool | Type | Purpose |
|------|------|---------|
| **Jenkins** | CI/CD | Open-source automation server |
| **GitHub Actions** | CI/CD | GitHub-integrated pipelines |
| **AWS CodePipeline** | CI/CD | AWS native pipeline |
| **Azure DevOps** | CI/CD | Microsoft DevOps platform |
| **GitLab CI** | CI/CD | GitLab integrated pipelines |

### Infrastructure as Code (IaC)

| Tool | Provider | Language | Purpose |
|------|---------|---------|---------|
| **Terraform** | HashiCorp (Multi-cloud) | HCL | Declarative infra provisioning |
| **CloudFormation** | AWS | YAML/JSON | AWS resource provisioning |
| **ARM Templates** | Azure | JSON | Azure resource provisioning |
| **Bicep** | Azure | Bicep DSL | Simplified ARM templates |
| **Pulumi** | Multi-cloud | Python/JS/Go | IaC with real languages |
| **Ansible** | Red Hat | YAML (Playbooks) | Configuration management, not provisioning |

```
Terraform Workflow:
terraform init     → download providers
terraform plan     → preview changes
terraform apply    → create resources
terraform destroy  → tear down resources
```

### Monitoring & Observability

| Pillar | What | Tools |
|--------|------|-------|
| **Metrics** | Numerical measurements over time | CloudWatch, Azure Monitor, Prometheus |
| **Logs** | Text event records | CloudWatch Logs, ELK Stack, Splunk |
| **Traces** | Request flow across services | AWS X-Ray, Jaeger, Zipkin |
| **Alerting** | Notify on threshold breach | PagerDuty, OpsGenie, SNS |

| AWS Service | Azure Equivalent | Purpose |
|------------|-----------------|---------|
| CloudWatch | Azure Monitor | Metrics + Logs |
| CloudTrail | Azure Activity Log | API audit |
| X-Ray | Application Insights | Distributed tracing |
| GuardDuty | Azure Defender | Threat detection |

---

## 📌 MUST REMEMBER — Cloud Computing

| # | Key Fact |
|---|----------|
| 1 | IaaS → most control; SaaS → least control |
| 2 | Containers share HOST OS kernel; VMs have own kernel |
| 3 | Type-1 Hypervisor runs on bare metal (VMware ESXi, KVM, Xen) |
| 4 | S3 = 11 nines (99.999999999%) durability |
| 5 | Security Groups = Stateful; NACLs = Stateless |
| 6 | Spot instances can be interrupted with 2-min notice |
| 7 | CloudWatch = performance monitoring; CloudTrail = API audit |
| 8 | RTO = downtime tolerance; RPO = data loss tolerance |
| 9 | VPC Peering is NOT transitive; Transit Gateway IS |
| 10 | K8s Secrets are base64 encoded, not encrypted |
| 11 | Active-Active = lowest RTO/RPO, highest cost |
| 12 | Pilot Light = DB synced, app servers off (fastest minimal DR) |
| 13 | Lambda max timeout = 15 minutes |
| 14 | Reserved instances = up to 60% savings over 3 years |
| 15 | Terraform: multi-cloud IaC; CloudFormation: AWS-only |

---

## ⚠️ COMMON TRAPS — Cloud Computing

| Trap | Reality |
|------|---------|
| "Serverless = no servers" | Servers exist; YOU just don't manage them |
| "S3 is a file system" | S3 is OBJECT storage, not a filesystem |
| "Hybrid = multi-cloud" | Hybrid = public+private; Multi-cloud = multiple publics |
| "SG denies all by default" | Inbound: deny all; Outbound: allow all by default |
| "NACL is stateful" | NACL is STATELESS; must add return traffic rules |
| "K8s Secrets are secure" | Base64 only; need external vault for real security |
| "Azure AD = on-prem AD" | Azure AD is cloud identity; AD DS for on-prem features |
| "Spot is always available" | Spot can be interrupted; not for critical workloads |
| "EBS can be shared" | EBS attaches to ONE EC2 (use EFS for sharing) |
| "Reserved = always running" | Reserved = billing commitment, not forced uptime |

---

## ⚡ 30-SECOND REVISION — Cloud Computing

```
SERVICE MODELS:    IaaS → VM | PaaS → Platform | SaaS → Software | FaaS → Function
DEPLOYMENT:        Public (shared) | Private (dedicated) | Hybrid | Multi-cloud
HYPERVISORS:       Type-1 = bare metal (ESXi) | Type-2 = on OS (VirtualBox)
CONTAINERS vs VMs: Containers = shared kernel, MBs, fast | VMs = own kernel, GBs, slow
K8s KEY OBJECTS:   Pod > ReplicaSet > Deployment | Service (ClusterIP/NodePort/LB) | Ingress
AWS STORAGE:       EBS=block | S3=object | EFS=file | Glacier=archive
SECURITY:          SG=stateful+allow | NACL=stateless+allow+deny | CloudTrail=audit
COST MODELS:       On-demand > Reserved(40-60%) > Spot(90%) | Savings Plans flexible
HA/DR:             RTO=downtime | RPO=data loss | Active-Active=best | Pilot Light=cheapest DR
DEVOPS:            CI/CD pipeline | Terraform=multi-cloud IaC | CloudFormation=AWS IaC
```
