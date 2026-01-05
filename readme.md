# webapp-ci

Simple Flask web app project to demonstrate Docker, Kubernetes and CI/CD practices.

The [workflow](https://github.com/saytricky/webapp-ci/actions) shows how image is built and tagged using Docker, and pushed to an AWS ECR repository before deployment to an AWS EKS cluster.

Kubernetes manifests are in `kube/`.