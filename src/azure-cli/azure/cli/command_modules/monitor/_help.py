# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import
# pylint: disable=line-too-long, too-many-lines

helps['monitor'] = """
type: group
short-summary: Manage the Azure Monitor Service.
"""

helps['monitor action-group'] = """
type: group
short-summary: Manage action groups
"""

helps['monitor action-group wait'] = """
type: command
short-summary: Place the CLI in a waiting state.
"""

helps['monitor activity-log'] = """
type: group
short-summary: Manage activity logs.
"""

helps['monitor activity-log alert'] = """
type: group
short-summary: Manage activity log alert rules.
"""

helps['monitor activity-log alert action-group'] = """
type: group
short-summary: Manage action groups for activity log alert rules.
"""

helps['monitor activity-log alert action-group add'] = """
type: command
short-summary: Add action groups to this activity log alert rule. It can also be used to overwrite existing webhook properties of particular action groups.
parameters:
  - name: --name -n
    short-summary: Name of the activity log alert rule.
  - name: --action-group -a
    short-summary: The names or the resource ids of the action groups to be added.
  - name: --reset
    short-summary: Remove all the existing action groups before add new conditions.
  - name: --webhook-properties -w
    short-summary: >
        Space-separated webhook properties in 'key[=value]' format. These properties will be associated with
        the action groups added in this command.
    long-summary: >
        For any webhook receiver in these action group, these data are appended to the webhook payload.
        To attach different webhook properties to different action groups, add the action groups in separate update-action commands.
  - name: --strict
    short-summary: Fails the command if an action group to be added will change existing webhook properties.
examples:
  - name: Add an action group and specify webhook properties.
    text: |
        az monitor activity-log alert action-group add -n {AlertName} -g {ResourceGroup} \\
          --action /subscriptions/{SubID}/resourceGroups/{ResourceGroup}/providers/microsoft.insights/actionGroups/{ActionGroup} \\
          --webhook-properties usage=test owner=jane
  - name: Overwite an existing action group's webhook properties.
    text: |
        az monitor activity-log alert action-group add -n {AlertName} -g {ResourceGroup} \\
          -a /subscriptions/{SubID}/resourceGroups/{ResourceGroup}/providers/microsoft.insights/actionGroups/{ActionGroup} \\
          --webhook-properties usage=test owner=john
  - name: Remove webhook properties from an existing action group.
    text: |
        az monitor activity-log alert action-group add -n {AlertName} -g {ResourceGroup} \\
          -a /subscriptions/{SubID}/resourceGroups/{ResourceGroup}/providers/microsoft.insights/actionGroups/{ActionGroup}
  - name: Add new action groups but prevent the command from accidently overwrite existing webhook properties
    text: |
        az monitor activity-log alert action-group add -n {AlertName} -g {ResourceGroup} --strict \\
          --action-group {ResourceIDList}
"""

helps['monitor activity-log alert action-group remove'] = """
type: command
short-summary: Remove action groups from this activity log alert rule.
parameters:
  - name: --name -n
    short-summary: Name of the activity log alert rule.
  - name: --action-group -a
    short-summary: The names or the resource ids of the action groups to be removed.
"""

helps['monitor activity-log alert create'] = """
type: command
short-summary: Create a default activity log alert rule.
long-summary: This command will create a default activity log with one condition which compares if the activities logs 'category' field equals to 'ServiceHealth'. The newly created activity log alert does not have any action groups attached to it.
parameters:
  - name: --name -n
    short-summary: Name of the activity log alert rule.
  - name: --scope -s
    short-summary: A list of strings that will be used as prefixes.
    long-summary: >
        The alert rule will only apply to activity logs with resourceIDs that fall under one of these prefixes.
        If not provided, the path to the resource group will be used.
  - name: --disable
    short-summary: Disable the activity log alert rule after it is created.
  - name: --description
    short-summary: A description of this activity log alert rule.
  - name: --condition -c
    short-summary: The condition that will cause the alert rule to activate. The format is FIELD=VALUE[ and FIELD=VALUE...].
    long-summary: >
        The possible values for the field are 'resourceId', 'category', 'caller', 'level', 'operationName', 'resourceGroup',
        'resourceProvider', 'status', 'subStatus', 'resourceType', or anything beginning with 'properties.'.
  - name: --action-group -a
    short-summary: >
        Add an action group. Accepts space-separated action group identifiers. The identifier can be the action group's name
        or its resource ID.
  - name: --webhook-properties -w
    short-summary: >
        Space-separated webhook properties in 'key[=value]' format. These properties are associated with the action groups
        added in this command.
    long-summary: >
        For any webhook receiver in these action group, this data is appended to the webhook payload. To attach different webhook
        properties to different action groups, add the action groups in separate update-action commands.
examples:
  - name: Create an alert rule with default settings.
    text: >
        az monitor activity-log alert create -n {AlertName} -g {ResourceGroup}
  - name: Create an alert rule with condition about error level service health log.
    text: >
        az monitor activity-log alert create -n {AlertName} -g {ResourceGroup} \\
          --condition category=ServiceHealth and level=Error
  - name: Create an alert rule with an action group and specify webhook properties.
    text: >
        az monitor activity-log alert create -n {AlertName} -g {ResourceGroup} \\
          -a /subscriptions/{SubID}/resourceGroups/{ResourceGroup}/providers/microsoft.insights/actionGroups/{ActionGroup} \\
          -w usage=test owner=jane
  - name: Create an alert rule which is initially disabled.
    text: >
        az monitor activity-log alert create -n {AlertName} -g {ResourceGroup} --disable
"""

