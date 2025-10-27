import subprocess
from ..file_utils.file_ops import parse_yaml_file

def is_host_up(hostname: str) -> bool:
    """ Pings the given hostname to check if it is reachable. """
    print(f"  -- network_ops.is_host_up called for {hostname}")
    try:
        # Using '-c 1' for Unix/Linux and '-n 1' for Windows
        result= subprocess.run(["ping", "-n", "1", hostname],  
                                       check=True,
                                       capture_output=True,
                                       text=True,
                                       timeout=3)
        
        return result.returncode == 0

    except (subprocess.CalledProcessError, 
            subprocess.TimeoutExpired):
        return False
    

def check_hosts_from_config(config_path: str) -> bool:
    """ Checks if hosts listed in a YAML config file are up. """
    print(f"  -- network_ops.check_hosts_from_config called for {config_path}")
    config_data = parse_yaml_file(config_path)
    hosts = config_data.get("hosts", [])
    if not hosts:
        print("No hosts found in configuration.")
        return False
    
    return all(is_host_up(hostname) for hostname in hosts)
