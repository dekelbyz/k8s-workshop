# K8s workshop

Welcome to the k8s workshop
in this workshop we will demonstrate a k8s cluster using minikube
we will create a live cluster with deployments, services, namespaces and much more fun stuff.
We will split the work by using branches. Every branch will represent the current
state of knowledge / progress we're at at the moment.

---
# Lesson4:
In this lesson, we will add the secret component and attach our deployment to it.
It will allow us to use an external configuration and by that we will not have to 
restart our system with every change we make.
and this information is secret and cannot be accessed from outside the cluster so 
its very secure.

run the following command in order to apply our new secret config into our cluster:
`kubectl apply -f k8s/secret.yaml` 

Now lets re-deploy our deployment with our new changes:
`kubectl apply -f k8s/mongo.yaml` 

* if you did not alter your context to our namespace, add: `-n ws-namespace` at the end.