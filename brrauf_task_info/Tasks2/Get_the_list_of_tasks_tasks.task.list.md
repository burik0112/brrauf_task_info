---
title: "Get the list of tasks tasks.task.list | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/tasks-task-list.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user

The method `tasks.task.list` retrieves a list of tasks with pagination.

Access to the data depends on permissions:

- administrators see all tasks,
- managers see their employees' tasks,
- others see only the tasks available to them.

## Method Parameters

| **Name**   `type` | **Description** |
| --- | --- |
| **order**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | An object for sorting the list of tasks in the format `{"field_1": "value_1", ... "field_N": "value_N"}`.  The sorting direction can take the following values:  - `asc` — ascending - `desc` — descending  By default — descending by `ID`.  The field for sorting can take the following values:  - `ID` — task identifier - `TITLE` — task title - `TIME_SPENT_IN_LOGS` — time spent recorded in the change history - `DATE_START` — task start date - `CREATED_DATE` — task creation date - `CHANGED_DATE` — date of the last change to the task - `CLOSED_DATE` — task completion date - `ACTIVITY_DATE` — date of the last activity - `START_DATE_PLAN` — planned start date for task execution - `END_DATE_PLAN` — planned completion date for task execution - `DEADLINE` — task deadline - `REAL_STATUS` — task status - `STATUS_COMPLETE` — task completion flag - `PRIORITY` — task priority - `MARK` — rating for task completion - `CREATED_BY_LAST_NAME` — last name of the task creator - `RESPONSIBLE_LAST_NAME` — last name of the task assignee - `GROUP_ID` — workgroup identifier - `TIME_ESTIMATE` — time allocated for the task - `ALLOW_CHANGE_DEADLINE` — flag allowing the assignee to change the deadline - `ALLOW_TIME_TRACKING` — flag enabling time tracking for the task - `MATCH_WORK_TIME` — flag indicating the need to skip weekends - `FAVORITE` — flag indicating that the task has been added to favorites - `SORTING` — sorting index - `IS_PINNED` — pinned status - `IS_PINNED_IN_GROUP` — pinned in group status |
| **filter**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | An object for filtering the list of tasks in the format `{"field_1": "value_1", ... "field_N": "value_N"}`. The filterable field can take the following values:  - `ID` — task identifier - `PARENT_ID` — parent task identifier - `GROUP_ID` — workgroup identifier - `CREATED_BY` — creator - `STATUS_CHANGED_BY` — user who last changed the task status - `PRIORITY` — priority - `FORUM_TOPIC_ID` — forum topic identifier - `RESPONSIBLE_ID` — assignee - `TITLE` — task title (can search by pattern \[%\_\]) - `TAG` — task tag - `REAL_STATUS` — task status. Corresponds to the `status` field in the response. 	- `2` — waiting for execution 	- `3` — in progress 	- `4` — awaiting control 	- `5` — completed 	- `6` — postponed - `STATUS` — status for sorting. Corresponds to the `subStatus` field in the response. Similar to `REAL_STATUS`, but has three additional meta-statuses: 	- `-3` — task is almost overdue 	- `-2` — unviewed task 	- `-1` — overdue task - `MARK` — rating - `SITE_ID` — site identifier - `ADD_IN_REPORT` — task in report - `DATE_START` — start date for execution - `DEADLINE` — deadline - `CREATED_DATE` — creation date - `CLOSED_DATE` — completion date - `CHANGED_DATE` — date of the last change - `ACCOMPLICE` — co-assignee identifier - `AUDITOR` — auditor identifier - `DEPENDS_ON` — identifier of the previous task - `ONLY_ROOT_TASKS` — only root tasks and subtasks without access to the parent - `STAGE_ID` — stage - `SPRINT_ID` — sprint identifier - `BACKLOG_ID` — backlog identifier - `UF_CRM_TASK` — binding to CRM entities  To get tasks from Favorites, add the filter parameter `$filter[::SUBFILTER-PARAMS][FAVORITE]=Y`.  Before the name of the filterable field, you can specify the type of filtering:  - `!` — not equal - `<` — less than - `<=` — less than or equal to - `>` — greater than - `>=` — greater than or equal to  By default, records are not filtered |
| **select**   [`array`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | An array containing a [list of fields](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/fields.html) to be selected.  By default, the system returns only those fields stored in the record — without additional data calculated on the fly.  Warning  Always specify fields in `select`. The default set of fields may change. |
| **params**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | Additional information that can be retrieved about the task:  - `WITH_RESULT_INFO` — information about the result in the task - `WITH_TIMER_INFO` — data on time spent - `WITH_PARSED_DESCRIPTION` — description with HTML markup |
| **start**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | This parameter is used to control pagination.  The page size of results is always static — 50 records.  To select the second page of results, you need to pass the value `50`. To select the third page of results — the value `100`, and so on.  The formula for calculating the value of the `start` parameter:  `start = (N - 1) * 50`, where `N` — the number of the desired page |

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
-d '{"order":{"DEADLINE":"asc","PRIORITY":"desc"},"filter":{"!STATUS":6,">=DEADLINE":"'"$(date +%Y-%m-%d)"'","RESPONSIBLE_ID":547,"::SUBFILTER-PARAMS":{"FAVORITE":"Y"}},"select":["ID","TITLE","DESCRIPTION","STATUS","subStatus","DEADLINE","CREATED_DATE","RESPONSIBLE_ID","ACCOMPLICES","AUDITORS","TAGS","COUNTERS","PRIORITY","MARK"],"params":{"WITH_TIMER_INFO":true,"WITH_RESULT_INFO":true,"WITH_PARSED_DESCRIPTION":true}}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/tasks.task.list
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"order":{"DEADLINE":"asc","PRIORITY":"desc"},"filter":{"!STATUS":6,">=DEADLINE":"'"$(date +%Y-%m-%d)"'","RESPONSIBLE_ID":547,"::SUBFILTER-PARAMS":{"FAVORITE":"Y"}},"select":["ID","TITLE","DESCRIPTION","STATUS","subStatus","DEADLINE","CREATED_DATE","RESPONSIBLE_ID","ACCOMPLICES","AUDITORS","TAGS","COUNTERS","PRIORITY","MARK"],"params":{"WITH_TIMER_INFO":true,"WITH_RESULT_INFO":true,"WITH_PARSED_DESCRIPTION":true},"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/tasks.task.list
```

```javascript
// callListMethod: Retrieves all data at once.
// Use only for small selections (< 1000 items) due to high
// memory load.

try {
const response = await $b24.callListMethod(
    'tasks.task.list',
    {
    order: {
        'DEADLINE': 'asc',
        'PRIORITY': 'desc'
    },
    filter: {
        '!STATUS': 6,
        '>=DEADLINE': new Date().toISOString().split('T')[0],
        'RESPONSIBLE_ID': 547,
        '::SUBFILTER-PARAMS': { 'FAVORITE': 'Y' }
    },
    select: [
        'ID', 'TITLE', 'DESCRIPTION', 'STATUS', 'subStatus',
        'DEADLINE', 'CREATED_DATE', 'RESPONSIBLE_ID',
        'ACCOMPLICES', 'AUDITORS', 'TAGS', 'COUNTERS',
        'PRIORITY', 'MARK'
    ],
    params: {
        'WITH_TIMER_INFO': true,
        'WITH_RESULT_INFO': true,
        'WITH_PARSED_DESCRIPTION': true,
    },
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
const generator = $b24.fetchListMethod('tasks.task.list', {
    order: {
    'DEADLINE': 'asc',
    'PRIORITY': 'desc'
    },
    filter: {
    '!STATUS': 6,
    '>=DEADLINE': new Date().toISOString().split('T')[0],
    'RESPONSIBLE_ID': 547,
    '::SUBFILTER-PARAMS': { 'FAVORITE': 'Y' }
    },
    select: [
    'ID', 'TITLE', 'DESCRIPTION', 'STATUS', 'subStatus',
    'DEADLINE', 'CREATED_DATE', 'RESPONSIBLE_ID',
    'ACCOMPLICES', 'AUDITORS', 'TAGS', 'COUNTERS',
    'PRIORITY', 'MARK'
    ],
    params: {
    'WITH_TIMER_INFO': true,
    'WITH_RESULT_INFO': true,
    'WITH_PARSED_DESCRIPTION': true,
    },
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
const response = await $b24.callMethod('tasks.task.list', {
    order: {
    'DEADLINE': 'asc',
    'PRIORITY': 'desc'
    },
    filter: {
    '!STATUS': 6,
    '>=DEADLINE': new Date().toISOString().split('T')[0],
    'RESPONSIBLE_ID': 547,
    '::SUBFILTER-PARAMS': { 'FAVORITE': 'Y' }
    },
    select: [
    'ID', 'TITLE', 'DESCRIPTION', 'STATUS', 'subStatus',
    'DEADLINE', 'CREATED_DATE', 'RESPONSIBLE_ID',
    'ACCOMPLICES', 'AUDITORS', 'TAGS', 'COUNTERS',
    'PRIORITY', 'MARK'
    ],
    params: {
    'WITH_TIMER_INFO': true,
    'WITH_RESULT_INFO': true,
    'WITH_PARSED_DESCRIPTION': true,
    },
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
            'tasks.task.list',
            [
                'order' => [
                    'DEADLINE' => 'asc',
                    'PRIORITY' => 'desc'
                ],
                'filter' => [
                    '!STATUS' => 6,
                    '>=DEADLINE' => date('Y-m-d'),
                    'RESPONSIBLE_ID' => 547,
                    '::SUBFILTER-PARAMS' => ['FAVORITE' => 'Y']
                ],
                'select' => [
                    'ID', 'TITLE', 'DESCRIPTION', 'STATUS', 'subStatus',
                    'DEADLINE', 'CREATED_DATE', 'RESPONSIBLE_ID',
                    'ACCOMPLICES', 'AUDITORS', 'TAGS', 'COUNTERS',
                    'PRIORITY', 'MARK'
                ],
                'params' => [
                    'WITH_TIMER_INFO' => true,
                    'WITH_RESULT_INFO' => true,
                    'WITH_PARSED_DESCRIPTION' => true,
                ],
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);
    processData($result);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error fetching tasks: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'tasks.task.list',
    {
        // Sorting
        order: {
            'DEADLINE': 'asc',
            'PRIORITY': 'desc'
        },
        // Filtering
        filter: {
            '!STATUS': 6, // Exclude postponed
            '>=DEADLINE': new Date().toISOString().split('T')[0], // Not overdue
            'RESPONSIBLE_ID': 547, // Tasks of a specific assignee
            '::SUBFILTER-PARAMS': { 'FAVORITE': 'Y' } // Favorite tasks
        },
        // Fields to select
        select: [
            'ID',
            'TITLE',
            'DESCRIPTION',
            'STATUS',
            'subStatus',
            'DEADLINE',
            'CREATED_DATE',
            'RESPONSIBLE_ID',
            'ACCOMPLICES',
            'AUDITORS',
            'TAGS',
            'COUNTERS',
            'PRIORITY',
            'MARK'
        ],
        // Additional parameters
        params: {
            'WITH_TIMER_INFO': true,
            'WITH_RESULT_INFO': true,
            'WITH_PARSED_DESCRIPTION': true,
        },
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
    'tasks.task.list',
    [
        'order' => [
            'DEADLINE' => 'asc',
            'PRIORITY' => 'desc'
        ],
        'filter' => [
            '!STATUS' => 6,
            '>=DEADLINE' => date('Y-m-d'),
            'RESPONSIBLE_ID' => 547,
            '::SUBFILTER-PARAMS' => ['FAVORITE' => 'Y']
        ],
        'select' => [
            'ID', 'TITLE', 'DESCRIPTION', 'STATUS', 'subStatus',
            'DEADLINE', 'CREATED_DATE', 'RESPONSIBLE_ID',
            'ACCOMPLICES', 'AUDITORS', 'TAGS', 'COUNTERS',
            'PRIORITY', 'MARK'
        ],
        'params' => [
            'WITH_TIMER_INFO' => true,
            'WITH_RESULT_INFO' => true,
            'WITH_PARSED_DESCRIPTION' => true,
        ],
    ]
);

echo '<PRE>';
print_r($result);
echo '</PRE>';
```

## Response Handling

HTTP status: **200**

```json
{
    "result": {
        "tasks": [
            {
                "id": "8017",
                "title": "Task example",
                "description": "Task description with [B]formatting[/B]",
                "deadline": "2025-10-24T19:00:00+02:00",
                "createdDate": "2025-06-04T16:15:55+02:00",
                "responsibleId": "547",
                "priority": "2",
                "mark": "",
                "descriptionInBbcode": "Y",
                "lengthDeadline": "1",
                "status": "2",
                "auditors": [
                    "13",
                    "103"
                ],
                "accomplices": [],
                "group": [],
                "responsible": {
                    "id": "547",
                    "name": "Maria",
                    "link": "/company/personal/user/547/",
                    "icon": "/bitrix/images/tasks/default_avatar.png",
                    "workPosition": "Tester"
                },
                "accomplicesData": [],
                "auditorsData": {
                    "13": {
                        "id": "13",
                        "name": "John Smith",
                        "link": "/company/personal/user/13/",
                        "icon": "https://mysite.com/b17053/resize_cache/209/c0120a8d7c10d63c83e32398d1ec4d9e/main/c8dd225a1c6ea0a25722d01644b90fe4/8b.jpg",
                        "workPosition": "System Administrator"
                    },
                    "103": {
                        "id": "103",
                        "name": "Svetlana Ivanova",
                        "link": "/company/personal/user/103/",
                        "icon": "https://mysite.com/b17053/resize_cache/8644/c0120a8d7c10d63c83e32398d1ec4d9e/main/45f/45fff10d17d398a5583184c8350cd197/buh.jpg",
                        "workPosition": "Accountant"
                    }
                },
                "taskRequireResult": "Y",
                "taskHasOpenResult": "N",
                "taskHasResult": "Y",
                "timeElapsed": null,
                "timerIsRunningForCurrentUser": "N",
                "parsedDescription": "Task description with [B]formatting[/B]",
                "counter": {
                    "counters": {
                        "expired": 0,
                        "newComments": 0,
                        "projectExpired": 0,
                        "projectNewComments": 0,
                        "mutedExpired": 0,
                        "mutedNewComments": 0
                    },
                    "color": "gray",
                    "value": 0
                },
                "tags": {
                    "35": {
                        "id": 35,
                        "title": "arpar"
                    }
                },
                "subStatus": "2"
            }
        ]
    },
    "total": 1,
    "time": {
        "start": 1761054322,
        "finish": 1761054322.348041,
        "duration": 0.3480410575866699,
        "processing": 0,
        "date_start": "2025-10-21T16:45:22+02:00",
        "date_finish": "2025-10-21T16:45:22+02:00",
        "operating_reset_at": 1761054922,
        "operating": 0
    }
}
```

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **result**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | An object with response data |
| **tasks**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | An array of objects, where each object contains [task description](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/fields.html).  The set of fields depends on the `select` parameter |
| **total**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | Total number of records found |
| **time**   [`time`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html#time) | Information about the time taken to execute the request |

HTTP status: **400**

```json
{
    "error": "0",
    "error_description": "Invalid sorting key (internal error)"
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Description** | **Value** |
| --- | --- | --- |
| `0` | Invalid sorting key (internal error) | The `order` parameter specifies a task field that cannot be sorted or a non-existent field |

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

- [Tasks: Overview of Methods](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/index.html)
- [Add Task tasks.task.add](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-add.html)
- [Update Task tasks.task.update](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-update.html)
- [Get Task by ID tasks.task.get](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-get.html)
- [Delete Task tasks.task.delete](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-delete.html)
- [Get the list of fields tasks.task.getFields](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-get-fields.html)
- [How to Create a Comment in a Task and Attach a File](https://apidocs.bitrix24.com/api-reference/tasks/tutorials/tasks/how-to-create-comment-with-file.html)
- [How to Upload a File to a Task](https://apidocs.bitrix24.com/api-reference/tasks/tutorials/tasks/how-to-upload-file-to-task.html)
- [How to Create a Task with an Attached File](https://apidocs.bitrix24.com/api-reference/tasks/tutorials/tasks/how-to-create-task-with-file.html)