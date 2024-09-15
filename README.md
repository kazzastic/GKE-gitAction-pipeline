Have you ever brought a bazuka to a street fight? This repository does exactly that, in order to send a simple email, it deploys to kubernetes. More or less, this is my hand's on practice for making a CI/CD pipeline using docker and kubernetes :D

### Google Managed Kubernetes Cluster 
- a simple autoscaled, fully managed by Google Cloud
- pipeline deploys to default `namespace`

### Google Artifcat Registry 
- The docker image is being published at Google Artifact

### Python Script Secrets
- The python secrets are being published from github secrets along with k8s deployment secrets

code deploys when merged with master branch
