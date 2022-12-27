# K8s workshop

Welcome to the k8s workshop
in this workshop we will demonstrate a k8s cluster using minikube
we will create a live cluster with deployments, services, namespaces and much more fun stuff.
We will split the work by using branches. Every branch will represent the current
state of knowledge / progress we're at at the moment.

---
# Lesson3:
in this lesson we will modify a little bit our `mongo.yaml` file.
First, we will go to https://hub.docker.com/_/mongo and learn what kind of 
variables/other crucial information we need in order to use this image properly properly.

Then, we will add those environment variables in the deployment configuration.

We will also expose a port for the container.

We do not have anything to test / run at this point because our configuration files are currently broken.