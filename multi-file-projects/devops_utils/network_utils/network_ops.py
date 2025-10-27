import subprocess

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