# K8s workshop

Welcome to the k8s workshop
in this workshop we will demonstrate a k8s cluster using minikube
we will create a live cluster with deployments, services, namespaces and much more fun stuff.
We will split the work by using branches. Every branch will represent the current
state of knowledge / progress we're at at the moment.

---
# Lesson6:
Now that we have our mongo-db app up and running, lets try to interact with it using mongo-express.
We will add a new deployment to a file called `mongo-express.yaml`

"Mongo Express is a lightweight web-based administrative interface deployed to manage MongoDB databases interactively. It is authored using Node.js, Express and Bootstrap packages. " - helpnetsecurity.

Since the mongo-express configuration requires some of the credentials we already have in our secret,
we can simply address the right secret on our cluster, just like we did with the mongodb.

There is another variable tho, this variable should exist on the configMap.
So branch up to lesson-7 and lets see how we add a configMap component and how we address it


