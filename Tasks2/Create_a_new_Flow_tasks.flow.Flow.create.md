---
title: "Create a new Flow tasks.flow.Flow.create | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/flow/tasks-flow-flow-create.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user who is not an extranet user

The method `tasks.flow.Flow.create` creates a flow.

The flow must be linked to a group. If a group ID is not provided when creating the flow, a new group will be automatically created, consisting of the creator, administrator, and the flow team.

## Method Parameters

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **flowData** \*   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Field values for creating the flow (detailed description is provided below) |

### Parameter flowData

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **name** \*   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | The name of the flow. Must be unique for each flow.  You can check the name using the method [tasks.flow.Flow.isExists](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/tasks/flow/tasks-flow-flow-is-exists.html) |
| **description**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Description of the flow |
| **groupId**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | The ID of the group to which the flow will be linked.  If not specified, a new group will be automatically created |
| **ownerId**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | The ID of the flow administrator.  If not specified, the creator will be the administrator of the flow |
| **templateId**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | The ID of the template that users will use to add tasks to the flow |
| **plannedCompletionTime** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | The planned time to complete the task in seconds |
| **distributionType** \*   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Distribution type:  - `manually` — manual distribution - `queue` — queue distribution - `himself` — self-distribution  More about distribution types can be found in the article [Flows: Overview of Methods](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/tasks/flow/index.html) |
| **responsibleList** \*   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | IDs of employees who will receive tasks.  For manual distribution, specify the ID of the flow moderator.  For self-distribution or queue distribution, specify the IDs of employees or departments. For example:  ```js [     [         'department','3'     ],     [         'department','17:F'     ] ] ```  If you do not add the suffix `:F`, the system will select all sub-departments of the specified department according to the company structure |
| **taskCreators**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | A list of users who can add tasks to the flow in the format `{"<entity-type>": "<entity-id>"}`. For example:  ```js [     [         'user','3'     ],     [         'department','17:F'     ] ] ```  If you do not add the suffix `:F`, the system will select all sub-departments of the specified department according to the company structure.  To allow all users to add tasks, specify the value `{"meta-user": "all-users"}` |
| **matchWorkTime**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Skip weekends and holidays when calculating the task deadline.  Accepts values `0` and `1`. Default is `1` |
| **responsibleCanChangeDeadline**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Can the responsible person change the task deadline.  Accepts values `0` and `1`. Default is `0` |
| **notifyAtHalfTime**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Notify the assignee at half the task deadline.  Accepts values `0` and `1`. Default is `0` |
| **taskControl**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Send the completed task to the creator for review.  Accepts values `0` and `1`. Default is `0` |
| **notifyOnQueueOverflow**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Notify the flow administrator when the number of tasks in the queue exceeds this parameter.  Default is `null`, meaning no notifications |
| **notifyOnTasksInProgressOverflow**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Notify the flow administrator when the number of tasks in progress exceeds this parameter.  Default is `null`, meaning no notifications |
| **notifyWhenEfficiencyDecreases**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Notify the flow administrator when efficiency drops below this parameter.  Default is `null`, meaning no notifications |

## Code Examples

