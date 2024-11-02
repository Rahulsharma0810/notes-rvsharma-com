
### Choosing Platform For Kubernetes 

Although Ubuntu Minimal Server, Servers the purpose. However i do not want to give OS another fraction of compute, lets say i have 1 master + 4 nodes, each with ubuntu. Then there will be unnecessary compute, 4-10% depends .

Then i found another CNCF Backed Project called Talos Linux. it's metal ios only sized ~ 120MB and doesn't have other tools like ssh etc.

Think it as Managed Kubernetes.

#### Talos Linux on Proxmox


Downloaded ISO with below config.

Didn't enabled the secure boot, as it was asking to kernel flags which i am not sure about. #learn

#URL https://factory.talos.dev/?arch=amd64&board=undefined&cmdline-set=true&extensions=-&extensions=siderolabs%2Fqemu-guest-agent&platform=metal&target=metal&version=1.8.2

```
customization: 
    systemExtensions: 
        officialExtensions: 
            - siderolabs/qemu-guest-agent
```

1. Disable Secure Boot and start the VM.
2. Add IP via Interactive Serial Dashboard.1

Then Follow https://www.talos.dev/v1.8/talos-guides/install/virtualized-platforms/proxmox/


Static IPs to Control Panel and Worker Nodes

```yaml
#controlplane.yaml
network:
hostname: I1-1806-Talos-CP01
interfaces:
- interface: ens18 # The interface name.
addresses:
- 192.168.0.5/24
routes:
- network: 0.0.0.0/0 # The route's network.
gateway: 192.168.0.1 # The route's gateway.
dhcp: false
```

```worker.yaml
network:
hostname: I1-1806-Talos-Worker01
interfaces:
- interface: enp6s18 # The interface name.
addresses:
- 192.168.0.6/24
routes:
- network: 0.0.0.0/0 # The route's network.
gateway: 192.168.0.1 # The route's gateway.
dhcp: false
```

**Instruction Followed**

```shell
❯ talosctl gen config talos-proxmox-cluster https://$CONTROL_PLANE_IP:6443 --output-dir ../Talos-config --install-image factory.talos.dev/installer/ce4c980550dd2ab1b17bbf2b08801c7eb59418eafe8f279833297925d67c7515:v1.8.2 --force
```


For Cilium cluster.proxy.disabled = true and cluster.network.cni.name = none [Guide](https://www.talos.dev/v1.8/kubernetes-guides/network/deploying-cilium/)
  
```shell
❯ talosctl apply-config --insecure --nodes 192.168.0.5 --file ./controlplane.yaml

❯ talosctl apply-config --insecure --nodes 192.168.0.6 --file ./worker.yaml
```

```
❯ export TALOSCONFIG=./talosconfig
❯ talosctl config endpoint 192.168.0.5
❯ talosctl config node 192.168.0.5
❯ talosctl bootstrap
❯ talosctl kubeconfig .
❯ rm -rf ~/.kube/config
❯ cp kubeconfig ~/.kube/config
```

