on:
  push:
    branches: [ "main" ]
  workflow_dispatch:

env:
  AZURE_WEBAPP_NAME: HPC    # set this to your application's name
  AZURE_WEBAPP_PACKAGE_PATH: 'https://github.com/arghyaroy2/AI-Use-Cases'      # set this to the path to your web app project, defaults to the repository root
  NODE_VERSION: '20.x'                # set this to the node version to use

permissions:
  contents: read