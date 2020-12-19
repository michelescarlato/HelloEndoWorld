provider "kubernetes" {
  config_context_cluster   = "minikube"
  load_config_file = "false"
  host = "https://121.179.158.56:8443"
  client_certificate     = "${file("/root/.minikube/client.crt")}"
  client_key             = "${file("/root/.minikube/client.key")}"
  cluster_ca_certificate = "${file("/root/.minikube/ca.crt")}"
}
resource "kubernetes_namespace" "minikube-namespace" {
  metadata {
        name = "my-first-terraform-namespace"
  }
}
