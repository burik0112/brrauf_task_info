---
title: "Add Task tasks.task.add | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/tasks-task-add.html"
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

The method `tasks.task.add` adds a new task.

## Method Parameters

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **fields** \*   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | Values of [task fields](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/fields.html). Required fields for creating a task:  - `TITLE` — task title - `RESPONSIBLE_ID` — responsible person's identifier  Check which required custom fields are set for tasks in your Bitrix24. All required fields must be passed to the method.  You can pass the parameter `SE_PARAMETER` to the method — a list of objects with additional task parameters. Possible values for `CODE`:  - `1` — deadlines are determined by the deadlines of subtasks - `2` — automatically complete the task when subtasks are completed (and vice versa) - `3` — do not complete the task without a result  ```js SE_PARAMETER: [     {         VALUE: 'Y',         CODE: 3     },     {         VALUE: 'Y',         CODE: 2     } ] ``` |

## Code Examples

[How to Use Examples in Documentation](https://apidocs.bitrix24.com/first-steps/how-to-use-examples.html)

Let's add a task with files and CRM entity bindings. To attach a file to the task, you need to add the character `n` before the file identifier.

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
-d '{"fields":{"TITLE":"Task Title","DEADLINE":"2025-12-31T23:59:59","CREATED_BY":456,"RESPONSIBLE_ID":123,"UF_CRM_TASK":["L_4","C_7","CO_5","D_10"],"UF_TASK_WEBDAV_FILES":["n12345","n67890"]}}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/tasks.task.add
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"fields":{"TITLE":"Task Title","DEADLINE":"2025-12-31T23:59:59","CREATED_BY":456,"RESPONSIBLE_ID":123,"UF_CRM_TASK":["L_4","C_7","CO_5","D_10"],"UF_TASK_WEBDAV_FILES":["n12345","n67890"]},"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/tasks.task.add
```

```js
try
{
    const response = await $b24.callMethod(
        "tasks.task.add",
        {
            fields: {               
                TITLE: "Task Title", // Task title
                DEADLINE: "2025-12-31T23:59:59", // Deadline
                CREATED_BY: 456, // Creator's identifier
                RESPONSIBLE_ID: 123, // Responsible person's identifier
                // Example of passing multiple values in the UF_CRM_TASK field
                UF_CRM_TASK: [
                    "L_4", // Binding to lead
                    "C_7", // Binding to contact
                    "CO_5", // Binding to company
                    "D_10" // Binding to deal
                ],
                // Example of passing multiple files in the UF_TASK_WEBDAV_FILES field
                UF_TASK_WEBDAV_FILES: [
                    "n12345", // Identifier of the first disk file
                    "n67890" // Identifier of the second disk file
                ]
            }
        }
    );
    
    const result = response.getData().result;
    console.info("Task successfully created with ID " + result.task.id);
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
            'tasks.task.add',
            [
                'fields' => [
                    'TITLE'         => 'Task Title',
                    'DEADLINE'      => '2025-12-31T23:59:59',
                    'CREATED_BY'    => 456,
                    'RESPONSIBLE_ID' => 123,
                    'UF_CRM_TASK'   => [
                        'L_4',
                        'C_7',
                        'CO_5',
                        'D_10',
                    ],
                    'UF_TASK_WEBDAV_FILES' => [
                        'n12345',
                        'n67890',
                    ],
                ],
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Task successfully created with ID ' . $result['task']['id'];

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error creating task: ' . $e->getMessage();
}
```

```javascript
BX24.callMethod(
    "tasks.task.add",
    {
        fields: {               
            TITLE: "Task Title", // Task title
            DEADLINE: "2025-12-31T23:59:59", // Deadline
            CREATED_BY: 456, // Creator's identifier
            RESPONSIBLE_ID: 123, // Responsible person's identifier
            // Example of passing multiple values in the UF_CRM_TASK field
            UF_CRM_TASK: [
                "L_4", // Binding to lead
                "C_7", // Binding to contact
                "CO_5", // Binding to company
                "D_10" // Binding to deal
            ],
            // Example of passing multiple files in the UF_TASK_WEBDAV_FILES field
            UF_TASK_WEBDAV_FILES: [
                "n12345", // Identifier of the first disk file
                "n67890" // Identifier of the second disk file
            ]
        }
    },
    function(result) {
        if (result.error()) {
            console.error(result.error());
        } else {
            console.info("Task successfully created with ID " + result.data().task.id);
        }
    }
);
```

```php
require_once('crest.php');

$result = CRest::call(
    'tasks.task.add',
    [
        'fields' => [
            'TITLE' => 'Task Title', // Task title
            'DEADLINE' => '2025-12-31T23:59:59', // Deadline
            'CREATED_BY' => 456, // Creator's identifier
            'RESPONSIBLE_ID' => 123, // Responsible person's identifier
            // Example of passing multiple values in the UF_CRM_TASK field
            'UF_CRM_TASK' => [
                'L_4', // Binding to lead
                'C_7', // Binding to contact
                'CO_5', // Binding to company
                'D_10' // Binding to deal
            ],
            // Example of passing multiple files in the UF_TASK_WEBDAV_FILES field
            'UF_TASK_WEBDAV_FILES' => [
                'n12345', // Identifier of the first disk file
                'n67890' // Identifier of the second disk file
            ]
        ]
    }
);

if (isset($result['error'])) {
    echo 'Error: ' . $result['error_description'];
} else {
    echo 'Task successfully created with ID ' . $result['result']['task']['id'];
}
```

## Response Handling

HTTP Status: **200**

```json
{
    "result": {
        "task": {
            "id": "3711",
            "parentId": null,
            "title": "task for test",
            "description": "",
            "mark": null,
            "priority": "1",
            "multitask": "N",
            "notViewed": "N",
            "replicate": "N",
            "stageId": "0",
            "createdBy": "1",
            "createdDate": "2024-11-02T10:06:08+02:00",
            "responsibleId": "1",
            "changedBy": "1",
            "changedDate": "2024-11-02T10:06:08+02:00",
            "statusChangedBy": null,
            "closedBy": null,
            "closedDate": null,
            "activityDate": "2024-11-02T10:06:08+02:00",
            "dateStart": null,
            "deadline": null,
            "startDatePlan": null,
            "endDatePlan": null,
            "guid": "{c2794da9-c7fe-404d-a709-ddab4578717a}",
            "xmlId": null,
            "commentsCount": null,
            "serviceCommentsCount": null,
            "allowChangeDeadline": "N",
            "allowTimeTracking": "N",
            "taskControl": "N",
            "addInReport": "N",
            "forkedByTemplateId": null,
            "timeEstimate": "0",
            "timeSpentInLogs": null,
            "matchWorkTime": "N",
            "forumTopicId": null,
            "forumId": null,
            "siteId": "s1",
            "subordinate": "Y",
            "exchangeModified": null,
            "exchangeId": null,
            "outlookVersion": "1",
            "viewedDate": null,
            "sorting": null,
            "durationFact": null,
            "isMuted": "N",
            "isPinned": "N",
            "isPinnedInGroup": "N",
            "flowId": null,
            "descriptionInBbcode": "Y",
            "status": "2",
            "statusChangedDate": "2024-11-02T10:06:08+02:00",
            "durationPlan": null,
            "durationType": "days",
            "favorite": "N",
            "groupId": "0",
            "auditors": [],
            "accomplices": [],
            "checklist": [],
            "group": [],
            "creator": {
                "id": "1",
                "name": "Viola",
                "link": "/company/personal/user/1/",
                "icon": "https://your-domain.bitrix24.com/b13743910/resize_cache/2267/c0120a8d7c10d63c83e32398d1ec4d9e/main/c7b/c7bd44b1babaa5448125dd97d038ce1b/d5fb56b94dc2c3cd8c006a2c595a4895.jpg",
                "workPosition": ""
            },
            "responsible": {
                "id": "1",
                "name": "Viola",
                "link": "/company/personal/user/1/",
                "icon": "https://your-domain.bitrix24.com/b13743910/resize_cache/2267/c0120a8d7c10d63c83e32398d1ec4d9e/main/c7b/c7bd44b1babaa5448125dd97d038ce1b/d5fb56b94dc2c3cd8c006a2c595a4895.jpg",
                "workPosition": ""
            },
            "accomplicesData": [],
            "auditorsData": [],
            "newCommentsCount": 0,
            "action": {
                "accept": false,
                "decline": false,
                "complete": true,
                "approve": false,
                "disapprove": false,
                "start": true,
                "pause": false,
                "delegate": true,
                "remove": true,
                "edit": true,
                "defer": true,
                "renew": false,
                "create": true,
                "changeDeadline": true,
                "checklistAddItems": true,
                "addFavorite": true,
                "deleteFavorite": false,
                "rate": true,
                "edit.originator": false,
                "checklist.reorder": true,
                "elapsedtime.add": true,
                "dayplan.timer.toggle": false,
                "edit.plan": true,
                "checklist.add": true,
                "favorite.add": true,
                "favorite.delete": false
            },
            "checkListTree": {
                "nodeId": 0,
                "fields": {
                    "id": null,
                    "copiedId": null,
                    "entityId": null,
                    "userId": 1,
                    "createdBy": null,
                    "parentId": null,
                    "title": "",
                    "sortIndex": null,
                    "displaySortIndex": "",
                    "isComplete": false,
                    "isImportant": false,
                    "completedCount": 0,
                    "members": [],
                    "attachments": []
                },
                "action": [],
                "descendants": []
            },
            "checkListCanAdd": true
        }
    },
    "time": {
        "start": 1758188171.142611,
        "finish": 1758188172.101309,
        "duration": 0.958698034286499,
        "processing": 0.9341180324554443,
        "date_start": "2025-09-18T12:36:11+03:00",
        "date_finish": "2025-09-18T12:36:12+03:00",
        "operating_reset_at": 1758188771,
        "operating": 0.9340989589691162
    }
}
```

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **result**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | Object with response data |
| **task**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | Object with [task description](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/fields.html) after the operation is performed |
| **time**   [`time`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html#time) | Information about the request execution time |

HTTP Status: **400**

```json
{
    "error": "ERROR_CORE",
    "error_description": "Task title not specified\u003Cbr\u003E"
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Description** | **Value** |
| --- | --- | --- |
| `100` | Could not find value for parameter {fields} (internal error) | Parameter `fields` not passed or passed empty |
| `ERROR_CORE` | User specified in the "Responsible" field not found | An identifier of a non-existent user is specified in the `RESPONSIBLE_ID` field |
| `ERROR_CORE` | Responsible person not specified | The `RESPONSIBLE_ID` field is not filled |
| `ERROR_CORE` | Task title not specified | The `TITLE` field is not filled |
| `ERROR_CORE` | No value entered for required field | Required custom field with the specified name is not filled |
| `ERROR_CORE` | Invalid status | An incorrect value is specified in the `STATUS` field |
| `ERROR_CORE` | Task specified in the "Parent Task" field not found | An identifier of a non-existent task is specified in the `PARENT_ID` field |
| `ERROR_CORE` | In scheduling deadlines, the end date is earlier than the start date | The date and time in the `END_DATE_PLAN` field is earlier than in `START_DATE_PLAN` |
| `ERROR_CORE` | In scheduling deadlines, the task duration is too long | The value in the `END_DATE_PLAN` field specifies a date that is too far in the future |

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
- [Update Task tasks.task.update](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-update.html)
- [Get Task by ID tasks.task.get](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-get.html)
- [Get the list of tasks tasks.task.list](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-list.html)
- [Delete Task tasks.task.delete](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-delete.html)
- [Get the list of fields tasks.task.getFields](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-get-fields.html)
- [How to Create a Task with an Attached File](https://apidocs.bitrix24.com/api-reference/tasks/tutorials/tasks/how-to-create-task-with-file.html)
- [How to Attach a Task to a SPA](https://apidocs.bitrix24.com/api-reference/tasks/tutorials/tasks/how-to-connect-task-to-spa.html)
- [How to Create a Comment in a Task and Attach a File](https://apidocs.bitrix24.com/api-reference/tasks/tutorials/tasks/how-to-create-comment-with-file.html)