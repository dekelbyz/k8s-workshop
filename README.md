# K8s workshop

Welcome to the k8s workshop
in this workshop we will demonstrate a k8s cluster using minikube
we will create a live cluster with deployments, services, namespaces and much more fun stuff.
We will split the work by using branches. Every branch will represent the current
state of knowledge / progress we're at at the moment.

---
# Lesson9:
Now we are going to do something different.
We are going to 

* create a simple 'hello-world' image
* Authenticate to docker 
* Push it to docker registry (dockerhub) 
* Create a deployment 
* Use the image we've pushed to the registry in our controller 

Lets create and push this image (after logging in to docker.io)
Follow the next steps: 

`docker login -u "myusername" -p "mypassword" docker.io`
`cd hello-world/`
`docker build -t ${your_docker_username}/hello-world .`
`docker push ${your_docker_username}/hello-world`





