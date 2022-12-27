# K8s workshop

Welcome to the k8s workshop
in this workshop we will demonstrate a k8s cluster using minikube
we will create a live cluster with deployments, services, namespaces and much more fun stuff.
We will split the work by using branches. Every branch will represent the current
state of knowledge / progress we're at at the moment.

---
# Lesson8:
Now that we mongo-express up and running, lets access it from the browser.
In order to do that, we need to add an external service which will allow addressing 
the cluster from outside of it.

We added the external service to the same file of the deployment, as we did with mongodb configuration file.
Lets apply this to our cluster by running:
`kubectl apply -f k8s/mongo-express.yaml` 
* if you did not alter your context to our namespace, add: `-n ws-namespace` at the end.


Now, lets help minikube give us an external ip address for our external service we've created.
`minikube service mongo-express-service -n ws-namespace`





