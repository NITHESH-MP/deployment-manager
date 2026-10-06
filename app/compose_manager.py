import subprocess


COMPOSE_FILE = "/deployment-manager/compose.yml"

def deploy_services(plan):

    profiles = [
        item["profile"]
        for item in plan
        if "profile" in item
    ]

    # Remove previous deployment
    down_command = [
        "docker",
        "compose",
        "-f",
        COMPOSE_FILE,
        "--profile",
        "machine",
        "--profile",
        "maintenance",
        "down"
    ]

    print("\nRemoving previous deployment...")

    subprocess.run(
        down_command,
        check=True
    )

    # Start selected services
    up_command = [
        "docker",
        "compose",
        "-f",
        COMPOSE_FILE
    ]

    for profile in profiles:
        up_command.extend([
            "--profile",
            profile
        ])

    up_command.extend([
        "up",
        "-d",
        "--build"
    ])

    print("\nStarting selected services...")
    print("Command:", " ".join(up_command))

    subprocess.run(
        up_command,
        check=True
    )

    print("\nDeployment completed.")