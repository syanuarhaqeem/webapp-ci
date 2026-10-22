# webapp-ci

Simple Flask web app project to demonstrate Docker, Kubernetes on EKS and CI/CD practices.

The [workflow file](https://github.com/syanuarhaqeem/webapp-ci/blob/main/.github/workflows/deploy.yaml) shows how image is built and tagged using Docker, and pushed to an AWS ECR repository before deployment to an AWS EKS cluster.

## Deployment Workflow
The GitHub Actions workflow is triggered when a tag matching "v*" is pushed.

1. Check out the source code and grabs image tag.
2. Authenticate to AWS using GitHub Actions OIDC and AWS IAM role.
3. Build, tag image, then pushes it to Amazon ECR.
4. Configure kubectl to the EKS cluster and verify cluster connectivity.
5. Apply the Kubernetes manifests and update the Deployment to use the tagged image.

## Kubernetes
Kubernetes manifests are in `kube/`. The project also includes PostgreSQL and basic alerting rules. For production use, PostgreSQL should use persistent storage like StatefulSet with persistent volumes.