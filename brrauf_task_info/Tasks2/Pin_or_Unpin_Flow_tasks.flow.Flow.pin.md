---
title: "Pin or Unpin Flow tasks.flow.Flow.pin | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/flow/tasks-flow-flow-pin.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/scopes/permissions.html)
> 
> Who can execute the method: a user who can see the flow in the list of flows

This method pins or unpins a flow in the list of flows by its identifier.

## Method Parameters

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **flowId** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | The identifier of the flow to be pinned or unpinned.  You can obtain the identifier using the method to create a new flow [tasks.flow.Flow.create](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/tasks/flow/tasks-flow-flow-create.html) or the method to get a task [tasks.task.get](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/tasks/tasks-task-get.html) for a task from the flow |

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
https://your-domain.bitrix24.com/rest/_USER_ID_/_CODE_/tasks.flow.Flow.pin
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
-d '{
    "flowId": 517
}' \
https://your-domain.bitrix24.com/rest/tasks.flow.Flow.pin
```

```js
try
{
    const response = await $b24.callMethod(
        'tasks.flow.Flow.pin',
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
            'tasks.flow.Flow.pin',
            [
                'flowId' => 517
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    if ($result->error()) {
        error_log($result->error());
        echo 'Error: ' . $result->error();
    } else {
        echo 'Info: ' . print_r($result->data(), true);
    }

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error calling tasks.flow.Flow.pin: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'tasks.flow.Flow.pin',
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
    'tasks.flow.Flow.pin',
    [
        'flowId' => $flowId
    ]
);

// Processing the response from Bitrix24
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
    "result": true
}
```

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **result**   [`boolean`](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/data-types.html) | The result of the method execution. Possible values:  - `true` — flow is pinned - `false` — flow is unpinned |

HTTP status: **200**

```json
{
    "error": "0",
    "error_description": "Unknown error"
}
```

| **Code** | **Description** | **Additional Information** |
| --- | --- | --- |
| `0` | Access denied or flow not found | The account plan does not allow working with flows or the user does not have permission to perform the operation |
| `0` | Unknown error | Unknown error |

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
- [Get Flow tasks.flow.Flow.get](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/tasks/flow/tasks-flow-flow-get.html)
- [Update Flow tasks.flow.Flow.update](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/tasks/flow/tasks-flow-flow-update.html)
- [Delete Flow tasks.flow.Flow.delete](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/tasks/flow/tasks-flow-flow-delete.html)
- [Check the existence of the Flow tasks.flow.Flow.isExists](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/tasks/flow/tasks-flow-flow-is-exists.html)
- [Activate/Deactivate Flow tasks.flow.Flow.activate](https://apidocs.bitrix24.com/api-reference/tasks/flow/api-reference/tasks/flow/tasks-flow-flow-activate.html)