helps['monitor activity-log alert list'] = """
type: command
short-summary: List activity log alert rules under a resource group or the current subscription.
parameters:
  - name: --resource-group -g
    short-summary: Name of the resource group under which the activity log alert rules are being listed. If it is omitted, all the activity log alert rules under the current subscription are listed.
"""

helps['monitor activity-log alert scope'] = """
type: group
short-summary: Manage scopes for activity log alert rules.
"""

helps['monitor activity-log alert scope add'] = """
type: command
short-summary: Add scopes to this activity log alert rule.
parameters:
  - name: --name -n
    short-summary: Name of the activity log alert rule.
  - name: --scope -s
    short-summary: List of scopes to add. Each scope could be a resource ID, a resource group ID or a subscription ID.
  - name: --reset
    short-summary: Remove all the existing scopes before add new scopes.
examples:
  - name: Add scopes to this activity log alert rule. (autogenerated)
    text: |
        az monitor activity-log alert scope add --name MyActivityLogAlerts --resource-group MyResourceGroup --scope /subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx  /subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myRG  /subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myRG/Microsoft.KeyVault/vaults/mykey
    crafted: true
"""

helps['monitor activity-log alert scope remove'] = """
type: command
short-summary: Removes scopes from this activity log alert rule.
parameters:
  - name: --name -n
    short-summary: Name of the activity log alert rule.
  - name: --scope -s
    short-summary: The scopes to remove
"""

helps['monitor activity-log alert update'] = """
type: command
short-summary: Update the details of this activity log alert rule.
parameters:
  - name: --description
    short-summary: A description of this activity log alert rule.
  - name: --condition -c
    short-summary: The conditional expression that will cause the alert rule to activate. The format is FIELD=VALUE[ and FIELD=VALUE...].
    long-summary: >
        The possible values for the field are 'resourceId', 'category', 'caller', 'level', 'operationName', 'resourceGroup',
        'resourceProvider', 'status', 'subStatus', 'resourceType', or anything beginning with 'properties.'.
examples:
  - name: Update the condition
    text: >
        az monitor activity-log alert update -n {AlertName} -g {ResourceGroup} \\
          --condition category=ServiceHealth and level=Error
  - name: Disable an alert rule.
    text: >
        az monitor activity-log alert update -n {AlertName} -g {ResourceGroup} --enable false
  - name: Update the details of this activity log alert rule. (autogenerated)
    text: |
        az monitor activity-log alert update --enabled true --name MyActivityLogAlerts --resource-group MyResourceGroup --subscription MySubscription
    crafted: true
  - name: Update the details of this activity log alert. (autogenerated)
    text: |
        az monitor activity-log alert update --name MyActivityLogAlerts --resource-group MyResourceGroup --tags key=value
    crafted: true
"""

helps['monitor activity-log list'] = """
type: command
short-summary: List and query activity log events.
parameters:
  - name: --correlation-id
    short-summary: Correlation ID to query.
  - name: --resource-id
    short-summary: ARM ID of a resource.
  - name: --namespace
    short-summary: Resource provider namespace.
  - name: --caller
    short-summary: Caller to query for, such as an e-mail address or service principal ID.
  - name: --status
    short-summary: >
        Status to query for (ex: Failed)
  - name: --max-events
    short-summary: Maximum number of records to return.
  - name: --select
    short-summary: Space-separated list of properties to return.
  - name: --offset
    short-summary: >
        Time offset of the query range, in ##d##h format.
    long-summary: >
        Can be used with either --start-time or --end-time. If used with --start-time, then
        the end time will be calculated by adding the offset. If used with --end-time (default), then
        the start time will be calculated by subtracting the offset. If --start-time and --end-time are
        provided, then --offset will be ignored.
examples:
  - name: List all events from July 1st, looking forward one week.
    text: az monitor activity-log list --start-time 2018-07-01 --offset 7d
  - name: List events within the past six hours based on a correlation ID.
    text: az monitor activity-log list --correlation-id b5eac9d2-e829-4c9a-9efb-586d19417c5f
  - name: List events within the past hour based on resource group.
    text: az monitor activity-log list -g {ResourceGroup} --offset 1h
"""

helps['monitor activity-log list-categories'] = """
type: command
short-summary: List the event categories of activity logs.
"""

helps['monitor autoscale'] = """
type: group
short-summary: Manage autoscale settings.
long-summary: >
    For more information on autoscaling, visit: https://docs.microsoft.com/azure/monitoring-and-diagnostics/monitoring-understanding-autoscale-settings
"""

