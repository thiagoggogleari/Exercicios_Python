import ipaddress

def listar_ips_subrede(subrede):
    rede = ipaddress.ip_network(subrede,strict=False)
    return list(rede.hosts())

subrede = "192.168.0.1/24"
ips = listar_ips_subrede(subrede)

print(f"Todos os IPs da sub-rede {subrede}:")

for ip in ips:
    print(ip)
