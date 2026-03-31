# DevSecOps_Gorilla_MockTest.md

Timed practice: **30–35 minutes**. 40 questions, 4 options each.

Write your answers and self-check using the inline `Answer:` after each question.

---

## Mock Test (40 MCQs)

1) SAST is best described as:  
A) Testing a running app from outside  
B) Scanning source code for vulnerabilities  
C) Scanning container runtime syscalls  
D) Monitoring production logs  
Answer: B

2) SCA primarily identifies:  
A) SQL injection in endpoints  
B) Vulnerable third‑party dependencies/licenses  
C) Misconfigured TLS certificates  
D) Broken authentication flows  
Answer: B

3) DAST requires:  
A) Only source code  
B) A running application endpoint  
C) Only SBOM  
D) Only git history  
Answer: B

4) Best practice to avoid long‑lived cloud access keys in CI is:  
A) Store keys in repo secrets permanently  
B) Encrypt keys in pipeline YAML  
C) Use OIDC to obtain short‑lived credentials  
D) Share one admin key across teams  
Answer: C

5) The biggest risk of using Docker image tag `latest` in production is:  
A) Slower pull time  
B) Non‑reproducible builds (tag changes over time)  
C) Larger image size  
D) It blocks vulnerability scanning  
Answer: B

6) Most secure default for containers is to:  
A) Run as root  
B) Run as non‑root user  
C) Mount Docker socket  
D) Use privileged mode  
Answer: B

7) Multi-stage Docker builds mainly help by:  
A) Making images larger  
B) Removing build tools from runtime image  
C) Enabling host networking  
D) Disabling TLS checks  
Answer: B

8) Image signing mainly provides:  
A) Faster startup time  
B) Integrity/provenance verification  
C) Better compression  
D) Automatic secret rotation  
Answer: B

9) SBOM stands for and is used for:  
A) System Backup Operations Manual; backups  
B) Software Bill of Materials; component inventory  
C) Secure Build Output Metadata; CPU tuning  
D) Security Baseline of Modules; firewall config  
Answer: B

10) “Least privilege” means:  
A) Everyone gets admin to avoid outages  
B) Give the minimum permissions needed  
C) Use one shared service account  
D) Disable access logs  
Answer: B

11) In Kubernetes, RBAC controls:  
A) Pod-to-pod encryption  
B) Who can do what to which resources  
C) Container image size  
D) Node autoscaling behavior  
Answer: B

12) NetworkPolicies are used to:  
A) Store secrets securely  
B) Control allowed network traffic between pods/services  
C) Rotate certificates  
D) Set CPU limits  
Answer: B

13) Best approach to handle secrets for CI/CD deployments is:  
A) Commit `.env` to git  
B) Use a secrets manager + short‑lived creds where possible  
C) Print secrets to logs for debugging  
D) Hardcode secrets in Dockerfile  
Answer: B

14) If a secret is committed to git, the FIRST step is:  
A) Delete the commit locally  
B) Rotate/revoke the secret immediately  
C) Ask the team if it’s okay  
D) Make the repo private  
Answer: B

15) “Shift-left security” means:  
A) Move security checks earlier in the SDLC  
B) Only scan production  
C) Disable checks during CI  
D) Do security after release  
Answer: A

16) Which is a strong mitigation against dependency confusion?  
A) Allow any public packages  
B) Use private registries/allowlists and pin versions  
C) Disable lockfiles  
D) Use `latest` versions  
Answer: B

17) A common CI/CD control for production releases is:  
A) Disable approvals  
B) Manual approval gates + restricted deploy permissions  
C) Allow everyone to deploy anytime  
D) Commit directly to main  
Answer: B

18) Best practice for artifact handling is:  
A) Rebuild in each environment  
B) Build once, promote the same immutable artifact  
C) Build in production only  
D) Copy files manually to servers  
Answer: B

19) IaC scanning is used to catch:  
A) Code formatting issues only  
B) Misconfigurations (public buckets, open SGs, weak policies)  
C) User typos in documentation  
D) CPU performance bottlenecks  
Answer: B

20) TLS is primarily for:  
A) Database indexing  
B) Encryption in transit + endpoint identity  
C) Encryption at rest only  
D) Caching  
Answer: B

21) OWASP Top 10 is:  
A) A list of Linux kernel vulnerabilities only  
B) Common web app security risks  
C) A container runtime  
D) A cloud IAM policy set  
Answer: B

22) A secure K8s pod configuration should typically:  
A) Allow privilege escalation  
B) Run as non-root and drop capabilities  
C) Mount host filesystem by default  
D) Use hostNetwork for all pods  
Answer: B

23) “Encryption at rest” for K8s secrets means:  
A) TLS for API server only  
B) Encrypting etcd stored secret data  
C) Encrypting container stdout logs  
D) Encrypting docker image layers only  
Answer: B

