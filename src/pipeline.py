from google.cloud import aiplatform as vertex

# import kfp
from kfp.v2 import dsl, compiler
from kfp.v2.dsl import (Artifact, Dataset, Input, InputPath, Model, Metrics, Output, OutputPath, component)
from google_cloud_pipeline_components import aiplatform as aip_components
# from google_cloud_pipeline_components.v1 import custom_job, dataset, endpoint, model
# from google_cloud_pipeline_components.types import artifact_types

PIPELINE_ROOT = f'gs:// '
PROJECT_ID = ' '

@dsl.pipeline(name = 'pipe-r-print-test', pipeline_root = PIPELINE_ROOT)
def r_pipeline():
    print_task = (aip_components.CustomContainerTrainingJobRunOp(  
        project = ' ',
        location = 'us-central1',
        display_name = "R print test",
        container_uri = 'us-central1-docker.pkg.dev/XXXX/docker-repo-XXX/print-r:latest',
        command = ["RScript", "print.R"],
        staging_bucket = PIPELINE_ROOT
    )
    .set_display_name("Print Test")
    .set_caching_options(False)
    )
    
compiler.Compiler().compile(pipeline_func = r_pipeline, package_path = 'pipe-r-print-test.json')

#-------------------#
# Run Test Pipeline #
#-------------------#

vertex.init(project=PROJECT_ID, staging_bucket=PIPELINE_ROOT)

job = vertex.PipelineJob(
    display_name = "r_print_test",
    template_path = 'pipe-r-print-test.json',
    pipeline_root = PIPELINE_ROOT,
    # parameter_values = pipeline_parms,
    enable_caching = False
)

job.submit()