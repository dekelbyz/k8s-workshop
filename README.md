# K8s workshop

Welcome to the k8s workshop
in this workshop we will demonstrate a k8s cluster using minikube
we will create a live cluster with deployments, services, namespaces and much more fun stuff.
We will split the work by using branches. Every branch will represent the current
state of knowledge / progress we're at at the moment.

---
# Lesson11:
Now we are going to do something different.
We are going to 

* create a simple 'hello-world' image
* Authenticate to docker 
* Push it to docker registry (dockerhub) 
* Create a deployment 
* Use the image we've pushed to the registry in our controller 

Now that our image is in our registry - we create a deployment 
and use that image (we can use the same namespace - ws-namespace)
We can now apply that deployment and add it to the cluster with the following command:

`kubectl apply -f hello-world.yaml`

Now, lets get the pod's name in order to check its logs:

`kubectl get pods`

`kubectl logs <pod-name>`







