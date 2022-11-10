#!/usr/bin/env Rscript
# inputs
args <- commandArgs(trailingOnly = TRUE)
project_id <- args[1]
region <- args[2]
gcs_uri_in <- args[3]
gcs_uri_out <- args[4]

cat("project_id: ", project_id)
cat("region: ", region)
cat("gcs_uri_in: ", gcs_uri_in)
cat("gcs_uri_out: ", gcs_uri_out)

# printing test
print("This is printed using the print function")

message("This is printed using the message function")

cat("This is printed using the cat function")

write("This is printed using the write function", stdout())

# view environment vars
Sys.getenv()
