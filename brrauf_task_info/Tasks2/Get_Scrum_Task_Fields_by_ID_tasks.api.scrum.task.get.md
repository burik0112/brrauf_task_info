---
title: "Get Scrum Task Fields by ID tasks.api.scrum.task.get | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/task/tasks-api-scrum-task-get.html"
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

This method retrieves the values of the Scrum task fields by its identifier `id`.

## Method Parameters

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **id** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/task/api-reference/data-types.html) | Task identifier |

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
-d '{"id":1}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/tasks.api.scrum.task.get
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"id":1,"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/tasks.api.scrum.task.get
```

```js
try
{
    const response = await $b24.callMethod(
        'tasks.api.scrum.task.get',
        {
            id: 1
        }
    );
    
    const result = response.getData().result;
    if (result.error())
    {
        console.error(result.error());
    }
    else
    {
        console.dir(result);
    }
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
            'tasks.api.scrum.task.get',
            [
                'id' => 1
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    if ($result->error()) {
        error_log($result->error());
        echo 'Error: ' . $result->error();
    } else {
        echo 'Success: ' . print_r($result->data(), true);
    }

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error getting scrum task: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'tasks.api.scrum.task.get',
    {
        id: 1
    },
        function(result)
    {
        if (result.error())
            console.error(result.error());
        else
            console.dir(result.data());
    }
);
```

```php
require_once('crest.php');

$result = CRest::call(
    'tasks.api.scrum.task.get',
    [
        'id' => 1
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
        "entityId": 2,
        "storyPoints": "2",
        "epicId": 4,
        "sort": 1,
        "createdBy": 1,
        "modifiedBy": 1
    },
    "time": {
        "start": 1721402687.900315,
        "finish": 1721402694.313811,
        "duration": 6.413496017456055,
        "processing": 6.387248992919922,
        "date_start": "2024-07-19T15:24:47+00:00",
        "date_finish": "2024-07-19T15:24:54+00:00",
        "operating": 6.387217998504639
    }
}
```

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **result**   [`object`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/task/api-reference/data-types.html) | Object with task data |
| **entityId**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/task/api-reference/data-types.html) | Identifier of the backlog or sprint |
| **storyPoints**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/task/api-reference/data-types.html) | Number of story points.  Data type is a string, as story points may not necessarily be a number |
| **epicId**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/task/api-reference/data-types.html) | Identifier of the epic |
| **sort**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/task/api-reference/data-types.html) | Sorting |
| **createdBy**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/task/api-reference/data-types.html) | Identifier of the user who created the task |
| **modifiedBy**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/task/api-reference/data-types.html) | Identifier of the user who last modified the task |
| **time**   [`array`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/task/api-reference/data-types.html#time) | Information about the time taken for the request |

HTTP Status: **200**

```json
{
    "error": 0,
    "error_description": "Task not found"
}
```

| **Code** | **Description** | **Value** |
| --- | --- | --- |
| `0` | Task not found | The task does not exist or the user does not have access to this task |
| `100` | Could not find value for parameter | The parameter name is incorrect or the parameter is not set |
| `100` | Invalid value {stringValue} to match with parameter {id}. Should be value of type int. | Invalid parameter type |

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
- [Create or Update a Scrum Task tasks.api.scrum.task.update](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/task/api-reference/sonet-group/scrum/task/tasks-api-scrum-task-update.html)
- [Get Scrum Task Fields tasks.api.scrum.task.getFields](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/task/api-reference/sonet-group/scrum/task/tasks-api-scrum-task-get-fields.html)