helps['monitor autoscale create'] = """
type: command
short-summary: Create new autoscale settings.
long-summary: >
    For more information on autoscaling, visit: https://docs.microsoft.com/azure/monitoring-and-diagnostics/monitoring-understanding-autoscale-settings
parameters:
  - name: --action -a
    short-summary: Add an action to fire when a scaling event occurs.
    long-summary: |
        Usage:   --action TYPE KEY [ARG ...]
        Email:   --action email bob@contoso.com ann@contoso.com
        Webhook: --action webhook https://www.contoso.com/alert apiKey=value
        Webhook: --action webhook https://www.contoso.com/alert?apiKey=value
        Multiple actions can be specified by using more than one `--action` argument.
examples:
  - name: Create autoscale settings to scale between 2 and 5 instances (3 as default). Email the administrator when scaling occurs.
    text: |
        az monitor autoscale create -g {myrg} --resource {resource-id} --min-count 2 --max-count 5 \\
          --count 3 --email-administrator

        az monitor autoscale rule create -g {myrg} --autoscale-name {resource-name} --scale out 1 \\
          --condition "Percentage CPU > 75 avg 5m"

        az monitor autoscale rule create -g {myrg} --autoscale-name {resource-name} --scale in 1 \\
          --condition "Percentage CPU < 25 avg 5m"
  - name: Create autoscale settings for exactly 4 instances.
    text: >
        az monitor autoscale create -g {myrg} --resource {resource-id} --count 4
  - name: Create new autoscale settings. (autogenerated)
    text: |
        az monitor autoscale create --count 3 --max-count 5 --min-count 2 --name MyAutoscaleSettings --resource myScaleSet --resource-group MyResourceGroup --resource-type Microsoft.Compute/virtualMachineScaleSets
    crafted: true
"""

helps['monitor autoscale profile'] = """
type: group
short-summary: Manage autoscaling profiles.
long-summary: >
    For more information on autoscaling, visit: https://docs.microsoft.com/azure/monitoring-and-diagnostics/monitoring-understanding-autoscale-settings
"""

helps['monitor autoscale profile create'] = """
type: command
short-summary: Create a fixed or recurring autoscale profile.
long-summary: >
    For more information on autoscaling, visit: https://docs.microsoft.com/azure/monitoring-and-diagnostics/monitoring-understanding-autoscale-settings
parameters:
  - name: --timezone
    short-summary: Timezone name.
    populator-commands:
      - az monitor autoscale profile list-timezones
  - name: --recurrence -r
    short-summary: When the profile recurs. If omitted, a fixed (non-recurring) profile is created.
    long-summary: |
        Usage:     --recurrence {week} [ARG ARG ...]
        Weekly:    --recurrence week Sat Sun
  - name: --start
    short-summary: When the autoscale profile begins. Format depends on the type of profile.
    long-summary: |
        Fixed:  --start yyyy-mm-dd [hh:mm:ss]
        Weekly: [--start hh:mm]
  - name: --end
    short-summary: When the autoscale profile ends. Format depends on the type of profile.
    long-summary: |
        Fixed:  --end yyyy-mm-dd [hh:mm:ss]
        Weekly: [--end hh:mm]
examples:
  - name: Create a fixed date profile, inheriting the default scaling rules but changing the capacity.
    text: |
        az monitor autoscale create -g {myrg} --resource {resource-id} --min-count 2 --count 3 \\
          --max-count 5

        az monitor autoscale rule create -g {myrg} --autoscale-name {name} --scale out 1 \\
          --condition "Percentage CPU > 75 avg 5m"

        az monitor autoscale rule create -g {myrg} --autoscale-name {name} --scale in 1 \\
          --condition "Percentage CPU < 25 avg 5m"

        az monitor autoscale profile create -g {myrg} --autoscale-name {name} -n Christmas \\
          --copy-rules default --min-count 3 --count 6 --max-count 10 --start 2018-12-24 \\
          --end 2018-12-26 --timezone "Pacific Standard Time"
  - name: Create a recurring weekend profile, inheriting the default scaling rules but changing the capacity.
    text: |
        az monitor autoscale create -g {myrg} --resource {resource-id} --min-count 2 --count 3 \\
          --max-count 5

        az monitor autoscale rule create -g {myrg} --autoscale-name {name} --scale out 1 \\
          --condition "Percentage CPU > 75 avg 5m"

        az monitor autoscale rule create -g {myrg} --autoscale-name {name} --scale in 1 \\
          --condition "Percentage CPU < 25 avg 5m"

        az monitor autoscale profile create -g {myrg} --autoscale-name {name} -n weeekend \\
          --copy-rules default --min-count 1 --count 2 --max-count 2 \\
          --recurrence week sat sun --timezone "Pacific Standard Time"
  - name: Create a fixed or recurring autoscale profile. (autogenerated)
    text: |
        az monitor autoscale profile create --autoscale-name MyAutoscale --copy-rules default --count 2 --end 2018-12-26 --max-count 10 --min-count 1 --name Christmas --recurrence week sat sun --resource-group MyResourceGroup --start 2018-12-24 --timezone "Pacific Standard Time"
    crafted: true
  - name: Create a fixed or recurring autoscale profile. (autogenerated)
    text: |
        az monitor autoscale profile create --autoscale-name MyAutoscale --count 2 --max-count 10 --min-count 1 --name Christmas --recurrence week sat sun --resource-group MyResourceGroup --start 2018-12-24 --subscription MySubscription --timezone "Pacific Standard Time"
    crafted: true
"""

