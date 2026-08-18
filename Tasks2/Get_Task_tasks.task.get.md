---
title: "Get Task tasks.task.get | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/tasks-task-get.html"
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

The method `tasks.task.get` returns information about a task by its identifier.

Access to the data depends on permissions:

- administrators see all tasks,
- managers see their employees' tasks,
- others see only the tasks available to them.

## Method Parameters

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **id** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/data-types.html) | Task identifier.  The task identifier can be obtained when [creating a new task](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/rest-v3/tasks/tasks-task-add.html) or by the old method of [getting the list of tasks](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/tasks/tasks-task-list.html) |
| **select**   [`array`](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/data-types.html) | An array of fields that the method will return. If `select` is not specified, a basic set of task fields without related objects is returned.  For related objects, use a nested path with a dot, for example `["responsible.name","responsible.email"]` - the response will include the `responsible` object with the requested fields. [List of fields with related objects](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/rest-v3/tasks/fields.html) |

## Code Examples

[How to Use Examples in Documentation](https://apidocs.bitrix24.com/first-steps/how-to-use-examples.html)

The call to the new API differs by adding the `/api/` parameter in the request:

`https://{installation_address}/rest/api/{user_id}/{webhook_token}/tasks.task.get`

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
-d '{"id":8017,"select":["responsible.name","responsible.email"]}' \
https://**put_your_bitrix24_address**/rest/api/**put_your_user_id_here**/**put_your_webhook_here**/tasks.task.get
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"id":8017,"select":["responsible.name","responsible.email"],"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/api/tasks.task.get
```

The SDK does not yet support calls to the address /rest/api/. Use direct HTTP requests, for example, via curl, fetch.

```javascript
try
{
    const response = await $b24.callMethod(
        'tasks.task.get',
        {
            id: 8017,
            select: [
                'responsible.name',
                'responsible.email'
            ]
        }
    );
    
    const result = response.getData().result;
    console.log('Fetched task:', result);
    processResult(result);
}
catch( error )
{
    console.error('Error:', error);
}
```

The SDK does not yet support calls to the address /rest/api/. Use direct HTTP requests, for example, via curl, fetch.

```php
try {
    $response = $b24Service
        ->core
        ->call(
            'tasks.task.get',
            [
                'id' => 8017,
                'select' => [
                    'responsible.name',
                    'responsible.email'
                ]
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error fetching task: ' . $e->getMessage();
}
```

The SDK does not yet support calls to the address /rest/api/. Use direct HTTP requests, for example, via curl, fetch.

```js
BX24.callMethod(
    'tasks.task.get',
    {
        id: 8017,
        select: [
            'responsible.name',
            'responsible.email'
        ]
    },
    function(result){
        console.info(result.data());
        console.log(result);
    }
);
```

The SDK does not yet support calls to the address /rest/api/. Use direct HTTP requests, for example, via curl, fetch.

```php
require_once('crest.php');

$result = CRest::call(
    'tasks.task.get',
    [
        'id' => 8017,
        'select' => [
            'responsible.name',
            'responsible.email'
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
            "id": 3835,
            "title": "title",
            "description": "description",
            "responsible": {
                "name": "Alex",
                "email": "mail@bitrix.com"
            },
            "deadline": "2025-12-25T23:00:00+01:00",
            "needsControl": false,
            "startPlan": null,
            "endPlan": null,
            "fileIds": null,
            "checklist": [
                153,
                165
            ],
            "epicId": null,
            "storyPoints": null,
            "priority": "average",
            "status": "pending",
            "statusChanged": "2025-11-24T06:00:00+01:00",
            "parentId": null,
            "containsChecklist": true,
            "containsSubTasks": false,
            "containsRelatedTasks": false,
            "containsGanttLinks": false,
            "containsPlacements": true,
            "containsResults": false,
            "numberOfReminders": 0,
            "chatId": 2537,
            "plannedDuration": 0,
            "actualDuration": 0,
            "durationType": "days",
            "started": null,
            "estimatedTime": 0,
            "replicate": false,
            "changed": "2025-12-10T16:04:54+01:00",
            "closed": null,
            "activity": "2025-12-10T16:04:42+01:00",
            "guid": "{99502976-b2a2-4246-8d35-c6943b5ff242}",
            "xmlId": null,
            "exchangeId": null,
            "exchangeModified": null,
            "outlookVersion": 12,
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
            "link": "/company/personal/user/1/tasks/task/view/3835/",
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
            "archiveLink": "/bitrix/tools/disk/uf.php?entityId=3835&entity=TASKS_TASK&fieldName=UF_TASK_WEBDAV_FILES&signature=516ff0b54563ff935bbdf891590bed09bf4216db4fdf2df4df20425b7dd341e1&action=downloadArchiveByEntity&ncc=1",
            "crmItemIds": [
                "D_6529"
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
        "code": "BITRIX_REST_V3_EXCEPTION_ENTITYNOTFOUNDEXCEPTION",
        "message": "Record with ID = \`2\` not found"
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
| `id` | Required field `id` is not specified | Add `id` to the request body |
| `id` | Field `id` requires data type `int` for this request | Ensure that the value is a number, not a string |

Error Code: `BITRIX_REST_V3_EXCEPTION_ENTITYNOTFOUNDEXCEPTION`

| **Field** | **Error Description** | **How to Fix** |
| --- | --- | --- |
| `id` | Record with ID = `2` not found | Specify `id` of an existing task |

Error Code: `BITRIX_REST_V3_EXCEPTION_UNKNOWNDTOPROPERTYEXCEPTION`

| **Field** | **Error Description** | **How to Fix** |
| --- | --- | --- |
| `-` | Unknown field `status` for entity `TaskDto` | Specify existing fields in `select` for retrieving fields of related objects |

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