[How to Use Examples in Documentation](https://apidocs.bitrix24.com/first-steps/how-to-use-examples.html)

cURL (Webhook)

cURL (oAuth)

JS

PHP

BX24.js

PHP CRest

```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{
    "flowData": {
        "name": "Unique Flow Name",
        "description": "Flow description",
        "plannedCompletionTime": 7200,
        "distributionType": "manually",
        "responsibleList": [["user","3"]],
        "taskCreators": [["meta-user","all-users"]],
        "matchWorkTime": 1,
        "notifyAtHalfTime": 0
    }
}' \
https://your-domain.bitrix24.com/rest/_USER_ID_/_CODE_/tasks.flow.Flow.create
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
-d '{
    "flowData": {
        "name": "Unique Flow Name",
        "description": "Flow description",
        "plannedCompletionTime": 7200,
        "distributionType": "manually",
        "responsibleList": [["user","3"]],
        "taskCreators": [["meta-user","all-users"]],
        "matchWorkTime": 1,
        "notifyAtHalfTime": 0
    }
}' \
https://your-domain.bitrix24.com/rest/tasks.flow.Flow.create
```

```js
try
{
    const response = await $b24.callMethod(
        'tasks.flow.Flow.create',
        {
            flowData: {
                name: 'Unique Flow Name',
                description: 'Flow description',
                plannedCompletionTime: 7200,
                distributionType: 'manually',
                responsibleList: [
                    [
                        'user','3'
                    ]
                ],
                taskCreators: [
                    [
                        'meta-user','all-users'
                    ]
                ],
                matchWorkTime: 1,
                notifyAtHalfTime: 0
            }
        }
    );
    
    const result = response.getData().result;
    console.info(result);
}
catch( error )
{
    console.error(error);
}
```

```php
try {
    $response = $b24Service
        ->core
        ->call(
            'tasks.flow.Flow.create',
            [
                'flowData' => [
                    'name'                  => 'Unique Flow Name',
                    'description'           => 'Flow description',
                    'plannedCompletionTime' => 7200,
                    'distributionType'      => 'manually',
                    'responsibleList'       => [
                        ['user', '3']
                    ],
                    'taskCreators'          => [
                        ['meta-user', 'all-users']
                    ],
                    'matchWorkTime'         => 1,
                    'notifyAtHalfTime'      => 0
                ]
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error creating flow: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'tasks.flow.Flow.create',
    {
        flowData: {
            name: 'Unique Flow Name',
            description: 'Flow description',
            plannedCompletionTime: 7200,
            distributionType: 'manually',
            responsibleList: [
                [
                    'user','3'
                ]
            ],
            taskCreators: [
                [
                    'meta-user','all-users'
                ]
            ],
            matchWorkTime: 1,
            notifyAtHalfTime: 0
        }
    },
    function(result) {
        if (result.error()) {
            console.error(result.error());
        } else {
            console.info(result.data());
        }
    }
);
```

```php
require_once('crest.php'); // connect CRest PHP SDK

$flowData = [
    "name" => "Unique Flow Name",
    "description" => "Flow description",
    "plannedCompletionTime" => 7200,
    "distributionType" => "manually",
    "responsibleList" => [["user", "3"]],
    "taskCreators" => [["meta-user", "all-users"]],
    "matchWorkTime" => 1,
    "notifyAtHalfTime" => 0
];

// execute the request to the REST API
$result = CRest::call(
    'tasks.flow.Flow.create',
    [
        'flowData' => $flowData
    ]
);

// Process the response from Bitrix24
if ($result['error']) {
    echo 'Error: '.$result['error_description'];
} else {
    print_r($result['result']);
}
```

## Response Handling

HTTP status: **200**

```json
{
    "result": {
        "id": 517,
        "creatorId": 1,
        "ownerId": 1,
        "groupId": 178,
        "templateId": 0,
        "efficiency": 0,
        "active": true,
        "plannedCompletionTime": 7200,
        "activity": "2024-09-02T15:27:29+00:00",
        "name": "Updated Flow Name",
        "description": "Updated description",
        "distributionType": "manually",
        "responsibleList": [
            [
                "user",
                "3"
            ]
        ],
        "demo": false,
        "responsibleCanChangeDeadline": true,
        "matchWorkTime": true,
        "taskControl": false,
        "notifyAtHalfTime": false,
        "notifyOnQueueOverflow": 10,
        "notifyOnTasksInProgressOverflow": 50,
        "notifyWhenEfficiencyDecreases": null,
        "taskCreators": [
            [
                "meta-user",
                "all-users"
            ]
        ],
        "team": [
            [
                "user",
                "3"
            ]
        ],
        "trialFeatureEnabled": false
    }
}
```

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **result**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Object with flow data |
| **id**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | ID of the created flow |
| **creatorId**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | ID of the flow creator. Read-only |
| **ownerId**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | ID of the flow administrator |
| **groupId**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | ID of the group to which the flow is linked |
| **templateId**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | ID of the template used to create tasks in the flow |
| **efficiency**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Efficiency of the flow in percentage. Read-only |
| **active**   [`boolean`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Status of the flow's activity |
| **plannedCompletionTime**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Planned time to complete the task in seconds |
| **activity**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Date and time of the last activity in the flow. Read-only |
| **name**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Name of the flow |
| **description**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Description of the flow |
| **distributionType**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Type of task distribution in the flow |
| **responsibleList**   [`array`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | List of responsible persons for tasks in the flow. For manual distribution, this is the flow moderator |
| **demo**   [`boolean`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Indicates whether the flow is a demo. System parameter. Read-only |
| **responsibleCanChangeDeadline**   [`boolean`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Can the responsible person change the task deadline |
| **matchWorkTime**   [`boolean`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Whether to skip weekends and holidays when calculating the task deadline |
| **taskControl**   [`boolean`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Whether to send the completed task to the creator for review |
| **notifyAtHalfTime**   [`boolean`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Whether to notify the assignee at half the task deadline |
| **notifyOnQueueOverflow**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Number of tasks in the queue, exceeding which will send a notification to the flow administrator (if `null`, notifications are disabled) |
| **notifyOnTasksInProgressOverflow**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Number of tasks in progress, exceeding which will send a notification to the flow administrator (if `null`, notifications are disabled) |
| **notifyWhenEfficiencyDecreases**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Efficiency in percentage, below which a notification will be sent to the flow administrator (if `null`, notifications are disabled) |
| **taskCreators**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | List of users who can add tasks to the flow in the format `{"<object-type>": "<object-id>"}`. For example, `[{"user": 3}, {"department": "17:F"}]`.  The element `{"meta-user": "all-users"}` means that all users can add tasks |
| **team**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Flow team.  For manual distribution, this includes all project participants to which the flow is linked, except for the moderator.  For queue and self-distribution, the team is the same as in `responsibleList` |
| **trialFeatureEnabled**   [`boolean`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Indicates whether the trial period is enabled for the flow. System parameter. Read-only |

HTTP status: **400**

```json
{
    "error": "0",
    "error_description": "Access denied or flow not found"
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Description** | **Additional Information** |
| --- | --- | --- |
| `0` | Access denied or flow not found | The account plan does not allow working with flows or the user does not have permission to create a flow |
| `0` | `Unknown error` | Unknown error |
| `0` | `'distributionType': field's value has an invalid value` | Invalid value for `distributionType` (similarly for other parameters) |
| `0` | A flow with this name already exists |  |

HTTP Status: **20x**, **40x**, **50x**

The errors described below may occur when calling any method.

| **Status** | **Code**   **Error Message** | **Description** |
| --- | --- | --- |
| `500` | `INTERNAL_SERVER_ERROR`   Internal server error | An internal server error has occurred, please contact the server administrator or [Bitrix24 technical support](https://apidocs.bitrix24.com/bitrix-support.html) |
| `500` | `ERROR_UNEXPECTED_ANSWER`   Server returned an unexpected response | An internal server error has occurred, please contact the server administrator or [Bitrix24 technical support](https://apidocs.bitrix24.com/bitrix-support.html) |
| `503` | `QUERY_LIMIT_EXCEEDED`   Too many requests | The [request intensity limit](https://apidocs.bitrix24.com/limits.html) has been exceeded |
| `405` | `ERROR_BATCH_METHOD_NOT_ALLOWED`   Method is not allowed for batch usage | The current method is not allowed to be called using [batch](https://apidocs.bitrix24.com/settings/how-to-call-rest-api/batch.html) |
| `400` | `ERROR_BATCH_LENGTH_EXCEEDED`   Max batch length exceeded | The maximum length of parameters passed to the [batch](https://apidocs.bitrix24.com/settings/how-to-call-rest-api/batch.html) method has been exceeded |
| `401` | `NO_AUTH_FOUND`   Wrong authorization data | Invalid [access token](https://apidocs.bitrix24.com/settings/oauth/index.html) or [webhook code](https://apidocs.bitrix24.com/local-integrations/local-webhooks.html) |
| `400` | `INVALID_REQUEST`   Https required | The methods must be called using the HTTPS protocol |
| `503` | `OVERLOAD_LIMIT`   REST API is blocked due to overload | The REST API is blocked due to overload. This is a manual individual block, to remove it you need to contact [Bitrix24 technical support](https://apidocs.bitrix24.com/bitrix-support.html) |
| `403` | `ACCESS_DENIED`   REST API is available only on commercial plans | The REST API is available only on commercial plans |
| `403` | `INVALID_CREDENTIALS`   Invalid request credentials | The user whose [access token](https://apidocs.bitrix24.com/settings/oauth/index.html) or [webhook](https://apidocs.bitrix24.com/local-integrations/local-webhooks.html) was used to call the method lacks permissions |
| `404` | `ERROR_MANIFEST_IS_NOT_AVAILABLE`   Manifest is not available | The manifest is not available |
| `403` | `insufficient_scope`   The request requires higher privileges than provided by the webhook token | The request requires higher privileges than those provided by the [webhook](https://apidocs.bitrix24.com/local-integrations/local-webhooks.html) token |
| `401` | `expired_token`   The access token provided has expired | The provided [access token](https://apidocs.bitrix24.com/settings/oauth/index.html) has expired |
| `403` | `user_access_error`   The user does not have access to the application | The user does not have access to the application. This means that the application is installed, but the account administrator has allowed access to this application only for specific users |
| `500` | `PORTAL_DELETED`   Portal was deleted | The public part of the site is closed. To open the public part of the site on an on-premise installation, disable the option "Temporary closure of the public part of the site". Path to the setting: *Desktop > Settings > Product Settings > Module Settings > Main Module > Temporary closure of the public part of the site* |

## Continue Learning

- [Update Flow tasks.flow.Flow.update](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/tasks/flow/tasks-flow-flow-update.html)
- [Get Flow tasks.flow.Flow.get](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/tasks/flow/tasks-flow-flow-get.html)
- [Delete Flow tasks.flow.Flow.delete](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/tasks/flow/tasks-flow-flow-delete.html)
- [Check the existence of the Flow tasks.flow.Flow.isExists](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/tasks/flow/tasks-flow-flow-is-exists.html)
- [Activate/Deactivate Flow tasks.flow.Flow.activate](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/tasks/flow/tasks-flow-flow-activate.html)
- [Pin or Unpin Flow tasks.flow.Flow.pin](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/tasks/flow/tasks-flow-flow-pin.html)