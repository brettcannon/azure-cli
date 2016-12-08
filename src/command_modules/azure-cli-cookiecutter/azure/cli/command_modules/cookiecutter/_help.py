# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.help_files import helps #pylint: disable=unused-import

#pylint: disable=line-too-long

helps['cookiecutter'] = """
    type: group
    short-summary: Manages Cookiecutter templates
"""

helps['component generate'] = """
    type: command
    short-summary: Run the specified Cookiecutter template
"""
