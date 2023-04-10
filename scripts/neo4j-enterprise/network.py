def generate_config(context):
    region = 'us-east4'

    network_name = 'fury'
    subnet_name = 'da-neo4j'

    network_ref = '$(ref.{}.selfLink)'.format(network_name)
    subnet_ref = '$(ref.{}.selfLink)'.format(subnet_name)
    subnet_cidr = '10.87.96.0/20'

    network = {
        'name': network_name,
        'type': 'compute.v1.network',
    }
    subnet = {
        'name': subnet_name,
        'type': 'compute.v1.subnetwork',
        'properties': {
            'region': region,
            'network': 'projects/shared-vpc-224614/global/networks/fury'
        }
    }
    config = {'resources': [], 'outputs': []}
    config['resources'].append(network)
    config['resources'].append(subnet)

    config['outputs'].append({
        'name': 'networkRef',
        'value': network_ref
    })
    config['outputs'].append({
        'name': 'subnetRef',
        'value': subnet_ref
    })
    config['outputs'].append({
        'name': 'subnetCidr',
        'value': subnet_cidr
    })
    return config