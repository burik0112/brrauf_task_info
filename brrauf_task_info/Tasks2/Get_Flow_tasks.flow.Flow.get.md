---
title: "Get Flow tasks.flow.Flow.get | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/flow/tasks-flow-flow-get.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/scopes/permissions.html)
> 
> Who can execute the method: flow team; user who can assign tasks in the flow

The method `tasks.flow.Flow.get` returns flow data by its identifier.

## Method Parameters

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **flowId** \* [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | The identifier of the flow whose data needs to be retrieved.  You can obtain the identifier by creating a new flow using the method [tasks.flow.Flow.create](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/tasks/flow/tasks-flow-flow-create.html) or by retrieving a task using the method [tasks.task.get](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/tasks/tasks-task-get.html) for a task from the flow |

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
    "flowId": 517
}' \
https://your-domain.bitrix24.com/rest/_USER_ID_/_CODE_/tasks.flow.Flow.get
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
-d '{
    "flowId": 517
}' \
https://your-domain.bitrix24.com/rest/tasks.flow.Flow.get
```

```js
try
{
    const response = await $b24.callMethod(
        'tasks.flow.Flow.get',
        {
            flowId: 517
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
            'tasks.flow.Flow.get',
            [
                'flowId' => 517
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);
    // Your logic for processing data
    processData($result);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error getting flow: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'tasks.flow.Flow.get',
    {
        flowId: 517
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
require_once('crest.php'); // connecting CRest PHP SDK

$flowId = 517;

// executing request to REST API
$result = CRest::call(
    'tasks.flow.Flow.get',
    [
        'flowId' => $flowId
    ]
);

// Processing response from Bitrix24
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
| **id**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Flow identifier |
| **creatorId**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Identifier of the flow creator. Read-only |
| **ownerId**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Identifier of the flow administrator |
| **groupId**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Identifier of the group to which the flow is linked |
| **templateId**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Identifier of the template used to create tasks in the flow |
| **efficiency**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Flow efficiency in percentage. Read-only |
| **active**   [`boolean`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Flow active status |
| **plannedCompletionTime**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Planned task completion time in seconds |
| **activity**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Date and time of the last activity in the flow. Read-only |
| **name**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Flow name |
| **description**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Flow description |
| **distributionType**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Type of task distribution in the flow |
| **responsibleList**   [`array`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | List of responsible persons for tasks in the flow. For manual distribution, this is the flow moderator |
| **demo**   [`boolean`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Indicates if the flow is a demo. System parameter. Read-only |
| **responsibleCanChangeDeadline**   [`boolean`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Can the responsible person change the task deadline |
| **matchWorkTime**   [`boolean`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Should weekends and holidays be skipped when calculating the task deadline |
| **taskControl**   [`boolean`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Should the completed task be sent to the creator for review |
| **notifyAtHalfTime**   [`boolean`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Should the assignee be notified at half the task deadline |
| **notifyOnQueueOverflow**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Number of tasks in the queue, exceeding which a notification will be sent to the flow administrator (if `null`, notifications are disabled) |
| **notifyOnTasksInProgressOverflow**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Number of tasks in progress, exceeding which a notification will be sent to the flow administrator (if `null`, notifications are disabled) |
| **notifyWhenEfficiencyDecreases**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Efficiency in percentage, below which a notification will be sent to the flow administrator (if `null`, notifications are disabled) |
| **taskCreators**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | List of users who can add tasks to the flow in the format `{"<object-type>": "<object-identifier>"}`. For example, `[{"user": 3}, {"department": "17:F"}]`.  The element `{"meta-user": "all-users"}` means that all users can add tasks |
| **team**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Flow team.  For manual distribution, this includes all project participants linked to the flow, except for the moderator.  For queue distribution and self-distribution, the team is the same as in `responsibleList` |
| **trialFeatureEnabled**   [`boolean`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | Indicates if the trial period is enabled for the flow. System parameter. Read-only |

HTTP status: **400**

```json
{
    "error": "0",
    "error_description": "Flow not found"
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Description** | **Additional Information** |
| --- | --- | --- |
| `0` | Access denied or flow not found | The account plan does not allow working with flows or the user does not have permission to retrieve flow data |
| `0` | `Unknown error` | Unknown error |
| `0` | `Flow not found` | Flow not found |

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

- [Create a new Flow tasks.flow.Flow.create](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/tasks/flow/tasks-flow-flow-create.html)
- [Update Flow tasks.flow.Flow.update](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/tasks/flow/tasks-flow-flow-update.html)
- [Delete Flow tasks.flow.Flow.delete](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/tasks/flow/tasks-flow-flow-delete.html)
- [Check the existence of the Flow tasks.flow.Flow.isExists](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/tasks/flow/tasks-flow-flow-is-exists.html)
- [Activate/Deactivate Flow tasks.flow.Flow.activate](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/tasks/flow/tasks-flow-flow-activate.html)
- [Pin or Unpin Flow tasks.flow.Flow.pin](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/tasks/flow/tasks-flow-flow-pin.html)