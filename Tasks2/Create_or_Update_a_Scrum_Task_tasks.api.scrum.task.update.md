---
title: "Create or Update a Scrum Task tasks.api.scrum.task.update | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/task/tasks-api-scrum-task-update.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/task/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user with access to Scrum

This method creates or updates a Scrum task. You will be able to:

- create a task in Scrum
- move a task from another project
- transfer it between the backlog and sprints
- change story points
- link an epic

A task must be created using the [tasks.task.add](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/task/api-reference/tasks/tasks-task-add.html) method or updated using the  [tasks.task.update](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/task/api-reference/tasks/tasks-task-update.html) method. Linking the task to Scrum is specified in the group identifier parameter  `GROUP_ID`.

You can obtain the group identifier using the [create new group](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/task/api-reference/sonet-group/sonet-group-create.html) method or the [get group list](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/task/api-reference/sonet-group/socialnetwork-api-workgroup-list.html) method. A group is considered Scrum if the  `SCRUM_MASTER_ID` field is filled.

## Method Parameters

| **Name**   `type` | **Description** |
| --- | --- |
| **id** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/task/api-reference/data-types.html) | Task identifier |
| **fields** \*   [`object`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/task/api-reference/data-types.html) | An object containing records about the Scrum task (detailed description provided [below](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/task/api-reference/sonet-group/scrum/task/tasks-api-scrum-task-update.html#parametr-fields)) in the following structure:  ```js fields: {     entityId: 'value'     storyPoints: 'value',     epicId: 'value',     sort: 'value' } ``` |

### Parameter fields

| **Name**   `type` | **Description** |
| --- | --- |
| **entityId**   `integer` | Identifier of the backlog or sprint.  If the value is not specified, *Bitrix24* will automatically add the task to the Scrum backlog if it exists |
| **storyPoints**   `string` | Story Points — a relative estimate of the task's complexity.  Can have a string value |
| **epicId**   `integer` | Epic identifier |
| **sort**   `integer` | Sorting |

## Code Examples

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
-d '{"id":1,"fields":{"epicId":1,"storyPoints":"8","entityId":2}}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/tasks.api.scrum.task.update
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"id":1,"fields":{"epicId":1,"storyPoints":"8","entityId":2},"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/tasks.api.scrum.task.update
```

```js
try
{
    const response = await $b24.callMethod(
        'tasks.api.scrum.task.update',
        {
            id: 1,
            fields: 
            {
                epicId: 1,
                storyPoints: '8',
                entityId: 2
            }
        }
    );
    
    const result = response.getData().result;
    console.log(result);
}
catch( error )
{
    console.error('Error:', error);
}
```

```php
try {
    $response = $b24Service
        ->core
        ->call(
            'tasks.api.scrum.task.update',
            [
                'id' => 1,
                'fields' => [
                    'epicId'      => 1,
                    'storyPoints' => '8',
                    'entityId'    => 2
                ]
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);
    // Your data processing logic
    processData($result);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error updating scrum task: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'tasks.api.scrum.task.update',
    {
        id: 1,
        fields: 
        {
            epicId: 1,
            storyPoints: '8',
            entityId: 2
        }
    },
    function(res)
    {
        console.log(res);
    }
);
```

```php
require_once('crest.php');

$result = CRest::call(
    'tasks.api.scrum.task.update',
    [
        'id' => 1,
        'fields' => [
            'epicId' => 1,
            'storyPoints' => '8',
            'entityId' => 2
        ]
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
    "status" : "success",
    "data" : true,
    "errors" : []
}
```

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **status**   `string` | Response status.  Possible values:  - `success` - `error` |
| **data**   `boolean` \| `null` | Returns:  - `true` — in case of success - `null` — in case of error |
| **errors**   `array` | Array of errors |

HTTP status: **400**

```json
{
    "error": 0,
    "error_description": "Task not found"
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Description** | **Value** |
| --- | --- | --- |
| `0` | Epic not found | Epic not found |
| `0` | Task not found | Task not found |
| `0` | Access denied | Access denied |
| `0` | Item not created | Task not added to Scrum |

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

- [Scrum Tasks: Overview of Methods](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/task/api-reference/sonet-group/scrum/task/index.html)
- [Get Scrum Task Fields by ID tasks.api.scrum.task.get](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/task/api-reference/sonet-group/scrum/task/tasks-api-scrum-task-get.html)
- [Get Scrum Task Fields tasks.api.scrum.task.getFields](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/task/api-reference/sonet-group/scrum/task/tasks-api-scrum-task-get-fields.html)