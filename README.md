# Introduction to Vertex AI Pipelines with R 

## Environment Setup 

To run the example notebooks in this repository, you will need a GCP project with billing enabled. Each notebook contains additional required setup steps 

### Vertex AI Workbench Notebook

To create a notebook instance: 

1.  Navigate to [Vertex Workbench User Managed Notebooks](https://console.cloud.google.com/ai-platform/notebooks) and create a python notebook instance (or use the cloud shell command below)
    2.1.  At the top of the screen, click "NEW NOTEBOOK"  
    2.2.  Use the first option for a notebook "Python 3"  
    2.3.  For the Region, select the first option "us-central1"  
    2.4.  Click "Create"  
    ```sh
    gcloud notebooks instances create vertex-pipelines-r \
        --vm-image-project=deeplearning-platform-release \
        --vm-image-family=common-cpu-notebooks \
        --machine-type=n1-standard-8 \
        --location=us-central1-a 
    ```
3.  Once the notebook instance is created, clone this repository via the GUI or terminal: 
    ```sh
    git clone https://github.com/justinjm/vertex-ai-pipelines-r-model-intro
    ```

**Optional** You can also work from the [Cloud Shell Editor](https://cloud.google.com/shell/docs/editor-overview) and click the button below to clone and open this repository in your own Cloud Shell instance:  

[![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/justinjm/vertex-ai-pipelines-r-model-intro)


## Contents 

* [01-run-r-script](01-run-r-script)



## References 

* https://github.com/RajeshThallam/vertex-ai-labs
* https://github.com/jarokaz/vertex-ai-workshop/