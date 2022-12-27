# K8s workshop

Welcome to the k8s workshop
in this workshop we will demonstrate a k8s cluster using minikube
we will create a live cluster with deployments, services, namespaces and much more fun stuff.
We will split the work by using branches. Every branch will represent the current
state of knowledge / progress we're at at the moment.

---
# Lesson2:
in this lesson we will create a mongo-db deployment.
We have the `mongo.yaml` configuration file and image from docker registry.
run:
`kubectl apply -f mongo.yaml`

* if you did not alter your context to our namespace, add: `-n ws-namespace` at the end.