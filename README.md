# GitOps-ArgoCD

In this project I implemented the following steps:
1. Installing a kubernetes cluster with 1 master and 1 workers, on AWS ec2 instances.
2. Throw Jenkins server, I created a CI pipeline that pulls a Dockerfile Iv'e created from Gitlab server( SCM ), and Build a Docker image
3. Pushing the Image to DockerHub
4. A successful execution of the CI pipeline triggers a CD pipeline that Reads a deployment.yml from another repository in Gitlab
5. Inserting the updated image into the deployment using environment variable
5. ArgoCD monitores the CD repository, and apply te changes to the workers
6. The NodePort Service allows access to the updated app