helps['monitor autoscale profile delete'] = """
type: command
short-summary: Delete an autoscale profile.
examples:
  - name: Delete an autoscale profile. (autogenerated)
    text: |
        az monitor autoscale profile delete --autoscale-name MyAutoscale --name MyAutoscaleProfile --resource-group MyResourceGroup
    crafted: true
"""

helps['monitor autoscale profile list'] = """
type: command
short-summary: List autoscale profiles.
examples:
  - name: List autoscale profiles. (autogenerated)
    text: |
        az monitor autoscale profile list --autoscale-name MyAutoscale --resource-group MyResourceGroup
    crafted: true
"""

helps['monitor autoscale profile list-timezones'] = """
type: command
short-summary: Look up time zone information.
"""

helps['monitor autoscale profile show'] = """
type: command
short-summary: Show details of an autoscale profile.
"""

helps['monitor autoscale rule'] = """
type: group
short-summary: Manage autoscale scaling rules.
long-summary: >
    For more information on autoscaling, visit: https://docs.microsoft.com/azure/monitoring-and-diagnostics/monitoring-understanding-autoscale-settings
"""

helps['monitor autoscale rule copy'] = """
type: command
short-summary: Copy autoscale rules from one profile to another.
"""

helps['monitor autoscale rule create'] = """
type: command
short-summary: Add a new autoscale rule.
long-summary: >
    For more information on autoscaling, visit: https://docs.microsoft.com/azure/monitoring-and-diagnostics/monitoring-understanding-autoscale-settings
parameters:
  - name: --condition
    short-summary: The condition which triggers the scaling action.
    long-summary: >
        Usage:  --condition ["NAMESPACE"] METRIC {==,!=,>,>=,<,<=} THRESHOLD
                            {avg,min,max,total,count} PERIOD
                            [where DIMENSION {==,!=} VALUE [or VALUE ...]
                            [and   DIMENSION {==,!=} VALUE [or VALUE ...] ...]]

        Dimensions can be queried by adding the 'where' keyword and multiple dimensions can be queried by combining them with the 'and' keyword.
        Values for METRIC and appropriate THRESHOLD values can be obtained from the `az monitor metric` command.
        Format of PERIOD is "##h##m##s".
  - name: --scale
    short-summary: The direction and amount to scale.
    long-summary: |
        Usage:          --scale {to,in,out} VAL[%]
        Fixed Count:    --scale to 5
        In by Count:    --scale in 2
        Out by Percent: --scale out 10%
  - name: --timegrain
    short-summary: >
        The way metrics are polled across instances.
    long-summary: >
        The form of the timegrain is {avg,min,max,sum} VALUE. Values can be obtained from the `az monitor metric` command.
        Format of VALUE is "##h##m##s".
examples:
  - name: Scale to 5 instances when the CPU Percentage across instances is greater than 75 averaged over 10 minutes.
    text: |
        az monitor autoscale rule create -g {myrg} --autoscale-name {myvmss} \\
          --scale to 5 --condition "Percentage CPU > 75 avg 10m"
  - name: Scale up 2 instances when the CPU Percentage across instances is greater than 75 averaged over 5 minutes.
    text: |
        az monitor autoscale rule create -g {myrg} --autoscale-name {myvmss} \\
          --scale out 2 --condition "Percentage CPU > 75 avg 5m"
  - name: Scale down 50% when the CPU Percentage across instances is less than 25 averaged over 15 minutes.
    text: |
        az monitor autoscale rule create -g {myrg} --autoscale-name {myvmss} \\
          --scale in 50% --condition "Percentage CPU < 25 avg 15m"
  - name: Create autoscale settings via a guest vm metric enabled from diagnostic extensions.
          You can use counterSpecifier field retrieved from 'az vmss diagnostics get-default-config' in the `--condition`.
    text: |
        az monitor autoscale rule create -g {myrg} --autoscale-name test --scale out 1 --condition "/builtin/memory/percentavailablememory > 80 total 5m"

"""

helps['monitor autoscale rule delete'] = """
type: command
short-summary: Remove autoscale rules from a profile.
"""

helps['monitor autoscale rule list'] = """
type: command
short-summary: List autoscale rules for a profile.
examples:
  - name: List autoscale rules for a profile. (autogenerated)
    text: |
        az monitor autoscale rule list --autoscale-name MyAutoscale --profile-name MyProfile --resource-group MyResourceGroup
    crafted: true
"""

helps['monitor autoscale show'] = """
type: command
short-summary: Show autoscale setting details.
examples:
  - name: Show autoscale setting details. (autogenerated)
    text: |
        az monitor autoscale show --name MyAutoscaleSettings --resource-group MyResourceGroup
    crafted: true
"""

