# CUDA 12 & UBUNTU 22.04
FROM nvidia/cuda:12.8.0-cudnn-devel-ubuntu22.04

# RUN BASIC PACKAGE
RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    git wget curl nano && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

