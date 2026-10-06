from config import(
    FEATURES,
    MANDATORY_FEATURES
)
from git_manager import clone_repository

def display_features():

    print("\n================================")
    print("       Deployment Manager")
    print("================================\n")

    print("Available Features:\n")

    for key, feature in FEATURES.items():
        print(f"{key}. {feature['name']}")


def get_selection():

    while True:

        selection = input(
            "\nSelect features (example: 1,2): "
        )

        selected_keys = [
            item.strip()
            for item in selection.split(",")
        ]

        invalid = [
            key
            for key in selected_keys
            if key not in FEATURES
        ]

        if invalid:
            print(
                f"Invalid feature selection: {invalid}"
            )
            continue

        return selected_keys


def create_deployment_plan(selected_keys):

    plan = []

    for key, feature in MANDATORY_FEATURES.items():

        plan.append({
            "feature": feature["name"],
            "service": feature["service"],
            "repo": feature["repo"]
        })

    for key in selected_keys:

        feature = FEATURES[key]

        plan.append({
            "feature": feature["name"],
            "service": feature["service"],
            "profile": feature["profile"],
            "repo": feature["repo"]
        })

    return plan


def display_plan(plan):

    print("\n================================")
    print("       Deployment Plan")
    print("================================\n")

    for item in plan:

        print(f"Feature : {item['feature']}")
        print(f"Service : {item['service']}")
        print(f"Repo    : {item['repo']}")
        print("--------------------------------")

def download_repositories(plan):

    print("\n================================")
    print("       Getting Repositories")
    print("================================\n")

    for item in plan:

        clone_repository(
            item["repo"],
            item["service"]
        )
        