helps['monitor autoscale update'] = """
type: command
short-summary: Update autoscale settings.
long-summary: >
    For more information on autoscaling, visit: https://docs.microsoft.com/azure/monitoring-and-diagnostics/monitoring-understanding-autoscale-settings
parameters:
  - name: --add-action -a
    short-summary: Add an action to fire when a scaling event occurs.
    long-summary: |
        Usage:   --add-action TYPE KEY [ARG ...]
        Email:   --add-action email bob@contoso.com ann@contoso.com
        Webhook: --add-action webhook https://www.contoso.com/alert apiKey=value
        Webhook: --add-action webhook https://www.contoso.com/alert?apiKey=value
        Multiple actions can be specified by using more than one `--add-action` argument.
  - name: --remove-action -r
    short-summary: Remove one or more actions.
    long-summary: |
        Usage:   --remove-action TYPE KEY [KEY ...]
        Email:   --remove-action email bob@contoso.com ann@contoso.com
        Webhook: --remove-action webhook https://contoso.com/alert https://alerts.contoso.com
examples:
  - name: Update autoscale settings to use a fixed 3 instances by default.
    text: |
        az monitor autoscale update -g {myrg} -n {autoscale-name} --count 3
  - name: Update autoscale settings to remove an email notification.
    text: |
        az monitor autoscale update -g {myrg} -n {autoscale-name} \\
          --remove-action email bob@contoso.com
  - name: Update autoscale settings. (autogenerated)
    text: |
        az monitor autoscale update --count 3 --email-administrator true --enabled true --max-count 5 --min-count 2 --name MyAutoscaleSettings --resource-group MyResourceGroup --tags key[=value]
    crafted: true
"""

helps['monitor log-analytics workspace recover'] = """
type: command
short-summary: Recover a workspace in a soft-delete state within 14 days.
examples:
  - name: Recover a workspace in a soft-delete state within 14 days
    text: |
        az monitor log-analytics workspace recover --resource-group MyResourceGroup -n MyWorkspace
"""

helps['monitor log-analytics workspace table'] = """
type: group
short-summary: Manage tables for log analytics workspace.
"""

helps['monitor log-analytics workspace table create'] = """
type: command
short-summary: Create a Log Analytics workspace microsoft/custom log table. The table name needs to end with '_CL'.
examples:
  - name: Create a Log Analytics workspace custom log table.
    text: |
        az monitor log-analytics workspace table create --resource-group MyResourceGroup --workspace-name MyWorkspace -n MyTable_CL --retention-time 45 --columns MyColumn1=string TimeGenerated=datetime
"""

helps['monitor log-analytics workspace table search-job'] = """
type: group
short-summary: Manage tables for log analytics workspace search results table.
"""

helps['monitor log-analytics workspace table search-job create'] = """
type: command
short-summary: Create a Log Analytics workspace search results table. The table name needs to end with '_SRCH'.
examples:
  - name: Create a Log Analytics workspace search result table.
    text: |
        az monitor log-analytics workspace table search-job create --resource-group MyResourceGroup --workspace-name MyWorkspace -n MyTable_SRCH --retention-time 45 --search-query "Heartbeat | where SourceSystem != '' | project SourceSystem" --limit 1000 --start-search-time "Sat, 28 Aug 2021 05:29:18 GMT" --end-search-time "Sat, 28 Aug 2021 08:29:18 GMT"
"""

helps['monitor log-analytics workspace table restore'] = """
type: group
short-summary: Manage tables for log analytics workspace restore logs table.
"""

helps['monitor log-analytics workspace table restore create'] = """
type: command
short-summary: Create a Log Analytics workspace restore logs table. The table name needs to end with '_RST'.
examples:
  - name: Create a Log Analytics workspace restore logs table.
    text: |
        az monitor log-analytics workspace table restore create --resource-group MyResourceGroup --workspace-name MyWorkspace -n MyTable_RST --start-restore-time "Sat, 28 Aug 2021 05:29:18 GMT" --end-restore-time "Sat, 28 Aug 2021 08:29:18 GMT" --restore-source-table MyTable
"""

helps['monitor log-analytics workspace table update'] = """
type: command
short-summary: Update the properties of a Log Analytics workspace table.
examples:
  - name: Update the properties of a Log Analytics workspace table.
    text: |
        az monitor log-analytics workspace table update --resource-group MyResourceGroup --workspace-name MyWorkspace -n MyTable --retention-time 30
"""

helps['monitor log-analytics workspace saved-search create'] = """
type: command
short-summary: Create a saved search for a given workspace.
examples:
  - name: Create a saved search for a given workspace.
    text: az monitor log-analytics workspace saved-search create -g MyRG --workspace-name MyWS -n MySavedSearch --category Test1 --display-name TestSavedSearch -q "AzureActivity | summarize count() by bin(TimeGenerated, 1h)" --fa myfun --fp "a:string = value"
"""

helps['monitor log-analytics workspace saved-search update'] = """
type: command
short-summary: Update a saved search for a given workspace.
examples:
  - name: Update a saved search for a given workspace.
    text: az monitor log-analytics workspace saved-search update -g MyRG --workspace-name MyWS -n MySavedSearch --category Test1 --display-name TestSavedSearch -q "AzureActivity | summarize count() by bin(TimeGenerated, 1h)" --fa myfun --fp "a:string = value"
"""

