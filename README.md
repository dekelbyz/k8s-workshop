# K8s workshop

Welcome to the k8s workshop
in this workshop we will demonstrate a k8s cluster using minikube
we will create a live cluster with deployments, services, namespaces and much more fun stuff.
We will split the work by using branches. Every branch will represent the current
state of knowledge / progress we're at at the moment.

---
# Lesson7:
Now we can add our configMap (which is pretty much same as secret syntax)
and link our mongo-express deployment to it in order to read from it.
But first, of course, we will have to register it to our cluster
so lets run:

`kuebctl apply -f k8s/mongo-configmap.yaml`

now lets deploy our deployment to the cluster as well:

`kubectl apply -f k8s/mongo-express.yaml`

* if you did not alter your context to our namespace, add: `-n ws-namespace` at the end.


