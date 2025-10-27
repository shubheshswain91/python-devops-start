print("Main script starting")

from devops_utils import check_file_extension as check_file
import sys

print(sys.path)

filenames = ["config.yaml", "script.sh", "readit.go"]

for filename in filenames:
    print(f"Checking {filename}")
    print(f"Results: {check_file(filename)}")