helps['monitor log-analytics workspace linked-storage add'] = """
type: command
short-summary: Add some linked storage accounts with specific data source type for log analytics workspace.
examples:
  - name: Add two linked storage accounts for a log analytics workspace using the name of the storage account.
    text: az monitor log-analytics workspace linked-storage add --type AzureWatson -g MyResourceGroup --workspace-name MyWorkspace --storage-accounts StorageAccount1 StorageAccount2
  - name: Add one linked storage accounts for a log analytics workspace using the resource id of the storage account.
    text: az monitor log-analytics workspace linked-storage add --type AzureWatson -g MyResourceGroup --workspace-name MyWorkspace --storage-accounts /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/clitest.rg000001/providers/Microsoft.Storage/storageAccounts/cli000001
"""

helps['monitor log-analytics workspace linked-storage remove'] = """
type: command
short-summary: Remove some linked storage accounts with specific data source type for log analytics workspace
examples:
  - name: Remove two linked storage accounts for a log analytics workspace using the name of the storage account.
    text: az monitor log-analytics workspace linked-storage remove --type AzureWatson -g MyResourceGroup --workspace-name MyWorkspace --storage-accounts StorageAccount1 StorageAccount2
  - name: Remove one linked storage accounts for a log analytics workspace using the resource id of the storage account.
    text: az monitor log-analytics workspace linked-storage remove --type AzureWatson -g MyResourceGroup --workspace-name MyWorkspace --storage-accounts /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/clitest.rg000001/providers/Microsoft.Storage/storageAccounts/cli000001
"""

helps['monitor metrics'] = """
type: group
short-summary: View Azure resource metrics.
"""

helps['monitor metrics alert'] = """
type: group
short-summary: Manage near-realtime metric alert rules.
"""

helps['monitor metrics alert create'] = """
type: command
short-summary: Create a metric-based alert rule.
parameters:
  - name: --action -a
    short-summary: Add an action group and optional webhook properties to fire when the alert is triggered.
    long-summary: |
        Usage:   --action ACTION_GROUP_NAME_OR_ID [KEY=VAL [KEY=VAL ...]]

        Multiple action groups can be specified by using more than one `--action` argument.
  - name: --disabled
    short-summary: Create the rule in a disabled state.
  - name: --condition
    short-summary: The condition which triggers the rule.
                   It can be created by 'az monitor metrics alert condition create' command.
    long-summary: |
        Usage:  --condition {avg,min,max,total,count} [NAMESPACE.]METRIC
                           [{=,!=,>,>=,<,<=} THRESHOLD]
                           [{<,>,><} dynamic SENSITIVITY VIOLATIONS of EVALUATIONS [since DATETIME]]
                           [where DIMENSION {includes,excludes} VALUE [or VALUE ...]
                           [and   DIMENSION {includes,excludes} VALUE [or VALUE ...] ...]]
                           [with skipmetricvalidation]

        Sensitivity can be 'low', 'medium', 'high'.

        Violations can be the number of violations to trigger an alert. It should be smaller or equal to evaluation.

        Evaluations can be the number of evaluation periods for dynamic threshold.

        Datetime can be the date from which to start learning the metric historical data and calculate the dynamic thresholds (in ISO8601 format).

        Dimensions can be queried by adding the 'where' keyword and multiple dimensions can be queried by combining them with the 'and' keyword.

        Values for METRIC, DIMENSION and appropriate THRESHOLD values can be obtained from `az monitor metrics list-definitions` command.

        Due to server limitation, when an alert rule contains multiple criterias, the use of dimensions is limited to one value per dimension within each criterion.

        Multiple conditions can be specified by using more than one `--condition` argument.
examples:
  - name: Create a high CPU usage alert on a VM with no action.
    text: >
        az monitor metrics alert create -n alert1 -g {ResourceGroup} --scopes {VirtualMachineID} --condition "avg Percentage CPU > 90" --description "High CPU"
  - name: Create a high CPU usage alert on a VM with email and webhook actions.
    text: |
        az monitor metrics alert create -n alert1 -g {ResourceGroup} --scopes {VirtualMachineID} \\
            --condition "avg Percentage CPU > 90" --window-size 5m --evaluation-frequency 1m \\
            --action "/subscriptions/<subscriptionId>/resourceGroups/<resourceGroupName>/providers/Microsoft.Insights/actionGroups/<actionGroupName>" apiKey={APIKey} type=HighCPU \\
            --description "High CPU"
  - name: Create an alert when a storage account shows a high number of slow transactions, using multi-dimensional filters.
    text: |
        az monitor metrics alert create -g {ResourceGroup} -n alert1 --scopes {StorageAccountId} \\
            --description "Storage Slow Transactions" \\
            --condition "total transactions > 5 where ResponseType includes Success" \\
            --condition "avg SuccessE2ELatency > 250 where ApiName includes GetBlob"
  - name: Create a metric-based alert rule that monitors a custom metric.
    text: |
        az monitor metrics alert create -n "metric alert rule on a custom metric" -g "Demos" --scopes {VirtualMachineID} \\
            --condition "max Azure.VM.Windows.GuestMetrics.Memory\\Available Bytes > 90" \\
            --window-size 5m --evaluation-frequency 1m
  - name: Create a high CPU usage alert on several VMs with no actions.
    text: |
        az monitor metrics alert create -n alert1 -g {ResourceGroup} --scopes {VirtualMachineID1} {VirtualMachineID2} {VirtualMachineID3} \\
            --condition "avg Percentage CPU > 90" --description "High CPU" --region westus
  - name: Create a dynamic CPU usage alert on several VMs with no actions.
    text: |
        az monitor metrics alert create -n alert1 -g {ResourceGroup} --scopes {VirtualMachineID1} {VirtualMachineID2} {VirtualMachineID3} \\
            --condition "avg Percentage CPU > dynamic medium 2 of 4 since 2020-10-01T10:23:00.000Z"
            --description "Dynamic CPU"
            --window-size 5m
            --region westus

"""

