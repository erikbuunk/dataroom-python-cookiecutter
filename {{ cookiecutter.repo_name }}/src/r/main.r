# Example Script for R

# retrievee commandline argument for setting the working directory
args = commandArgs(trailingOnly=TRUE)
if (length(args)>0) {
    setwd(args[1])
}

# Add code