# GCPServiceAccountwithRoles
This code creates a custom role with required minimal permissions and a service account consuming that role

Follow the steps below to create the Role:
Download the files, *_custom_role.* and put it in your gcloud editor

execute below query to 
gcloud deployment-manager deployments create customRoleForServiceAccount --config project_custom_role.yaml

Note : Before executing just confirm that you have enabled the Identity and Access Management (IAM) API & Cloud Deployment Manager V2 API

