import subprocess
from pathlib import Path


WORKSPACE = Path("/deployment-manager/deployment-workspace")

def clone_repository(repo_url, service_name):

    target_path = WORKSPACE / service_name

    if target_path.exists():
        print(f"{service_name}: repository exists.")
        print(f"{service_name}: pulling latest changes...")
        
        subprocess.run(
            [
                "git",
                "config",
                "--global",
                "--add",
                "safe.directory",
                str(target_path)
            ],
            check=True
        )


        subprocess.run(
            ["git", "-C", str(target_path), "pull"],
            check=True
        )

        print(f"{service_name}: update completed.")

    else:
        print(f"{service_name}: cloning repository...")

        subprocess.run(
            [
                "git",
                "clone",
                repo_url,
                str(target_path)
            ],
            check=True
        )

        print(f"{service_name}: clone completed")

    return target_path