24) The most reliable way to know what code produced an image is:  
A) Ask the developer  
B) Use git SHA labels + build provenance/attestation + SBOM  
C) Use image size  
D) Use container name  
Answer: B

25) A canary deployment helps by:  
A) Deploying to all users at once  
B) Gradually shifting traffic to new version with monitoring  
C) Disabling monitoring  
D) Preventing all rollbacks  
Answer: B

26) Best immediate response to active exploitation in production is:  
A) Wait for the next sprint  
B) Contain impact (block, isolate, disable) then rotate creds  
C) Publish logs publicly  
D) Ignore if error rate is low  
Answer: B

27) Secret scanning should run:  
A) Only after release  
B) In CI and ideally pre-commit as well  
C) Only on developer laptops  
D) Only yearly audits  
Answer: B

28) Logging sensitive data (tokens/PII) is:  
A) Fine in debug mode  
B) A security risk; avoid and mask/redact  
C) Required for performance  
D) Only a compliance issue, not security  
Answer: B

29) A common reason CI works locally but fails in pipeline is:  
A) Deterministic builds  
B) Dependency/version mismatch or missing env vars  
C) Too much documentation  
D) Too many tests  
Answer: B

30) Container vulnerability scanning should be done:  
A) Only after deployment  
B) During CI before pushing to prod, and continuously in registry  
C) Only on weekends  
D) Only for base images  
Answer: B

31) The best way to reduce blast radius is:  
A) One shared admin account  
B) Segmentation + least privilege + separate environments  
C) Disable alerts  
D) Put everything in one VPC/subnet  
Answer: B

32) A “break-glass” account should be:  
A) Used daily  
B) Highly controlled, audited, and used only for emergencies  
C) Shared in team chat  
D) Password set to never expire  
Answer: B

33) Which is a strong control to prevent unauthorized pipeline changes?  
A) Allow anyone to edit pipeline YAML  
B) Protect branches + require reviews + CODEOWNERS  
C) Disable audit logs  
D) Disable PR checks  
Answer: B

34) For Kubernetes admission control/policy, a common approach is:  
A) Disable RBAC  
B) Use policy engines (conceptually like OPA/Gatekeeper/Kyverno)  
C) Allow privileged pods everywhere  
D) Run everything in default namespace  
Answer: B

35) The goal of threat modeling is to:  
A) Replace testing  
B) Identify threats early and decide mitigations  
C) Remove need for monitoring  
D) Eliminate all risk  
Answer: B

36) Which choice best describes “defense in depth”?  
A) One strong control only  
B) Multiple layered controls across stages/components  
C) No controls in CI  
D) Only perimeter firewall  
Answer: B

37) A strong mitigation for SSRF is:  
A) Enable debug logs  
B) Restrict egress + URL allowlists + metadata service protections  
C) Disable TLS  
D) Increase CPU  
Answer: B

38) A common secure default in cloud storage is:  
A) Public read for convenience  
B) Private by default, explicit access grants  
C) Anonymous write allowed  
D) No encryption  
Answer: B

39) “Principle of separation of duties” means:  
A) Developers approve their own production deploys  
B) Different roles for build vs approve vs deploy  
C) Everyone shares credentials  
D) One person does everything  
Answer: B

40) Best metric to alert on for an API security incident (first signals) is often:  
A) Page view count  
B) Error rate spikes + auth failures + unusual traffic patterns  
C) CPU temperature only  
D) Code coverage  
Answer: B

## DevSecOps_Gorilla_MockTest (Additional MCQs, answers inline)

41) What is the primary security purpose of protected branches in a git workflow?
A) Increase repository size
B) Prevent unauthorized changes by requiring reviews/approvals
C) Remove the need for CI
D) Speed up merges by skipping checks
Answer: B

42) Which is the best control to reduce the chance of deploying a tampered artifact?
A) Rebuild during deployment
B) Build once and deploy the exact immutable artifact (with signing/provenance)
C) Use mutable tags only
D) Allow manual artifact replacement
Answer: B

43) In dependency scanning, why is a lockfile useful?
A) It forces deterministic dependency versions so builds are reproducible
B) It encrypts dependencies
C) It prevents SCA from running
D) It removes the need for SAST
Answer: A

44) Which is the best practice for container users/privileges?
A) Run as root to avoid permission issues
B) Run as non-root and drop capabilities where possible
C) Enable privileged mode for simplicity
D) Mount host `/` by default
Answer: B

45) A CI pipeline runs on PRs from forks. What is the safest approach?
A) Give forked PRs access to production secrets
B) Use restricted permissions and no access to sensitive secrets for untrusted code
C) Disable all scans to reduce time
D) Run everything with cluster-admin credentials
Answer: B