helps['monitor metrics alert dimension'] = """
type: group
short-summary: Manage near-realtime metric alert rule dimensions.
"""

helps['monitor metrics alert dimension create'] = """
type: command
short-summary: Build a metric alert rule dimension.
examples:
  - name: Build a metric alert rule dimension.
    text: |
         $dim = az monitor metrics alert dimension create -n dimName --op Include -v GetBlob PutBlob
"""

helps['monitor metrics alert condition'] = """
type: group
short-summary: Manage near-realtime metric alert rule conditions.
"""

helps['monitor metrics alert condition create'] = """
type: command
short-summary: Build a metric alert rule condition.
parameters:
  - name: --metric
    short-summary: Name of the metric to base the rule on.
    populator-commands:
      - az monitor metrics list-definitions
examples:
  - name: Build a static condition.
    text: |
        $dim1 = az monitor metrics alert dimension create -n dimName --op Include -v GetBlob PutBlob
        $dim2 = az monitor metrics alert dimension create -n Instance --op Exclude -v Get Put
        $condition = az monitor metrics alert condition create -t static \n
        --aggregation Count \n
        --metric "CPU Percentage" \n
        --op GreaterThan  \n
        --threshold 95 \n
        --dimension "$dim1" "$dim2"
  - name: Build a dynamic condition.
    text: |
        $condition = az monitor metrics alert condition create -t dynamic \n
        --aggregation Average \n
        --metric "CPU Percentage" \n
        --op GreaterOrLessThan \n
        --num-violations 4 \n
        --num-periods 4 \n
        --since 2020-11-02T12:11
"""


helps['monitor metrics alert delete'] = """
type: command
short-summary: Delete a metrics-based alert rule.
examples:
  - name: Delete a metrics-based alert rule. (autogenerated)
    text: |
        az monitor metrics alert delete --name MyAlertRule --resource-group MyResourceGroup
    crafted: true
"""

helps['monitor metrics alert list'] = """
type: command
short-summary: List metric-based alert rules.
examples:
  - name: List metric-based alert rules. (autogenerated)
    text: |
        az monitor metrics alert list --resource-group MyResourceGroup
    crafted: true
"""

helps['monitor metrics alert show'] = """
type: command
short-summary: Show a metrics-based alert rule.
examples:
  - name: Show a metrics-based alert rule. (autogenerated)
    text: |
        az monitor metrics alert show --name MyAlertRule --resource-group MyResourceGroup
    crafted: true
"""

helps['monitor metrics alert update'] = """
type: command
short-summary: Update a metric-based alert rule.
parameters:
  - name: --add-condition
    short-summary: Add a condition which triggers the rule.
    long-summary: |
        Usage:  --add-condition {avg,min,max,total,count} [NAMESPACE.]METRIC
                           [{=,!=,>,>=,<,<=} THRESHOLD]
                           [{<,>,><} dynamic SENSITIVITY VIOLATIONS of EVALUATIONS [since DATETIME]]
                           [where DIMENSION {includes,excludes} VALUE [or VALUE ...]
                           [and   DIMENSION {includes,excludes} VALUE [or VALUE ...] ...]]

        Sensitivity can be 'low', 'medium', 'high'.

        Violations can be the number of violations to trigger an alert. It should be smaller or equal to evaluation.

        Evaluations can be the number of evaluation periods for dynamic threshold.

        Datetime can be the date from which to start learning the metric historical data and calculate the dynamic thresholds (in ISO8601 format).

        Dimensions can be queried by adding the 'where' keyword and multiple dimensions can be queried by combining them with the 'and' keyword.

        Values for METRIC, DIMENSION and appropriate THRESHOLD values can be obtained from `az monitor metrics list-definitions` command.

        Due to server limitation, when an alert rule contains multiple criterias, the use of dimensions is limited to one value per dimension within each criterion.

        Multiple conditions can be specified by using more than one `--condition` argument.
  - name: --remove-conditions
    short-summary: Space-separated list of condition names to remove.
  - name: --add-action
    short-summary: Add an action group and optional webhook properties to fire when the alert is triggered.
    long-summary: |
        Usage:   --add-action ACTION_GROUP_NAME_OR_ID [KEY=VAL [KEY=VAL ...]]

        Multiple action groups can be specified by using more than one `--action` argument.
  - name: --remove-actions
    short-summary: Space-separated list of action group names to remove.
examples:
  - name: Disable/Enable a metric-based alert rule.
    text: |
        az monitor metrics alert update --enabled false --name MyAlertRule --resource-group MyResourceGroup
"""

