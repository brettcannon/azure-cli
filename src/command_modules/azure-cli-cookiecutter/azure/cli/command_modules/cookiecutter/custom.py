# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import cookiecutter.main

import azure.cli.core._logging as _logging

logger = _logging.get_az_logger(__name__)

def generate(template_location):
    """Generate a project."""
    url = "/".join(["https://github.com", template_location])
    url += ".git"
    logger.debug("Generating a template from " + url)
    cookiecutter.main.cookiecutter(url)