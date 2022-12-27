# K8s workshop

Welcome to the k8s workshop
in this workshop we will demonstrate a k8s cluster using minikube
we will create a live cluster with deployments, services, namespaces and much more fun stuff.
We will split the work by using branches. Every branch will represent the current
state of knowledge / progress we're at at the moment.

---
# Lesson1:
in this lesson all we will do is set up a namespace, which will allow us to 
seperate all our future resources and put them in one place instead of 
installing them on our global, default namespace.

```kubectl apply -f ws-namespace.yaml```

lets use kubens in order to switch the default namespace (provided by k8s) to the one we just created.
that way we won't have to specify on which namespace we want to create our resources every time.

```kubens ws-namespace```