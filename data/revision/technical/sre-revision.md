# DevOps Advanced / SRE Revision

## GitOps
**What is it?** GitOps uses Git as the declarative source of infrastructure and application state. **Interview answer:** "A controller reconciles the cluster toward versioned Git manifests." **Example:** Argo CD deploy. **Use:** Auditable delivery. **Points:** Pull reconciliation, drift. **Follow-ups:** Push vs pull.

## ArgoCD
**What is it?** Argo CD continuously deploys Kubernetes resources declared in Git or Helm. **Interview answer:** "It detects drift and can sync or pause changes through policy." **Example:** Promote a new image digest. **Use:** GitOps. **Points:** App, sync, health. **Follow-ups:** Rollback.

## Docker Security
**What is it?** Docker security minimizes image, runtime, and registry risk. **Interview answer:** "I use minimal signed images, non-root users, read-only filesystems, and secrets injection." **Example:** Remove shell and set no privilege. **Use:** Container workloads. **Points:** Scanning, capabilities. **Follow-ups:** Runtime escape.

## Multi-stage Docker Builds
**What is it?** Multi-stage builds compile in one stage and copy only the artifact to a runtime stage. **Interview answer:** "It removes build tools and source from the final image." **Example:** Go or Python wheel build. **Use:** Smaller images. **Points:** Cache, final stage. **Follow-ups:** Distroless.

## Zero-Downtime Deployments
**What is it?** Zero-downtime deployment keeps requests available while replacing software. **Interview answer:** "I ensure readiness, backward-compatible schemas, rolling or blue-green traffic, and rollback." **Example:** API migration. **Use:** Production releases. **Points:** Healthcheck, draining. **Follow-ups:** Database migration.

## Infrastructure as Code Best Practices
**What is it?** IaC defines infrastructure reproducibly in reviewed versioned code. **Interview answer:** "I use modules, plans, locked state, separate environments, and no manual drift." **Example:** Terraform network stack. **Use:** Teams and cloud. **Points:** State, lint, drift. **Follow-ups:** State migration.

## SRE Basics
**What is it?** SRE applies software engineering to reliability through budgets and automation. **Interview answer:** "SRE defines user-facing objectives and balances feature work with error budgets." **Example:** 99.9% availability target. **Use:** Operational maturity. **Points:** TOIL, automation, incident review. **Follow-ups:** SRE vs DevOps.

## SLI
**What is it?** An SLI is a measured service indicator. **Interview answer:** "For an API, a good SLI is the percentage of valid requests faster than a threshold." **Example:** 95th-percentile latency. **Use:** Objective measurement. **Points:** Coverage, denominator. **Follow-ups:** SLI vs metric.

## SLO
**What is it?** An SLO is a target for an SLI over a time window. **Interview answer:** "We aim for 99.9% of successful requests under 300 ms each month." **Example:** Checkout availability. **Use:** Prioritizing reliability. **Points:** Window, target. **Follow-ups:** Error budget.

## SLA
**What is it?** An SLA is a contractual commitment that may include remedies. **Interview answer:** "An SLA specifies promised uptime and consequences; it should be less ambitious than internal SLOs." **Example:** 99.9% service credit. **Use:** Customer contracts. **Points:** Contract, measurement. **Follow-ups:** SLA vs SLO.
