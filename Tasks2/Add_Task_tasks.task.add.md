---
title: "Add Task tasks.task.add | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/tasks-task-add.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user

The method `tasks.task.add` adds a new task.

## Method Parameters

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **fields** \*   [`object`](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/data-types.html) | Task fields. To create a task, fill in the [required fields](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/rest-v3/tasks/tasks-task-add.html#fields); without them, the creation operation will not be executed. |

### Parameter fields

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **title** \*   [`string`](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/data-types.html) | Task title |
| **creatorId** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/data-types.html) | Creator's identifier.   The employee identifier can be obtained using the [user.get](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/user/user-get.html) method. |
| **responsibleId** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/data-types.html) | Executor's identifier.   The employee identifier can be obtained using the [user.get](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/user/user-get.html) method. |

[Description of all task fields](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/rest-v3/tasks/fields.html)

## Code Examples

[How to Use Examples in Documentation](https://apidocs.bitrix24.com/first-steps/how-to-use-examples.html)

The call to the new API differs by adding the parameter `/api/` in the request:

`https://{installation_address}/rest/api/{user_id}/{webhook_token}/tasks.task.add`

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
-d '{"fields":{"title":"Task Title","deadline":"2025-12-31T23:59:59+02:00","creatorId":29,"responsibleId":1,"crmItemIds":["L_1000959"]}}' \
https://**put_your_bitrix24_address**/rest/api/**put_your_user_id_here**/**put_your_webhook_here**/tasks.task.add
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"fields":{"title":"Task Title","deadline":"2025-12-31T23:59:59+02:00","creatorId":29,"responsibleId":1,"crmItemIds":["L_1000959"]},"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/api/tasks.task.add
```

The SDK does not yet support calls to the address /rest/api/. Use direct HTTP requests, for example, via curl or fetch.

```javascript
try
{
    const response = await $b24.callMethod(
        'tasks.task.add',
        {
            fields: {
                title: 'Task Title',
                deadline: '2025-12-31T23:59:59+02:00',
                creatorId: 29,
                responsibleId: 1,
                crmItemIds: ['L_1000959']
            }
        }
    );
    
    const result = response.getData().result;
    console.info('Task created with ID', result.item?.id);
}
catch( error )
{
    console.error(error);
}
```

The SDK does not yet support calls to the address /rest/api/. Use direct HTTP requests, for example, via curl or fetch.

```php
try {
    $response = $b24Service
        ->core
        ->call(
            'tasks.task.add',
            [
                'fields' => [
                    'title' => 'Task Title',
                    'deadline' => '2025-12-31T23:59:59+02:00',
                    'creatorId' => 29,
                    'responsibleId' => 1,
                    'crmItemIds' => ['L_1000959'],
                ],
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error creating task: ' . $e->getMessage();
}
```

The SDK does not yet support calls to the address /rest/api/. Use direct HTTP requests, for example, via curl or fetch.

```js
BX24.callMethod(
    'tasks.task.add',
    {
        fields: {
            title: 'Task Title',
            deadline: '2025-12-31T23:59:59+02:00',
            creatorId: 29,
            responsibleId: 1,
            crmItemIds: ['L_1000959']
        }
    },
    function(result){
        console.info(result.data());
        console.log(result);
    }
);
```

The SDK does not yet support calls to the address /rest/api/. Use direct HTTP requests, for example, via curl or fetch.

```php
require_once('crest.php');

$result = CRest::call(
    'tasks.task.add',
    [
        'fields' => [
            'title' => 'Task Title',
            'deadline' => '2025-12-31T23:59:59+02:00',
            'creatorId' => 29,
            'responsibleId' => 1,
            'crmItemIds' => ['L_1000959']
        ]
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
        "item": {
            "id": 3839,
            "title": "Task Title",
            "description": "",
            "deadline": "2026-01-01T00:59:59+03:00",
            "needsControl": false,
            "startPlan": null,
            "endPlan": null,
            "fileIds": null,
            "checklist": [],
            "epicId": null,
            "storyPoints": null,
            "priority": "average",
            "status": "pending",
            "statusChanged": null,
            "parentId": null,
            "containsChecklist": false,
            "containsSubTasks": false,
            "containsRelatedTasks": false,
            "containsGanttLinks": false,
            "containsPlacements": true,
            "containsResults": false,
            "numberOfReminders": 0,
            "chatId": 2603,
            "plannedDuration": 0,
            "actualDuration": 0,
            "durationType": "days",
            "started": null,
            "estimatedTime": 0,
            "replicate": false,
            "changed": "2025-12-11T12:25:33+03:00",
            "closed": null,
            "activity": "2025-12-11T12:25:33+03:00",
            "guid": "{13d2c44c-730e-45dd-b99c-fdaad4e3c1fa}",
            "xmlId": null,
            "exchangeId": null,
            "exchangeModified": null,
            "outlookVersion": 1,
            "mark": "none",
            "allowsChangeDeadline": false,
            "allowsTimeTracking": false,
            "matchesWorkTime": false,
            "addInReport": null,
            "isMultitask": false,
            "siteId": "s1",
            "deadlineCount": null,
            "declineReason": null,
            "forumTopicId": null,
            "link": "\/company\/personal\/user\/1\/tasks\/task\/view\/3839\/",
            "rights": {
                "read": true,
                "watch": true,
                "mute": true,
                "createResult": true,
                "edit": true,
                "remove": true,
                "complete": true,
                "approve": false,
                "disapprove": false,
                "start": true,
                "take": false,
                "delegate": true,
                "defer": true,
                "renew": false,
                "deadline": true,
                "datePlan": true,
                "changeDirector": false,
                "changeResponsible": true,
                "changeAccomplices": true,
                "pause": false,
                "timeTracking": false,
                "mark": true,
                "changeStatus": true,
                "reminder": true,
                "addAuditors": true,
                "elapsedTime": true,
                "favorite": true,
                "checklistAdd": true,
                "checklistEdit": true,
                "checklistSave": true,
                "checklistToggle": true,
                "automate": true,
                "resultEdit": false,
                "completeResult": true,
                "removeResult": false,
                "resultRead": false,
                "admin": true,
                "createSubtask": true,
                "copy": true,
                "saveAsTemplate": true,
                "attachFile": true,
                "detachFile": true,
                "detachParent": true,
                "createGanttDependence": true,
                "sort": false
            },
            "archiveLink": "\/bitrix\/tools\/disk\/uf.php?entityId=3839\u0026entity=TASKS_TASK\u0026fieldName=UF_TASK_WEBDAV_FILES\u0026signature=89f4f46e33905bcb0899c8cb9613a62cf8e104b182824e799d2aeb9d1e5bf526\u0026action=downloadArchiveByEntity\u0026ncc=1",
            "crmItemIds": [
                "L_1000959"
            ],
            "requireResult": false,
            "matchesSubTasksTime": false,
            "autocompleteSubTasks": false,
            "allowsChangeDatePlan": false,
            "maxDeadlineChangeDate": null,
            "maxDeadlineChanges": null,
            "requireDeadlineChangeReason": false,
            "inFavorite": [],
            "inPin": [],
            "inGroupPin": [],
            "inMute": [],
            "dependsOn": [],
            "scenarios": [
                "default"
            ]
        }
    },
    "time": {
        "start": 1765445133,
        "finish": 1765445134.139558,
        "duration": 1.1395580768585205,
        "processing": 1,
        "date_start": "2025-12-11T12:25:33+03:00",
        "date_finish": "2025-12-11T12:25:34+03:00",
        "operating_reset_at": 1765445733,
        "operating": 0
    }
}
```

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **result**   [`object`](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/data-types.html) | Object with response data |
| **item**   [`object`](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/data-types.html) | Object with task field values. [Description of task fields with related objects](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/rest-v3/tasks/fields.html) |
| **time**   [`time`](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/data-types.html#time) | Information about the request execution time |

HTTP Status: **400**

```json
{
    "error": {
        "code": "BITRIX_REST_V3_EXCEPTION_VALIDATION_REQUESTVALIDATIONEXCEPTION",
        "message": "Error validating the request object",
        "validation": [
            {
                "message": "The \`deadline\` field requires a \`DateTime\` data type for this request",
                "field": "deadline"
            }
        ]
    }
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error.code**   `string` | String error code. Use it to identify the type of exception |
| **error.message**   `string` | Text description of the error |
| **error.validation**   `array` | Array with error details. Present only in data validation errors `BITRIX_REST_V3_EXCEPTION_VALIDATION_REQUESTVALIDATIONEXCEPTION` |
| **error.validation\[\].field**   `string` | Name of the field where the validation error occurred |
| **error.validation\[\].message**   `string` | Description of the error related to the specified field |

Error Code: `BITRIX_REST_V3_EXCEPTION_VALIDATION_REQUESTVALIDATIONEXCEPTION`

| **Field** | **Error Description** | **How to Fix** |
| --- | --- | --- |
| `title`   `responsibleId`   `creatorId`   `fields` | Required field `#FIELD#` is missing | Add the specified field to the request body |
| `#FIELD#` | The `#FIELD#` field requires a data type of `#TYPE#` for this request | Ensure that the provided value is of the correct type |
| `responsibleId` | The user specified in the "Executor" field was not found | Specify the identifier of an existing user in the `responsibleId` field |
| `creatorId` | "" | Specify the identifier of an existing user in the `creatorId` field |
| `parentId` | The task specified in the "Parent Task" field was not found | Specify the identifier of an existing task in the `parentId` field |
| `endPlan` | The end date in the scheduling is earlier than the start date | Specify an `endPlan` date later than `startPlan` |
| `endPlan` | The scheduling indicates a task duration that is too long | Reduce the date in the `endPlan` field |

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

- [Update Task tasks.task.update](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/rest-v3/tasks/tasks-task-update.html)
- [Send Message to Task Chat tasks.task.chat.message.send](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/rest-v3/tasks/tasks-task-chat-message-send.html)
- [Delete Task tasks.task.delete](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/rest-v3/tasks/tasks-task-delete.html)
- [Attach Files to Task tasks.task.file.attach](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/rest-v3/tasks/tasks-task-file-attach.html)