helps['monitor metrics list'] = """
type: command
short-summary: List the metric values for a resource.
parameters:
  - name: --aggregation
    short-summary: The list of aggregation types (space-separated) to retrieve.
    populator-commands:
      - az monitor metrics list-definitions
  - name: --interval
    short-summary: >
        The interval over which to aggregate metrics, in ##h##m format.
  - name: --filter
    short-summary: A string used to reduce the set of metric data returned. eg. "BlobType eq '*'"
    long-summary: 'For a full list of filters, see the filter string reference at https://docs.microsoft.com/rest/api/monitor/metrics/list'
  - name: --metadata
    short-summary: Returns the metadata values instead of metric data
  - name: --dimension
    short-summary: The list of dimensions (space-separated) the metrics are queried into.
    populator-commands:
      - az monitor metrics list-definitions
  - name: --namespace
    short-summary: Namespace to query metric definitions for.
    populator-commands:
      - az monitor metrics list-namespaces
  - name: --offset
    short-summary: >
        Time offset of the query range, in ##d##h format.
    long-summary: >
        Can be used with either --start-time or --end-time. If used with --start-time, then
        the end time will be calculated by adding the offset. If used with --end-time (default), then
        the start time will be calculated by subtracting the offset. If --start-time and --end-time are
        provided, then --offset will be ignored.
  - name: --metrics
    short-summary: >
        Space-separated list of metric names to retrieve.
    populator-commands:
      - az monitor metrics list-definitions

examples:
  - name: List a VM's CPU usage for the past hour
    text: >
        az monitor metrics list --resource {ResourceName} --metric "Percentage CPU"
  - name: List success E2E latency of a storage account and split the data series based on API name
    text: >
        az monitor metrics list --resource {ResourceName} --metric SuccessE2ELatency \\
                                --dimension ApiName
  - name: List success E2E latency of a storage account and split the data series based on both API name and geo type
    text: >
        az monitor metrics list --resource {ResourceName} --metric SuccessE2ELatency \\
                                --dimension ApiName GeoType
  - name: List success E2E latency of a storage account and split the data series based on both API name and geo type using "--filter" parameter
    text: >
        az monitor metrics list --resource {ResourceName} --metric SuccessE2ELatency \\
                                --filter "ApiName eq '*' and GeoType eq '*'"
  - name: List success E2E latency of a storage account and split the data series based on both API name and geo type. Limits the api name to 'DeleteContainer'
    text: >
        az monitor metrics list --resource {ResourceName} --metric SuccessE2ELatency \\
                                --filter "ApiName eq 'DeleteContainer' and GeoType eq '*'"
  - name: List transactions of a storage account per day since 2017-01-01
    text: >
        az monitor metrics list --resource {ResourceName} --metric Transactions \\
                                --start-time 2017-01-01T00:00:00Z \\
                                --interval PT24H
  - name: List the metadata values for a storage account under transaction metric's api name dimension since 2017
    text: >
        az monitor metrics list --resource {ResourceName} --metric Transactions \\
                                --filter "ApiName eq '*'" \\
                                --start-time 2017-01-01T00:00:00Z
"""

helps['monitor metrics list-definitions'] = """
type: command
short-summary: List the metric definitions for the resource.
parameters:
  - name: --namespace
    short-summary: Namespace to query metric definitions for.
    populator-commands:
      - az monitor metrics list-namespaces
examples:
  - name: List the metric definitions for the resource. (autogenerated)
    text: |
        az monitor metrics list-definitions --resource /subscriptions/{subscriptionID}/resourceGroups/{resourceGroup}/Microsoft.Network/networkSecurityGroups/{resourceName}
    crafted: true
"""

helps['monitor metrics list-namespaces'] = """
type: command
short-summary: List the metric namespaces for the resource.
examples:
  - name: List the metric namespaces for the resource.
    text: |
        az monitor metrics list-namespaces --resource /subscriptions/{subscriptionID}/resourceGroups/{resourceGroup}/Microsoft.Network/networkSecurityGroups/{resourceName} --start-time 2021-03-01T00:00:00Z
"""

helps['monitor clone'] = """
type: command
short-summary: Clone metrics alert rules from one resource to another resource.
examples:
  - name: Clone the metric alert settings from one VM to another
    text: |
        az monitor clone --source-resource /subscriptions/{subscriptionID}/resourceGroups/Space1999/providers/Microsoft.Compute/virtualMachines/vm1 --target-resource /subscriptions/{subscriptionID}/resourceGroups/Space1999/providers/Microsoft.Compute/virtualMachines/vm2
"""
