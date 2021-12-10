# App Container Setup with Azure CLI

```sh
az group create --resource-group dohoney-fastapi-rg  --location westus

az acr create --resource-group  dohoney-fastapi-rg --name dohoneyfastapiacr --sku Standard --location westus   

az acr build -g dohoney-fastapi-rg  -t myfastapi:v1 -r dohoneyfastapiacr .

#  Enable admin on acr
az acr update -n dohoneyfastapiacr --admin-enabled true

az acr credential show --name dohoneyfastapiacr

az acr login -n dohoneyfastapiacr

#BEWARE -- ACA is only in preview, so all regions are not spun up as of yet.
RESOURCE_GROUP="dohoney-fastapi-rg"
LOCATION="eastus"
LOG_ANALYTICS_WORKSPACE="my-container-apps-logs"
CONTAINERAPPS_ENVIRONMENT="fastapi-environment"


az monitor log-analytics workspace create \
  --resource-group $RESOURCE_GROUP \
  --workspace-name $LOG_ANALYTICS_WORKSPACE

LOG_ANALYTICS_WORKSPACE_CLIENT_ID=`az monitor log-analytics workspace show --query customerId -g $RESOURCE_GROUP -n $LOG_ANALYTICS_WORKSPACE --out tsv`
LOG_ANALYTICS_WORKSPACE_CLIENT_SECRET=`az monitor log-analytics workspace get-shared-keys --query primarySharedKey -g $RESOURCE_GROUP -n $LOG_ANALYTICS_WORKSPACE --out tsv`

az extension add \
  --source https://workerappscliextension.blob.core.windows.net/azure-cli-extension/containerapp-0.2.0-py2.py3-none-any.whl

az containerapp env create \
  --name $CONTAINERAPPS_ENVIRONMENT \
  --resource-group $RESOURCE_GROUP \
  --logs-workspace-id $LOG_ANALYTICS_WORKSPACE_CLIENT_ID \
  --logs-workspace-key $LOG_ANALYTICS_WORKSPACE_CLIENT_SECRET \
  --location eastus

  az containerapp create \
  --name fastapi-container-app \
  --resource-group $RESOURCE_GROUP \
  --environment $CONTAINERAPPS_ENVIRONMENT \
  --image dohoneyfastapiacr.azurecr.io/myfastapi:v1 \
  --target-port 80 \
  --ingress 'external' \
  --query configuration.ingress.fqdn
  #
  # Credentials can be obtained with the following CLI command
  # az acr credential show --name dohoneyfastapiacr
  #
  --registry-username  $REGISTRY_USERNAME
  --registry-password $REGISTRY_PASSWORD
  --debug


```

## Great Articles 
 Using Azure Bicep - https://www.thorsten-hans.com/how-to-deploy-azure-container-apps-with-bicep
 
 Using ACA Scaling - https://docs.microsoft.com/en-us/azure/container-apps/scale-app
 
 Decompile ARM to Bicep - https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/decompile?tabs=azure-cli
