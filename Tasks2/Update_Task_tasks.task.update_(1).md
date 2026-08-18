---
title: "Update Task tasks.task.update | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/tasks-task-update.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/scopes/permissions.html)
> 
> Who can execute the method:
> 
> - any user with access to edit the task
> - task Creator

The method `tasks.task.update` updates a task.

## Method Parameters

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **taskId** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | Task identifier.  The task identifier can be obtained when [creating a new task](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-add.html) or by using the [get task list method](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-list.html) |
| **fields** \*   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | Values of [task fields](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/fields.html). At least one field must be provided in the parameter; otherwise, the method will return an error.  You can pass the `SE_PARAMETER` parameter to the method — a list of objects with additional task parameters. Possible values for the `CODE` codes:  - `1` — deadlines are determined by the deadlines of subtasks - `2` — automatically complete the task when subtasks are completed (and vice versa) - `3` — do not complete the task without a result  ```js SE_PARAMETER: [     {         VALUE: 'Y',         CODE: 3     },     {         VALUE: 'Y',         CODE: 2     } ] ``` |

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
-d '{"taskId":11,"fields":{"UF_CRM_TASK":["L_4","C_7","CO_5","D_10"],"UF_TASK_WEBDAV_FILES":["n12345","n67890"],"RESPONSIBLE_ID":123}}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/tasks.task.update
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"taskId":11,"fields":{"UF_CRM_TASK":["L_4","C_7","CO_5","D_10"],"UF_TASK_WEBDAV_FILES":["n12345","n67890"],"RESPONSIBLE_ID":123},"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/tasks.task.update
```

```js
try
{
    const response = await $b24.callMethod(
        "tasks.task.update",
        {
            taskId: 11, // Identifier of the task you want to update
            fields: {
                // Example of passing multiple values in the UF_CRM_TASK field
                UF_CRM_TASK: [
                    "L_4", // Link to lead with id 4
                    "C_7", // Link to contact with id 7
                    "CO_5", // Link to company with id 5
                    "D_10" // Link to deal with id 10
                ],
                // Example of passing multiple files in the UF_TASK_WEBDAV_FILES field
                UF_TASK_WEBDAV_FILES: [
                    "n12345", // Identifier of the first disk file
                    "n67890" // Identifier of the second disk file
                ],
                RESPONSIBLE_ID: 123 // Identifier of the new Participant
            }
        }
    );
    
    const result = response.getData().result;
    console.info("Task successfully updated");
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
            'tasks.task.update',
            [
                'taskId' => 11, // Identifier of the task you want to update
                'fields' => [
                    // Example of passing multiple values in the UF_CRM_TASK field
                    'UF_CRM_TASK' => [
                        'L_4', // Link to lead with id 4
                        'C_7', // Link to contact with id 7
                        'CO_5', // Link to company with id 5
                        'D_10' // Link to deal with id 10
                    ],
                    // Example of passing multiple files in the UF_TASK_WEBDAV_FILES field
                    'UF_TASK_WEBDAV_FILES' => [
                        'n12345', // Identifier of the first disk file
                        'n67890' // Identifier of the second disk file
                    ],
                    'RESPONSIBLE_ID' => 123 // Identifier of the new Participant
                ]
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Task successfully updated';

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error updating task: ' . $e->getMessage();
}
```

```javascript
BX24.callMethod(
     "tasks.task.update",
     {
         taskId: 11, // Identifier of the task you want to update
         fields: {
             // Example of passing multiple values in the UF_CRM_TASK field
             UF_CRM_TASK: [
                 "L_4", // Link to lead with id 4
                 "C_7", // Link to contact with id 7
                 "CO_5", // Link to company with id 5
                 "D_10" // Link to deal with id 10
             ],
             // Example of passing multiple files in the UF_TASK_WEBDAV_FILES field
             UF_TASK_WEBDAV_FILES: [
                 "n12345", // Identifier of the first disk file
                 "n67890" // Identifier of the second disk file
             ],
             RESPONSIBLE_ID: 123 // Identifier of the new Participant
         }
     },
     function(result) {
         if (result.error()) {
             console.error(result.error());
         } else {
             console.info("Task successfully updated");
         }
     }
 );
```

```php
require_once('crest.php');

$result = CRest::call(
    'tasks.task.update',
    [
        'taskId' => 11, // Identifier of the task you want to update
        'fields' => [
            // Example of passing multiple values in the UF_CRM_TASK field
            'UF_CRM_TASK' => [
                'L_4', // Link to lead with id 4
                'C_7', // Link to contact with id 7
                'CO_5', // Link to company with id 5
                'D_10' // Link to deal with id 10
            ],
            // Example of passing multiple files in the UF_TASK_WEBDAV_FILES field
            'UF_TASK_WEBDAV_FILES' => [
                'n12345', // Identifier of the first disk file
                'n67890' // Identifier of the second disk file
            ],
            'RESPONSIBLE_ID' => 123 // Identifier of the new Participant
        ]
    ]
);

if (isset($result['error'])) {
    echo 'Error: ' . $result['error_description'];
} else {
    echo 'Task successfully updated';
}
```

## Response Handling

HTTP Status: **200**

```json
{
    "result": {
        "task": {
            "id": "8157",
            "title": "Task Example",
            "description": "Task description with [B]formatting[/B]",
            "description": "",
            "mark": null,
            "priority": "1",
            "multitask": "N",
            "notViewed": "N",
            "replicate": "N",
            "stageId": "0",
            "sprintId": null,
            "backlogId": null,
            "createdBy": "503",
            "createdDate": "2025-10-06T17:40:12+02:00",
            "responsibleId": "503",
            "changedBy": "503",
            "changedDate": "2025-10-07T16:32:02+02:00",
            "statusChangedBy": "503",
            "closedBy": "0",
            "closedDate": null,
            "activityDate": "2025-10-07T16:29:55+02:00",
            "dateStart": null,
            "deadline": "2025-12-31T23:59:00+02:00",
            "startDatePlan": "2024-11-02T11:06:00+02:00",
            "endDatePlan": "2024-11-02T19:06:00+02:00",
            "guid": "{1a90e51d-5423-4c1e-b1a2-664a519b4612}",
            "xmlId": null,
            "commentsCount": "4",
            "serviceCommentsCount": "4",
            "allowChangeDeadline": "N",
            "allowTimeTracking": "N",
            "taskControl": "N",
            "addInReport": "N",
            "forkedByTemplateId": null,
            "timeEstimate": "0",
            "timeSpentInLogs": null,
            "matchWorkTime": "N",
            "forumTopicId": "1439",
            "forumId": "11",
            "siteId": "s1",
            "subordinate": "Y",
            "exchangeModified": null,
            "exchangeId": null,
            "outlookVersion": "8",
            "viewedDate": "2025-10-07T16:30:34+02:00",
            "sorting": null,
            "durationFact": null,
            "isMuted": "N",
            "isPinned": "N",
            "isPinnedInGroup": "N",
            "flowId": null,
            "descriptionInBbcode": "Y",
            "status": "2",
            "statusChangedDate": "2025-10-07T16:22:24+02:00",
            "durationPlan": "0",
            "durationType": "days",
            "favorite": "N",
            "groupId": "0",
            "auditors": ["503", "547"],
            "accomplices": [],
            "checklist": [],
            "group": [],
            "creator": {
                "id": "503",
                "name": "Maria Johnson",
                "link": "/company/personal/user/503/",
                "icon": "https://mysite.com/b17053/resize_cache/45749/c0120a8d7c10d63c83e32398d1ec4d9e/main/c89/c89c6b7301880958ea704b5a8470635c/4R5A1256.png",
                "workPosition": "Administrator"
            },
            "responsible": {
                "id": "503",
                "name": "Maria Johnson",
                "link": "/company/personal/user/503/",
                "icon": "https://mysite.com/b17053/resize_cache/45749/c0120a8d7c10d63c83e32398d1ec4d9e/main/c89/c89c6b7301880958ea704b5a8470635c/4R5A1256.png",
                "workPosition": "Administrator"
            },
            "accomplicesData": [],
            "auditorsData": {
                "547": {
                    "id": "547",
                    "name": "Helen",
                    "link": "/company/personal/user/547/",
                    "icon": "/bitrix/images/tasks/default_avatar.png",
                    "workPosition": "Lawyer"
                }
            },
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
                "take": false,
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
                    "userId": 503,
                    "createdBy": null,
                    "parentId": null,
                    "title": "",
                    "sortIndex": null,
                    "displaySortIndex": "",
                    "isComplete": false,
                    "isImportant": false,
                    "completedCount": 0,
                    "members": [],
                    "attachments": [],
                    "nodeId": null
                },
                "action": [],
                "descendants": []
            },
            "checkListCanAdd": true
        }
    },
    "time": {
        "start": 1759843922,
        "finish": 1759843922.725389,
        "duration": 0.7253890037536621,
        "processing": 0,
        "date_start": "2025-10-07T16:32:02+02:00",
        "date_finish": "2025-10-07T16:32:02+02:00",
        "operating_reset_at": 1759844522,
        "operating": 0.4929828643798828
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
    "error_description": "Cannot bind the node to itself\u003Cbr\u003E"
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Description** | **Value** |
| --- | --- | --- |
| `0` | wrong task id | The value in the `taskId` parameter is of an incorrect type |
| `100` | CTaskItem All parameters in the constructor must have real class type (internal error) | The required parameter `taskId` is missing |
| `0` | Action on the task is not allowed (internal error) | The user does not have permission to update the task or does not have access to the task |
| `100` | Could not find value for parameter {fields} (internal error) | The `fields` parameter is missing or empty |
| `ERROR_CORE` | The user specified in the "Responsible" field was not found\\u003Cbr\\u003E | The `RESPONSIBLE_ID` field contains the identifier of a non-existent user |
| `ERROR_CORE` | Invalid status\\u003Cbr\\u003E | An incorrect value is specified in the `STATUS` field |
| `ERROR_CORE` | The task specified in the "Parent Task" field was not found\\u003Cbr\\u003E | The `PARENT_ID` field contains the identifier of a non-existent task |
| `ERROR_CORE` | Cannot bind the node to itself\\u003Cbr\\u003E | The `PARENT_ID` field contains the identifier of the same task as in the `taskId` parameter |
| `ERROR_CORE` | Creating cyclic links in tasks is prohibited\\u003Cbr\\u003E | The `PARENT_ID` field contains the identifier of a subtask `taskId`. A subtask cannot become a parent task |
| `ERROR_CORE` | The end date specified in the scheduling is earlier than the start date\\u003Cbr\\u003E | The date and time in the `END_DATE_PLAN` field is earlier than in `START_DATE_PLAN` |
| `ERROR_CORE` | The duration of the task specified in the scheduling is too long\\u003Cbr\\u003E | The value in the `END_DATE_PLAN` field specifies a date that is too far in the future |

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
- [Get Task by ID tasks.task.get](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-get.html)
- [Get the list of tasks tasks.task.list](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-list.html)
- [Delete Task tasks.task.delete](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-delete.html)
- [Get the list of fields tasks.task.getFields](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-get-fields.html)
- [How to Upload a File to a Task](https://apidocs.bitrix24.com/api-reference/tasks/tutorials/tasks/how-to-upload-file-to-task.html)
- [How to Attach a Task to a SPA](https://apidocs.bitrix24.com/api-reference/tasks/tutorials/tasks/how-to-connect-task-to-spa.html)
- [How to Create a Comment in a Task and Attach a File](https://apidocs.bitrix24.com/api-reference/tasks/tutorials/tasks/how-to-create-comment-with-file.html)