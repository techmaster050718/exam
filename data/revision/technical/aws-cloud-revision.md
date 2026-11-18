# AWS / Cloud Interview Revision

## EC2
**What is it?** EC2 provides virtual server instances. **Interview answer:** "I choose instance type and placement, attach storage and IAM role, and usually use it for workload-specific control." **Example:** Custom application server. **Use:** IaaS. **Points:** AMI, scaling, billing. **Follow-ups:** EC2 vs Lambda.

## S3
**What is it?** S3 is durable object storage. **Interview answer:** "I store objects by key and control access with IAM and signed URLs." **Example:** Images and backups. **Use:** Files and static assets. **Points:** Object versioning, lifecycle, encryption. **Follow-ups:** Strong consistency.

## IAM
**What is it?** AWS IAM defines identities and authorization policies. **Interview answer:** "I grant least privilege with scoped roles and short-lived credentials." **Example:** Worker can write one bucket prefix. **Use:** AWS security. **Points:** Principal, action, resource, MFA. **Follow-ups:** Role vs policy.

## VPC
**What is it?** A VPC is an isolated virtual network. **Interview answer:** "I separate public and private subnets and control traffic with route tables and security groups." **Example:** Public ALB and private database. **Use:** Cloud networking. **Points:** CIDR, NAT, NACL. **Follow-ups:** Security group statefulness.

## RDS
**What is it?** RDS provides managed relational databases. **Interview answer:** "AWS manages patching and backups while I manage schema, queries, capacity, and access." **Example:** PostgreSQL for orders. **Use:** Managed SQL. **Points:** Multi-AZ, read replica, backup. **Follow-ups:** RDS vs EC2 database.

## Lambda
**What is it?** Lambda runs event-triggered functions without server management. **Interview answer:** "I use short, stateless functions for spiky workloads and isolate cold starts." **Example:** Resize images after upload. **Use:** Serverless. **Points:** Timeout, concurrency, IAM. **Follow-ups:** Cold start.

## CloudWatch
**What is it?** CloudWatch collects AWS metrics, logs, and alarms. **Interview answer:** "I create dashboards and alert on service-level symptoms." **Example:** API 5xx and latency alarms. **Use:** AWS observability. **Points:** Metrics, logs, alarms. **Follow-ups:** CloudWatch vs Prometheus.

## Route 53
**What is it?** Route 53 is AWS DNS and health-aware routing. **Interview answer:** "I map domains and can route by latency or failover." **Example:** Regional API records. **Use:** DNS. **Points:** Records, health check, TTL. **Follow-ups:** Latency vs failover routing.

## ECS
**What is it?** ECS runs containers with AWS-native orchestration. **Interview answer:** "I define tasks and services and let ECS place and maintain them." **Example:** Run a backend API. **Use:** AWS containers. **Points:** Task, service, Fargate. **Follow-ups:** ECS vs EKS.

## EKS
**What is it?** EKS provides a managed Kubernetes control plane. **Interview answer:** "I use Kubernetes APIs while AWS manages control-plane infrastructure." **Example:** Multi-service platform. **Use:** Kubernetes in AWS. **Points:** Nodes, IRSA, ingress. **Follow-ups:** EKS vs ECS.

## SQS
**What is it?** SQS is a managed queue. **Interview answer:** "A producer sends jobs and workers poll and delete them after success." **Example:** Async report creation. **Use:** Decoupling. **Points:** At-least-once, DLQ, visibility. **Follow-ups:** FIFO vs standard.

## SNS
**What is it?** SNS is a managed pub/sub notification service. **Interview answer:** "SNS fans out events to queues or endpoints." **Example:** Order event reaches payment and email queues. **Use:** Fan-out. **Points:** Topic, subscription. **Follow-ups:** SNS vs SQS.

## Cloud Service Models
**What is it?** IaaS gives infrastructure, PaaS gives managed runtime, and SaaS delivers a complete application. **Interview answer:** "Serverless is managed execution; the shared responsibility boundary changes." **Example:** EC2 vs Elastic Beanstalk vs Salesforce-like SaaS. **Use:** Build vs buy. **Points:** Responsibility, flexibility. **Follow-ups:** FaaS.

## Scalability, Elasticity & Availability
**What is it?** Scalability adds capacity; elasticity adds and removes it automatically; availability is readiness to serve. **Interview answer:** "I design for peak growth, automatic response, redundancy, and measured uptime." **Example:** Video launch. **Points:** Horizontal scale, AZs, MTBF/MTTR.

## Regions & Availability Zones
**What is it?** A region is a geographic AWS area; AZs are isolated locations inside it. **Interview answer:** "I place replicas across AZs and use multiple regions only for recovery requirements." **Example:** Multi-AZ database. **Points:** Latency, residency, cost. **Follow-ups:** Active-passive.

## Object Storage & Cloud Networking
**What is it?** Object storage holds durable blobs; cloud networking isolates and routes virtual resources. **Interview answer:** "S3 stores objects while VPC subnets and endpoints control network flow." **Example:** Private service upload. **Points:** Endpoints, routing, encryption.

## Cloud Security
**What is it?** Cloud security combines identity, network, data, and workload controls. **Interview answer:** "The provider secures infrastructure while I secure configuration and workloads." **Example:** Private database and encrypted S3. **Points:** IAM, encryption, logging. **Follow-ups:** Shared responsibility.
