# hello-k8s
Very simple hello world python Fastapi application.

1. Build docker image
    <pre><code>docker build -t hello-k8s . </pre></code>
2. Deploy to k8s
    <pre><code>kubectl apply -f Kubernetes/deployment.yaml </pre></code>
