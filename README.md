# GCPServiceAccountwithRoles
This code creates a custom role with required minimal permissions and a service account consuming that role

Follow the steps below to create the Role:

1. Download the files, * _custom_role. * and put it in your gcloud editor

2. execute below query to 

*gcloud deployment-manager deployments create customRoleForServiceAccount --config project_custom_role.yaml*

Note : Before executing just confirm that you have enabled the Identity and Access Management (IAM) API & Cloud Deployment Manager V2 API

3. Verify the Role created in IAM & Admin --> Roles in your GCP Console and copy the RoleName

4. Download the files service-accounts.py & service-accounts.yaml.

5. In service-accounts.py, Line# 19, change the RoleName in the file.

6. Excecute below command in your gcloud to create the service account.

*gcloud deployment-manager deployments create customRoleForServiceAccount --config service-accounts.yaml*

7. verify the service account created under IAM & Admin --> Service Accounts in your GCP Console and copy the email of your service-account

8. For creating the keys of your service account, run below command on gcloud

*gcloud iam service-accounts keys create ~/key.json  --iam-account <email  of your service account copied in previous step>
