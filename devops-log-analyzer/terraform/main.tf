terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_network" "log_network" {

  name = "log-analyzer-network"
}

resource "docker_container" "log_analyzer" {

  name  = "log-analyzer"
  image = "log-analyzer:latest"

  networks_advanced {
    name = docker_network.log_network.name
  }
}