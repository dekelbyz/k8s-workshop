# K8s workshop

Welcome to the k8s workshop
in this workshop we will demonstrate a k8s cluster using minikube
we will create a live cluster with deployments, services, namespaces and much more fun stuff.
We will split the work by using branches. Every branch will represent the current
state of knowledge / progress we're at at the moment.

---
# Lesson5:
In this lesson we will create a service and apply it to our cluster.
The service defined on the `mongo.yaml` file, below the deployment definition.
YAML gives us the ability to put 2 configuration inside one file by separating them using `---`
We could define our service somewhere else but it makes a lot of sense putting it along side the
deployment, because they linked to each other. They are besties <3 <3
Lets apply the new changes into our cluster:

`kubectl apply -f k8s/mongo.yaml`

* if you did not alter your context to our namespace, add: `-n ws-namespace` at the end.