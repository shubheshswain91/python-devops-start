print("Main script starting")

from devops_utils import check_file_extension as check_file, is_host_up, check_hosts_from_config
import sys

print(sys.path)

filenames = ["config.yaml", "script.sh", "readit.go"]

for filename in filenames:
    print(f"Checking {filename}")
    print(f"Results: {check_file(filename)}")

print(f"Is host 'localhost' up? {is_host_up('localhost')}")   
print(f"Is host 'google.com' up? {is_host_up('google.com')}") 
print(f"Is host 'nonexistent.domain' up? {is_host_up('nonexistent.domain')}")

print(f"\n Are all hosts from server_config.yaml up? {check_hosts_from_config("servers_config.yaml")}")