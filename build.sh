#!/bin/bash

# Update package list and install dependencies
apt-get update && apt-get install -y ocrmypdf
apt-get install tesseract-ocr-nor