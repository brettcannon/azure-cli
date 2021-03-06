# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.help_files import helps #pylint: disable=unused-import

#pylint: disable=line-too-long
helps['login'] = """
            examples:
                - name: Log in interactively.
                  text: >
                    az login
                - name: Log in with user name and password. This doesn't work with Microsoft accounts or accounts that have two-factor authentication enabled.
                  text: >
                    az login -u johndoe@contoso.com -p VerySecret
                - name: Log in with a service principal.
                  text: >
                    az login --service-principal -u http://azure-cli-2016-08-05-14-31-15 -p VerySecret --tenant contoso.onmicrosoft.com
            """

helps['account'] = """
    type: group
    short-summary: Manages stored and default subscriptions
"""

helps['account list-locations'] = """
    type: command
    short-summary: list supported regions of the current subscription
"""

helps['account show'] = """
    type: command
    short-summary: show details of the current subscription
"""

helps['account set'] = """
    type: command
    short-summary: Sets the active (default) subscription
"""

helps['account show'] = """
    type: command
    short-summary: Show the details of a subscription
    long-summary: If the subscription isn't specified, shows the details of the default subscription
"""
