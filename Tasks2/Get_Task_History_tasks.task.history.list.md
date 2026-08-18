---
title: "Get Task History tasks.task.history.list | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/tasks-task-history-list.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user with read access to the task

The method `tasks.task.history.list` retrieves the history of changes for a task.

## Method Parameters

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **taskId** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | The identifier of the task for which to retrieve the history.  The task identifier can be obtained when [creating a new task](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-add.html) or by using the [get task list method](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-list.html) |
| **filter**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | Filter by event type in the format `{FIELD: 'EVENT'}`. A list of possible values for `FIELD` is described [below](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-history-list.html#lists) |
| **order**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | An object for sorting the result in the form `{"field": "sort value", ... }`.  The sorting direction can take the following values:  - `asc` — ascending - `desc` — descending  By default, records are sorted in descending order by creation time, meaning from newest to oldest |

## Code Examples

[How to Use Examples in Documentation](https://apidocs.bitrix24.com/first-steps/how-to-use-examples.html)

cURL (Webhook)

cURL (OAuth)

JS

PHP

BX24.js

PHP CRest

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"taskId":8137,"filter":{"FIELD":"COMMENT"},"order":{"createdDate":"ASC"}}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/tasks.task.history.list
```

```javascript
// callListMethod: Retrieves all data at once.
// Use only for small selections (< 1000 items) due to high
// memory load.

try {
const response = await $b24.callListMethod(
    'tasks.task.history.list',
    {
        taskId: 8137,
        filter: { FIELD: 'COMMENT' },
        order: { createdDate: 'ASC' }
    },
    (progress) => { console.log('Progress:', progress) }
);
const items = response.getData() || [];
for (const entity of items) { console.log('Entity:', entity) }
} catch (error) {
console.error('Request failed', error)
}

// fetchListMethod: Retrieves data in parts using an iterator.
// Use for large volumes of data for efficient memory consumption.

try {
const generator = $b24.fetchListMethod('tasks.task.history.list', {
    taskId: 8137,
    filter: { FIELD: 'COMMENT' },
    order: { createdDate: 'ASC' }
}, 'ID');
for await (const page of generator) {
    for (const entity of page) { console.log('Entity:', entity) }
}
} catch (error) {
console.error('Request failed', error)
}

// callMethod: Manual control of pagination through the start parameter.
// Use for precise control over request batches.
// Less efficient for large data than fetchListMethod.

try {
const response = await $b24.callMethod('tasks.task.history.list', {
    taskId: 8137,
    filter: { FIELD: 'COMMENT' },
    order: { createdDate: 'ASC' }
}, 0);
const result = response.getData().result || [];
for (const entity of result) { console.log('Entity:', entity) }
} catch (error) {
console.error('Request failed', error)
}
```

```php
try {
    $response = $b24Service
        ->core
        ->call(
            'tasks.task.history.list',
            [
                'taskId' => 8137,
                'filter' => ['FIELD' => 'COMMENT'],
                'order' => ['createdDate' => 'ASC']
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);
    processData($result);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error fetching task history: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'tasks.task.history.list',
    {
        taskId: 8137,
        filter: { FIELD: 'COMMENT' },
        order: {createdDate: 'ASC'},
    },
    function(result){
        console.info(result.data());
        console.log(result);
    }
);
```

```php
require_once('crest.php');

$result = CRest::call(
    'tasks.task.history.list',
    [
        'taskId' => 8137,
        'filter' => ['FIELD' => 'COMMENT'],
        'order' => ['createdDate' => 'ASC']
    ]
);

echo '<PRE>';
print_r($result);
echo '</PRE>';
```

## Response Handling

HTTP Status: **200**

```json
{
    "result": {
        "list": [
            {
                "id": 16359,
                "createdDate": "2025-09-25T14:09:45+02:00",
                "field": "NEW",
                "value": {
                    "from": null,
                    "to": null
                },
                "user": {
                    "id": 503,
                    "name": "Maria",
                    "lastName": "Ivanova",
                    "secondName": "",
                    "login": "maria@mysite.com"
                }
            },
            {
                "id": 16361,
                "createdDate": "2025-09-25T14:09:45+02:00",
                "field": "COMMENT",
                "value": {
                    "from": null,
                    "to": "3409"
                },
                "user": {
                    "id": 503,
                    "name": "Maria",
                    "lastName": "Ivanova",
                    "secondName": "",
                    "login": "maria@mysite.com"
                }
            },
            {
                "id": 16363,
                "createdDate": "2025-09-25T14:09:45+02:00",
                "field": "CHECKLIST_ITEM_CREATE",
                "value": {
                    "from": "",
                    "to": "What to do"
                },
                "user": {
                    "id": 503,
                    "name": "Maria",
                    "lastName": "Ivanova",
                    "secondName": "",
                    "login": "maria@mysite.com"
                }
            },
            {
                "id": 16365,
                "createdDate": "2025-09-25T14:09:45+02:00",
                "field": "CHECKLIST_ITEM_CREATE",
                "value": {
                    "from": "",
                    "to": "Contact the client"
                },
                "user": {
                    "id": 503,
                    "name": "Maria",
                    "lastName": "Ivanova",
                    "secondName": "",
                    "login": "maria@mysite.com"
                }
            },
            {
                "id": 16367,
                "createdDate": "2025-09-25T14:09:45+02:00",
                "field": "CHECKLIST_ITEM_CREATE",
                "value": {
                    "from": "",
                    "to": "Prepare the contract"
                },
                "user": {
                    "id": 503,
                    "name": "Maria",
                    "lastName": "Ivanova",
                    "secondName": "",
                    "login": "maria@mysite.com"
                }
            },
            {
                "id": 16369,
                "createdDate": "2025-09-25T14:09:45+02:00",
                "field": "CHECKLIST_ITEM_CREATE",
                "value": {
                    "from": "",
                    "to": "Sign the contract"
                },
                "user": {
                    "id": 503,
                    "name": "Maria",
                    "lastName": "Ivanova",
                    "secondName": "",
                    "login": "maria@mysite.com"
                }
            },
            {
                "id": 16371,
                "createdDate": "2025-09-25T14:09:57+02:00",
                "field": "AUDITORS",
                "value": {
                    "from": "",
                    "to": "547"
                },
                "user": {
                    "id": 503,
                    "name": "Maria",
                    "lastName": "Ivanova",
                    "secondName": "",
                    "login": "maria@mysite.com"
                }
            },
            {
                "id": 16375,
                "createdDate": "2025-09-25T14:09:57+02:00",
                "field": "COMMENT",
                "value": {
                    "from": null,
                    "to": "3411"
                },
                "user": {
                    "id": 503,
                    "name": "Maria",
                    "lastName": "Ivanova",
                    "secondName": "",
                    "login": "maria@mysite.com"
                }
            },
            {
                "id": 16373,
                "createdDate": "2025-09-25T14:09:58+02:00",
                "field": "COMMENT",
                "value": {
                    "from": null,
                    "to": "3413"
                },
                "user": {
                    "id": 503,
                    "name": "Maria",
                    "lastName": "Ivanova",
                    "secondName": "",
                    "login": "maria@mysite.com"
                }
            }
        ],
    },
    "time": {
        "start": 1758798620,
        "finish": 1758798620.969019,
        "duration": 0.9690189361572266,
        "processing": 0,
        "date_start": "2025-09-25T14:10:20+02:00",
        "date_finish": "2025-09-25T14:10:20+02:00",
        "operating_reset_at": 1758799220,
        "operating": 0
    }
}
```

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **result**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | The root element of the response. Contains an array `list`, which includes objects with [event descriptions](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-history-list.html#lists) for the task.  Returns an empty array `"list":[]` if the task does not exist |
| **time**   [`time`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html#time) | Information about the request execution time |

#### Objects lists

| **Name**   `type` | **Description** |
| --- | --- |
| **id**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | Identifier of the history event |
| **createdDate**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | Date and time of the event creation in ISO 8601 format |
| **field**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | Type of history event. Possible values for `field`:  - `TITLE` — task title change - `DESCRIPTION` — task description change - `REAL_STATUS` — actual status change - `STATUS` — task status change - `PRIORITY` — priority change - `MARK` — task rating change - `COMMENT` — comment addition - `DELETE` — task deletion - `NEW` — new task creation - `RENEW` — task restoration - `MOVE_TO_BACKLOG` — move task to backlog - `MOVE_TO_SPRINT` — move task to sprint - `PARENT_ID` — change of parent task - `GROUP_ID` — change of workgroup/project - `STAGE_ID` — stage change - `CREATED_BY` — change of task author - `RESPONSIBLE_ID` — change of assignee - `ACCOMPLICES` — change of participants - `AUDITORS` — change of auditors - `DEADLINE` — deadline change - `START_DATE_PLAN` — planned start date change - `END_DATE_PLAN` — planned end date change - `DURATION_PLAN` — planned duration change - `DURATION_PLAN_SECONDS` — planned duration change in seconds - `DURATION_FACT` — actual duration change - `TIME_ESTIMATE` — time estimate change - `TIME_SPENT_IN_LOGS` — actual time spent change in logs - `TAGS` — task tags change - `DEPENDS_ON` — change of task dependencies - `FILES` — change of file list - `UF_TASK_WEBDAV_FILES` — change of user field with files - `CHECKLIST_ITEM_CREATE` — checklist item creation - `CHECKLIST_ITEM_RENAME` — checklist item renaming - `CHECKLIST_ITEM_REMOVE` — checklist item removal - `CHECKLIST_ITEM_CHECK` — checklist item marked as completed - `CHECKLIST_ITEM_UNCHECK` — checklist item unmarked as completed - `ADD_IN_REPORT` — change of "add to report" flag - `TASK_CONTROL` — change of result control - `ALLOW_TIME_TRACKING` — enable or disable time tracking - `ALLOW_CHANGE_DEADLINE` — allow or disallow deadline changes - `FLOW_ID` — change of flow |
| **value**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | The object describes what change occurred:  - `from` — value before the change - `to` — value after the change  The type of value depends on the event: for a new comment — `ID` of the comment, for checklist item change — text of the item, for adding an auditor — user identifier, and so on |
| **user**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | An object with [user description](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-history-list.html#user) who performed the action |

#### User Object

| **Name**   `type` | **Description** |
| --- | --- |
| **id**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | User identifier |
| **name**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | First name |
| **lastName**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | Last name |
| **secondName**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | Middle name |
| **login**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | Login |

HTTP Status: **400**

```json
{
    "error": "0",
    "error_description": "Access denied. (internal error)"
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Description** | **Value** |
| --- | --- | --- |
| `100` | CTaskItem All parameters in the constructor must have real class type (internal error) | Required parameter `taskId` is missing |
| `0` | wrong task id (internal error) | The value of `taskId` is of incorrect type |
| `0` | Access denied. (internal error) | The user does not have access to the task |

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

- [Get Task by ID tasks.task.get](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-get.html)
- [Get the list of tasks tasks.task.list](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-list.html)