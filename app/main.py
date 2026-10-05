from deploy import (
    display_features, 
    get_selection, 
    create_deployment_plan, 
    display_plan, 
    download_repositories
)
from compose_manager import deploy_services

def main():

    display_features()

    selected_keys = get_selection()

    plan = create_deployment_plan(selected_keys)
    
    print("\nDeployment plan created.")

    display_plan(plan)
    
    download_repositories(plan)
    
    deploy_services(plan)

    


if __name__ == "__main__":
    main()