46) What does “SBOM” help you do operationally?
A) Determine who wrote each commit
B) Identify all included components so you can assess CVEs/licenses faster
C) Replace runtime monitoring
D) Automatically fix vulnerabilities without patching
Answer: B

47) If your container registry supports it, why is image signing useful?
A) It improves CPU scheduling
B) It provides integrity verification and helps prevent unauthorized image use
C) It increases image compression
D) It disables TLS requirement
Answer: B

48) Which best describes role-based access control (RBAC)?
A) Controlling access based on roles/permissions
B) Encrypting data at rest
C) Scaling workloads automatically
D) Rotating certificates
Answer: A

49) NetworkPolicies in Kubernetes mainly protect against:
A) CPU spikes
B) Unwanted network traffic between pods/services (lateral movement)
C) Docker layer caching
D) Slow API endpoints only
Answer: B

50) What should you typically prefer for Kubernetes secrets management?
A) Putting secrets in ConfigMaps committed to git
B) External secret managers / encrypted secrets with tight RBAC access
C) Storing secrets in plain text environment variables in code
D) Disabling RBAC on secrets
Answer: B

51) A developer proposes “just disable security gates for this one PR.” Best response?
A) Approve and ignore because it’s one PR
B) Explain risk and propose safer alternatives (fix issues, keep gates for prod, possibly temporary scoped exceptions)
C) Disable monitoring to reduce noise
D) Only enable gates after deployment
Answer: B

52) What is threat modeling’s main value for an engineering team?
A) It replaces testing completely
B) It helps identify threats early and decide mitigations before implementing
C) It guarantees 0 vulnerabilities
D) It only matters for pentesting teams
Answer: B

53) If you suspect an active attack, what is a typical first operational action?
A) Continue rollout and wait for next monitoring report
B) Contain impact by isolating/pausing affected services, then revoke/rotate impacted credentials
C) Post the incident on social media
D) Remove logs to hide evidence
Answer: B

54) Which approach best prevents SSRF from reaching internal metadata/services?
A) Allow all egress to any destination
B) Restrict egress and enforce URL allowlists; protect metadata endpoints
C) Disable authentication
D) Increase max request size
Answer: B

55) What does “least privilege” imply in IAM/RBAC design?
A) Give broad admin roles to reduce management
B) Grant only permissions required for the specific job/task
C) Use shared credentials for easier audit
D) Avoid separating environments
Answer: B

56) Separation of duties in DevSecOps is mainly about:
A) One person does everything
B) Separating responsibilities (build vs approve vs deploy) to reduce insider risk
C) More documentation only
D) Disabling audit logs
Answer: B

57) Which is a good example of “shift-left” security?
A) Run vulnerability scans only once in production
B) Run SAST/SCA/secret/IaC checks in CI before merge/release
C) Remove checks from CI to avoid delays
D) Scan only after incidents
Answer: B

58) Which is the best explanation of CI “policy-as-code” gates?
A) Policies are written in YAML but not enforced
B) Security/compliance rules are encoded and enforced automatically in pipelines
C) Policies exist only in documentation
D) Policies are applied manually by developers
Answer: B

59) TLS primarily provides:
A) Encryption in transit and endpoint identity/authentication
B) Faster DB queries
C) Better code formatting
D) Automatic vulnerability patching
Answer: A

60) A pipeline uses environment variables but one is printed to logs. What is the risk?
A) No risk; logs are never accessible
B) Secrets/PII can leak and may be captured/retained; you should redact/mask and rotate if exposed
C) Environment variables can’t be sensitive
D) It improves security
Answer: B

61) Which is the best practice for incident documentation?
A) Only write summary after months
B) Keep factual timeline + root cause + corrective actions and preventive controls
C) Share sensitive tokens publicly
D) Remove evidence
Answer: B

62) For K8s hardening, what does “restricted” Pod Security aim to prevent?
A) Privileged pods and unsafe host mounts
B) High availability
C) DNS resolution
D) NetworkPolicies
Answer: A

63) When building Docker images, what does “multi-stage” most directly help with?
A) It increases the runtime attack surface by keeping build tools
B) It allows copying only what you need into the final image (smaller, fewer tools)
C) It disables dependency pinning
D) It makes builds non-deterministic
Answer: B

64) What is a good indicator that an offline metric gate might not protect production?
A) Offline evaluation is always perfect
B) Data distribution changed (drift), preprocessing mismatch, or feature schema differences
C) Latency improved
D) More logs were added
Answer: B

65) What’s the best way to implement rollback safety for a bad deploy?
A) Redeploy a different unrelated service version
B) Roll back to the last known-good artifact/config with controlled rollout and monitoring
C) Delete previous versions to avoid confusion
D) Disable alerts during rollback
Answer: B

