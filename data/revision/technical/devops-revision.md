# DevOps Interview Revision

## Linux & Bash
**What is it?** Linux provides processes, permissions, filesystems, networking, and shell automation. **Interview answer:** "I use Bash for repeatable setup and operational commands, and I inspect logs and processes with standard tools." **Key idea:** Text pipelines and least-privilege execution. **Example:** Restart a stuck service and inspect journal logs. **Use:** Servers and containers. **Points:** Permissions, pipes, cron, signals. **Follow-ups:** Shell scripts, process zombie. **Related:** Docker → Kubernetes.

## Networking Basics
**What is it?** Networking lets hosts discover and exchange data. **Interview answer:** "I map a request through DNS, routing, TCP, TLS, firewall, load balancer, and application port." **Key idea:** Separate names, addresses, protocols, and security zones. **Example:** Debug why `api.example.com` times out. **Use:** Cloud and service operation. **Points:** DNS, IP, subnet, NAT, ports. **Follow-ups:** TCP vs UDP.

## Git & GitHub
**What is it?** Git tracks code history and branches; GitHub hosts collaboration and automation. **Interview answer:** "I create focused branches, rebase or merge carefully, open a reviewed pull request, and protect the main branch." **Example:** Fix a release bug through a hotfix branch. **Use:** Team delivery. **Points:** Commit, branch, merge, revert. **Follow-ups:** Rebase vs merge.

## Docker
**What is it?** Docker packages an application and dependencies into a portable image and container. **Interview answer:** "A Dockerfile defines a reproducible image; Docker creates isolated processes with private-ish filesystem and network namespaces." **Example:** Package a FastAPI service. **Use:** Consistent environments. **Points:** Images, layers, volumes, networks. **Follow-ups:** Container vs VM.

## Docker Compose
**What is it?** Compose defines a local or small multi-container application. **Interview answer:** "I describe API, database, cache, networks, and volumes in one file for local startup." **Example:** Start a web app with PostgreSQL and Redis. **Use:** Development and small deployments. **Points:** Overrides, secrets, healthchecks. **Follow-ups:** Compose vs Kubernetes.

## Kubernetes
**What is it?** Kubernetes schedules and reconciles containerized workloads. **Interview answer:** "A Deployment declares replicas of a Pod template; the controller creates Pods and Services provide stable discovery." **Example:** Deploy a stateless API across nodes. **Use:** Distributed container operations. **Points:** Pod, ReplicaSet, Service, HPA, probes. **Follow-ups:** Desired vs current state.

## Helm
**What is it?** Helm templates and versions Kubernetes application packages. **Interview answer:** "A chart parameterizes replicas and endpoints so the same application can deploy to staging and production." **Example:** Share a chart across environments. **Use:** Kubernetes packaging. **Points:** Chart, values, release. **Follow-ups:** Values secret handling.

## CI/CD Pipelines
**What is it?** CI builds and tests changes; CD promotes verified artifacts. **Interview answer:** "A pipeline runs lint and tests, builds an immutable image, scans it, then deploys by environment." **Example:** Merge to main triggers staging. **Use:** Repeatable delivery. **Points:** Artifact, gate, rollback. **Follow-ups:** Continuous delivery vs deployment.

## GitHub Actions
**What is it?** GitHub Actions executes workflows on repository events. **Interview answer:** "I define jobs, permissions, and secrets for pull-request checks and deployment." **Example:** Test PR and publish a container on release. **Use:** GitHub automation. **Points:** Runner, actions, OIDC, caches. **Follow-ups:** Reusable workflows.

## AWS Cloud
**What is it?** AWS provides managed compute, storage, networking, databases, and observability. **Interview answer:** "I choose managed services by requirements, cost, region, availability, and operational fit." **Example:** ECS, RDS, S3, CloudWatch. **Use:** Cloud infrastructure. **Points:** Shared responsibility, IAM. **Follow-ups:** EC2 vs ECS vs Lambda.

## Terraform
**What is it?** Terraform declares infrastructure and reconciles it through a state file. **Interview answer:** "I version modules and review plans before applying network or database changes." **Example:** Create VPC, subnets, and ECS. **Use:** Infrastructure as code. **Points:** Plan, apply, state, modules. **Follow-ups:** State locking.

## Ansible
**What is it?** Ansible configures systems through agentless SSH automation. **Interview answer:** "I use idempotent playbooks to install packages and enforce configuration." **Example:** Configure app nodes. **Use:** Configuration management. **Points:** Inventory, modules, idempotency. **Follow-ups:** Ansible vs Terraform.

## Nginx Reverse Proxy
**What is it?** Nginx accepts external traffic and forwards it to application targets. **Interview answer:** "I use Nginx for TLS, static assets, compression, and upstream routing." **Example:** Route `/api` to backend containers. **Use:** Edge HTTP. **Points:** Proxy_pass, TLS, health. **Follow-ups:** Reverse vs forward proxy.

## Load Balancers
**What is it?** Load balancers distribute traffic across healthy targets. **Interview answer:** "They improve capacity and availability while health checks remove failures." **Example:** Spread API traffic across zones. **Use:** Scalable services. **Points:** L4/L7, algorithms, sessions. **Follow-ups:** Sticky sessions.

## Prometheus
**What is it?** Prometheus scrapes time-series metrics and evaluates rules. **Interview answer:** "I expose counters and histograms and alert on SLO burn, not every isolated spike." **Example:** Track API latency. **Use:** Metrics and alerting. **Points:** Pull model, PromQL. **Follow-ups:** Cardinality.

## Grafana
**What is it?** Grafana visualizes metrics and logs across data sources. **Interview answer:** "A dashboard correlates traffic, latency, errors, and resource saturation." **Example:** Incident overview. **Use:** Operations. **Points:** Variables, panels, alerts. **Follow-ups:** Dashboard design.

## ELK Logging
**What is it?** Elasticsearch, Logstash, and Kibana aggregate and analyze logs. **Interview answer:** "Applications emit structured JSON logs with request IDs and Kibana is used for search." **Example:** Find failed payments. **Use:** Centralized logs. **Points:** Retention, cardinality, security. **Follow-ups:** Elastic, OpenSearch.

## Blue-Green Deployments
**What is it?** Blue-green keeps two environments and switches traffic after verification. **Interview answer:** "New green code is warmed and tested, then traffic moves and old blue remains for rollback." **Example:** API release. **Use:** Low-downtime deploy. **Points:** Database compatibility. **Follow-ups:** Canary.

## Auto Scaling
**What is it?** Auto scaling adds or removes capacity based on demand and policy. **Interview answer:** "I scale on CPU plus queue depth and keep a warm capacity floor." **Example:** Order workers scale during a sale. **Use:** Variable load. **Points:** Metrics, cooldown, limits. **Follow-ups:** Scale-to-zero.

## Secrets Management
**What is it?** Secrets are injected at runtime from a controlled store. **Interview answer:** "I keep database credentials out of repositories and rotate them without rebuilding images." **Example:** KMS or Vault credentials. **Use:** Production configuration. **Points:** RBAC, rotation, audit. **Follow-ups:** Environment variables.
